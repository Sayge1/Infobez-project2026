import winreg
def find_all_programs(hive, flag): # находит все программы по hkey
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
                          0, winreg.KEY_READ | flag)
    count_subkey = winreg.QueryInfoKey(aKey)[0]
    software_list = []
    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'

            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'

            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


def get_unique_programs():  # Возвращает список словарей
    software_list = []

    software_list += find_all_programs(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY)
    software_list += find_all_programs(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)
    software_list += find_all_programs(winreg.HKEY_CURRENT_USER, 0)

    unique_software = {v['name']: v for v in software_list}.values()
    return sorted(unique_software, key=lambda x: x['name'])

##
import subprocess
import xml.etree.ElementTree as ET


def scan_oval(oval_file):
    cmd = [
        "oscap", "oval", "eval",
        "--results", "results_oval_old.xml",
        oval_file
    ]

    try:
        subprocess.run(cmd, check=False, capture_output=True)

        tree = ET.parse("results_oval_old.xml")
        root = tree.getroot()


        ns = {'oval-res': 'http://oval.mitre.org/XMLSchema/oval-results-5'}
        for system in root.findall('.//oval-res:system', ns):
            for test in system.findall('.//oval-res:test', ns):
                test_id = test.get('test_id')
                result = test.get('result')
                print(f"Test {test_id}: {result}")

    except FileNotFoundError:
        print("Ошибка: Утилита 'oscap' не установлена.")


scan_oval("rhba-2023.xml")