from pathlib import Path
import shlex

import paramiko


LOGIN = "kali"
PASSWORD = "kali"
IP = "127.0.0.1"
SSH_PORT = 2222

REMOTE_XML = "results_xccdf.xml"
REMOTE_DATASTREAM = "/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml"
REMOTE_PROFILE = "xccdf_org.ssgproject.content_profile_standard"


def run_ssh(ssh, password, command, use_sudo=False, allowed_codes=(0,)):
    if use_sudo:
        command = f"echo {shlex.quote(password)} | sudo -S -p '' bash -lc {shlex.quote(command)}"

    _, stdout, stderr = ssh.exec_command(command, get_pty=True)
    code = stdout.channel.recv_exit_status()
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")

    if code not in allowed_codes:
        raise RuntimeError(f"\nCOMMAND: {command}\nCODE: {code}\nSTDOUT:\n{out}\nSTDERR:\n{err}")

    return out


def virtual_check(login, password, ip, port):
    if not login or not password or not ip or not port:
        raise ValueError("Передай login, password, ip и port")

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
                    f"--profile {REMOTE_PROFILE}",
                    f"--results {remote_dir}/{REMOTE_XML}",
                    REMOTE_DATASTREAM,
                ]
            ),
            use_sudo=True,
            allowed_codes=(0, 2),
        )

        local_xml = Path(REMOTE_XML)
        with ssh.open_sftp() as sftp:
            sftp.get(f"{remote_dir}/{REMOTE_XML}", str(local_xml))

    finally:
        ssh.close()

    return str(local_xml)
