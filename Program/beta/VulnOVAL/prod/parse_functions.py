import xml.etree.ElementTree as ET


def parse_oval(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot() #начальный парсинг XML
    except Exception as e:
        print(e)
        return []

    definitions = {} #тут по айди будут храниться названия и описания
    scan_results = [] #тут по айди будут результаты проверки


    for el in root.findall(".//{*}definition"):
        id_of_definition = el.get('id')

        metadata = el.find(".//{*}metadata")
        if metadata is not None:
            title = "Unknown"
            description = ""

            title_el = metadata.find(".//{*}title")
            if title_el is not None and title_el.text:
                title = title_el.text

            desc_el = metadata.find(".//{*}description")
            if desc_el is not None and desc_el.text:
                description = desc_el.text

            definitions[id_of_definition] = {
                'title': title,
                'description': description
            }
            continue


        res_attr = el.get('result') #если в элементе не находится метадата - значит это результат проверки
        def_id_ref = el.get('definition_id')

        if res_attr and def_id_ref:
            scan_results.append({
                'id': def_id_ref,
                'result': res_attr
            })

    final_out = []

    if not definitions:
        print("в результатах нет definitions")

    for item in scan_results:
        did = item['id']
        meta = definitions.get(did, {}) #пробуем взять по id definition информацию, если не получается - пустой словарь

        final_out.append({
            'id': did,
            'cve': meta.get('title', 'N/A'),
            'result': item['result'],
            'description': meta.get('description', '').replace('\n', ' ').strip() #заменяем перенос строк на пробелы и убираем их по краям
        })

    return final_out

def parse_xccdf(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Ошибка открытия XML: {e}")
        return []

    def _text(elem):
        if elem is None:
            return ""
        return " ".join("".join(elem.itertext()).split())

    rules_map = {}
    scan_results = []

    for rule in root.findall(".//{*}Rule"):
        rid = rule.get("id")
        if not rid:
            continue

        title = _text(rule.find("./{*}title")) or "Unknown"
        description = _text(rule.find("./{*}description"))  # может быть длинным
        severity = rule.get("severity") or _text(rule.find("./{*}severity")) or ""


        cves = []
        for ident in rule.findall(".//{*}ident"):
            t = _text(ident)
            if "CVE-" in t:
                parts = [p.strip(",;") for p in t.replace("\n", " ").split()]
                cves.extend([p for p in parts if p.startswith("CVE-")])


        seen = set()
        cves_unique = []
        for c in cves:
            if c not in seen:
                seen.add(c)
                cves_unique.append(c)

        rules_map[rid] = {
            "title": title,
            "description": description,
            "severity": severity,
            "cves": cves_unique,
        }


    for tr in root.findall(".//{*}TestResult"):

        profile_id = tr.get("profile") or _text(tr.find("./{*}profile"))
        target = _text(tr.find("./{*}target"))

        for rr in tr.findall(".//{*}rule-result"):
            idref = rr.get("idref")
            res_elem = rr.find("./{*}result")
            result = _text(res_elem)

            if not idref or not result or result == "notselected":
                continue

            scan_results.append({
                "id": idref,
                "result": result,
                "profile": profile_id,
                "target": target,
            })

    final_output = []
    for item in scan_results:
        rid = item["id"]
        meta = rules_map.get(rid, {})

        final_output.append({
            "id": rid,
            "cve": ", ".join(meta.get("cves", [])) if meta.get("cves") else "N/A",
            "result": item["result"],
            "severity": meta.get("severity", "N/A") or "N/A",
            "title": meta.get("title", "N/A"),
            "description": (meta.get("description", "") or "").replace("\n", " ").strip(),
            "profile": item.get("profile") or "N/A",
            "target": item.get("target") or "N/A",
        })

    return final_output

