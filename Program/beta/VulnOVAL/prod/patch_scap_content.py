from pathlib import Path
import re

def patch_SCAP_content(system_cpe: str):
    if system_cpe == "Kali Linux":
        path = Path(r"/usr/share/xml/scap/ssg/content/ssg-debian13-ds.xml")
        text = path.read_text(encoding="utf-8")
        pattern = re.compile(r'^\s*<oval-def:criterion comment="Debian13 is installed" test_ref="oval:ssg-test_debian_13:tst:1"/>\r?\n?',re.MULTILINE)
        # регулярка сверху скипает сколько угодно пробелов до самого текста, а re.MULTILINE применяет такую операцию для каждой строки
        new_text, count = pattern.subn("", text, count=1)  # выполняет замену на пустую строку
        if count != 0:
            print(f"при патчинге было изменено {count} строк")
        if count == 0:
            print("патчинг не прошёл")
        backup = path.with_suffix(path.suffix + ".bak")
        backup.write_text(text, encoding="utf-8")
        path.write_text(new_text, encoding="utf-8")
