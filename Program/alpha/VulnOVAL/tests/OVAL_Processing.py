#!/usr/bin/env python3
# coding: utf-8

"""
parse_local_oscap_result.py

Анализирует существующий XCCDF/ARF результат в папке проекта.
НЕ запускает oscap, а только парсит XML!
"""

import sys
import json
import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, List

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger("oscap-parser")


# ------------ XML UTILS ------------
def local_name(tag: str) -> str:
    return tag.split('}')[-1] if tag else ""


def find_descendant_by_localname(elem: ET.Element, names: List[str]):
    for s in elem.iter():
        if local_name(s.tag) in names:
            return s
    return None


def text_of(e):
    if e is None:
        return None
    return (e.text or "").strip()


# ------------ PARSER ------------
def parse_xccdf_results(xml_path: Path):
    logger.info(f"Чтение XML результата: {xml_path}")
    tree = ET.parse(str(xml_path))
    root = tree.getroot()

    rules = []
    counts = {}

    rule_results = [elem for elem in root.iter() if local_name(elem.tag) == "rule-result"]
    if not rule_results:
        raise RuntimeError("Не найдено rule-result в файле!")

    for rr in rule_results:

        rule_id = rr.get("idref") or rr.get("id")

        title_node = find_descendant_by_localname(rr, ["title"])
        title = text_of(title_node)

        result_node = find_descendant_by_localname(rr, ["result", "status"])
        result_raw = text_of(result_node) or "unknown"

        note_node = find_descendant_by_localname(rr, ["note", "check", "message"])
        note = text_of(note_node)

        # нормализация
        r = result_raw.lower()
        if r.startswith("pass"):
            norm = "pass"
        elif r.startswith("fail"):
            norm = "fail"
        elif "fixed" in r:
            norm = "fixed"
        elif "notapp" in r:
            norm = "notapplicable"
        elif "error" in r:
            norm = "error"
        else:
            norm = "unknown"

        rules.append({
            "rule_id": rule_id,
            "rule_title": title,
            "result_raw": result_raw,
            "result": norm,
            "note": note
        })

        counts[norm] = counts.get(norm, 0) + 1

    summary = {"total": len(rules)}
    summary.update(counts)

    return summary, rules


# ------------ SEARCH FOR RESULTS FILE ------------
def find_local_result_file() -> Optional[Path]:
    """Ищет XML-файл результата в папке проекта"""

    candidates = [
        "results_oval_old.xml",
        "result.xml",
        "xccdf-result.xml",
        "oscap-results_oval_old.xml",
        "report.xml",
    ]

    # 1. Проверяем прямые имена в корне
    for name in candidates:
        p = Path(name)
        if p.exists():
            return p

    # 2. Папка results/
    results_dir = Path("results")
    if results_dir.is_dir():
        for xml in results_dir.rglob("*.xml"):
            return xml

    return None


# ------------ MAIN ------------
def main():
    xml_file = find_local_result_file()

    if not xml_file:
        print("❌ Не найден ни один XML результат в папке проекта.")
        print("Ожидаемые файлы: results_oval_old.xml, result.xml, xccdf-result.xml, report.xml, или ./results/*.xml")
        sys.exit(1)

    summary, rules = parse_xccdf_results(xml_file)

    # -------- ПЕЧАТЬ УЯЗВИМОСТЕЙ --------
    print("\n=== Детальный анализ правил (уязвимостей) ===\n")

    for r in rules:
        if r["result"] in ("fail", "error"):
            status = "НАЙДЕНА уязвимость"
        elif r["result"] in ("pass", "fixed"):
            status = "НЕ найдена"
        elif r["result"] == "notapplicable":
            status = "Неприменимо"
        else:
            status = "Неизвестно"

        print(f"[{status}] Rule ID: {r['rule_id']}")
        print(f"Название : {r['rule_title']}")
        print(f"Статус   : {r['result_raw']}")
        if r["note"]:
            print(f"Примечание: {r['note']}")
        print("-" * 60)

    # -------- СВОДКА --------
    print("\n=== Итог ===")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


main()