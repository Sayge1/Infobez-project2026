import subprocess

def do_xccdf_scan(system_cpe: str, remediation: int):
    if system_cpe == "Kali Linux":
        try:
            if remediation == 1:
                subprocess.run(
                    [
                        "oscap", "xccdf", "eval",
                        "--skip-signature-validation",
                        "--profile", "xccdf_org.ssgproject.content_profile_standard",
                        "--results", "results_xccdf.xml",
                        "--report", "report_xccdf.html",
                        "--remediate",
                        "/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml",
                    ],
                    capture_output=True,
                    text=True,
                )
            else:
                subprocess.run(
                    [
                        "oscap", "xccdf", "eval",
                        "--skip-signature-validation",
                        "--profile", "xccdf_org.ssgproject.content_profile_standard",
                        "--results", "results_xccdf.xml",
                        "--report", "report_xccdf.html",
                        "/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml",
                    ],
                    capture_output=True,
                    text=True,
                )
        except subprocess.CalledProcessError as error:
            stderr = error.stderr
            raise SystemExit(f"Ошибка запуска oscap: {stderr}")

def do_oval_scan(system_cpe: str):
    if system_cpe == "Kali Linux":
        try:
            subprocess.run(
                [
                    "oscap", "oval", "eval",
                    "--results", "results_oval.xml",
                    "--report", "report_oval.html",
                    "/usr/share/xml/scap/ssg/content/ssg-debian13-cpe-oval.xml",
                ],
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as error:
            stderr = error.stderr
            raise SystemExit(f"Ошибка запуска oscap: {stderr}")
