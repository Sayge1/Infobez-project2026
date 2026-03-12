import subprocess

def apt_install(package_name: str):
    try:
        subprocess.run(["apt", "install", "-y", package_name],check=True,capture_output=True,text=True)
    except subprocess.CalledProcessError as error:
        stderr = error.stderr
        raise SystemExit(f"{package_name} {stderr}")

def download_SCAP_content(system_cpe: str):
    if system_cpe == "Kali Linux":
        apt_install("openscap-scanner")
        apt_install("ssg-debian")

