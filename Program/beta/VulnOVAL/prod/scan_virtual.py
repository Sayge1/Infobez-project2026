from pathlib import Path
import shlex
import paramiko

remote_xml = "results_xccdf.xml"
remote_datastream = "/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml"
remote_profile = "xccdf_org.ssgproject.content_profile_standard"
def run_ssh(ssh, password, command, use_sudo=False):
    if use_sudo:
        command = f"echo {shlex.quote(password)} | sudo -S -p '' bash -lc {shlex.quote(command)}"

    _, stdout, stderr = ssh.exec_command(command, get_pty=True)
    out = stdout.read().decode("utf-8", errors="replace")

    return out
def virtual_check(login, password, ip, port):
    port = int(port)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=ip,
        port=port,
        username=login,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )

    try:
        run_ssh(
            ssh,
            password,
            "apt-get update && apt-get install -y --reinstall openscap-scanner ssg-debian",
            use_sudo=True,
        )

        run_ssh(
            ssh,
            password,
            """python3 -c "from pathlib import Path; import re; p=Path('/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml'); t=p.read_text(encoding='utf-8'); n=re.sub(r'^\\s*<oval-def:criterion comment=\\"Debian13 is installed\\" test_ref=\\"oval:ssg-test_debian_13:tst:1\\"/>\\r?\\n?', '', t, count=1, flags=re.MULTILINE); p.with_suffix(p.suffix + '.bak').write_text(t, encoding='utf-8'); p.write_text(n, encoding='utf-8')" """,
            use_sudo=True,
        )

        remote_dir = run_ssh(ssh, password, "mktemp -d /tmp/vulnoval-ssh-XXXXXX").strip()

        run_ssh(
            ssh,
            password,
            " ".join(
                [
                    "oscap xccdf eval",
                    "--skip-signature-validation",
                    f"--profile {remote_profile}",
                    f"--results {remote_dir}/{remote_xml}",
                    remote_datastream,
                ]
            ),
            use_sudo=True,
        )

        local_xml = Path(remote_xml)
        with ssh.open_sftp() as sftp:
            sftp.get(f"{remote_dir}/{remote_xml}", str(local_xml))

    finally:
        ssh.close()

    return str(local_xml)
