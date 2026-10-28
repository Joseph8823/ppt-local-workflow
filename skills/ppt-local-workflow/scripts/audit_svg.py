#!/usr/bin/env python3
"""Audit structured SVG sources. This does not render or validate PowerPoint."""

import argparse
import base64
import binascii
import json
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


SVG_NS = "http://www.w3.org/2000/svg"
XLINK = "{http://www.w3.org/1999/xlink}href"
DIMENSION = re.compile(r"^([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?)(?:px|pt|pc|cm|mm|in)?$")
REQUIRED_TEXT = ("font-family", "font-size", "font-weight", "fill", "x", "y", "text-anchor")


def local_name(name):
    return name.rsplit("}", 1)[-1]


def audit_file(path):
    path = Path(path)
    result = {
        "file": path.name,
        "counts": {"text": 0, "tspan": 0, "image": 0, "other": 0},
        "view_box": None,
        "root_dimensions": {},
        "errors": [],
        "warnings": [],
        "powerpoint_validation": "not_performed",
        "visually_verified": False,
    }
    errors, warnings = result["errors"], result["warnings"]
    try:
        source = path.read_text(encoding="utf-8-sig")
        if re.search(r"<!DOCTYPE|<!ENTITY|<\?xml-stylesheet", source, re.I):
            errors.append("Document entities, doctypes or external stylesheet processing instructions are not allowed.")
            return result
        root = ET.fromstring(source)
    except (OSError, UnicodeError, ET.ParseError) as error:
        errors.append(f"Cannot read SVG XML: {error}")
        return result
    if root.tag != f"{{{SVG_NS}}}svg":
        errors.append("Root must be an SVG element with the SVG namespace.")
    for attribute in ("width", "height"):
        value = root.get(attribute, "")
        result["root_dimensions"][attribute] = value
        dimension = DIMENSION.fullmatch(value)
        numeric = float(dimension.group(1)) if dimension else math.nan
        if not math.isfinite(numeric) or numeric <= 0:
            errors.append(f"Root {attribute} must be an explicit finite positive absolute dimension.")
    try:
        view_box = [float(value) for value in re.split(r"[\s,]+", root.get("viewBox", "").strip())]
        if len(view_box) != 4 or not all(math.isfinite(value) for value in view_box) or min(view_box[2:]) <= 0:
            raise ValueError()
        result["view_box"] = view_box
    except ValueError:
        errors.append("viewBox must contain four finite numbers with positive width and height.")

    seen_ids = set()
    texts = []
    for index, element in enumerate(root.iter()):
        tag = local_name(element.tag)
        label = f"{tag}[{index}]"
        if tag in result["counts"]:
            result["counts"][tag] += 1
        elif tag in ("rect", "circle", "ellipse", "line", "polyline", "polygon", "path", "use"):
            result["counts"]["other"] += 1
        if tag in ("script", "foreignObject", "textPath", "style"):
            errors.append(f"{label}: unsupported {tag}; use native text and explicit attributes.")
        element_id = element.get("id")
        if element_id:
            if element_id in seen_ids:
                errors.append(f"{label}: duplicate id.")
            seen_ids.add(element_id)
        for attribute, value in element.attrib.items():
            if local_name(attribute).lower().startswith("on"):
                errors.append(f"{label}: event-handler attributes are not allowed.")
            for reference in re.findall(r"url\(\s*['\"]?([^)'\"\s]+)", value, flags=re.I):
                if not reference.startswith("#"):
                    errors.append(f"{label}: external CSS URL is not self-contained.")
            if local_name(attribute) == "href" and tag != "image" and not value.startswith("#"):
                errors.append(f"{label}: external reference is not self-contained.")
        if tag in ("text", "tspan"):
            for attribute in ("x", "y", "dx", "dy", "rotate"):
                if attribute in element.attrib and len(re.split(r"[\s,]+", element.get(attribute).strip())) > 1:
                    errors.append(f"{label}: per-character coordinate list in {attribute}.")
            if tag == "tspan":
                warnings.append(f"{label}: verify partial-line emphasis does not split or move after conversion.")
            else:
                for attribute in REQUIRED_TEXT:
                    if not element.get(attribute, "").strip():
                        errors.append(f"{label}: missing explicit {attribute}.")
                texts.append("".join(element.itertext()).strip())
        if tag == "image":
            href = element.get("href") or element.get(XLINK, "")
            match = re.fullmatch(r"data:image/(png|jpeg|jpg|gif|webp);base64,([\s\S]+)", href, flags=re.I)
            if not match:
                errors.append(f"{label}: image must be embedded as a complete base64 raster image.")
                continue
            try:
                data = base64.b64decode(re.sub(r"\s+", "", match.group(2)), validate=True)
                subtype = match.group(1).lower()
                valid = {
                    "png": data.startswith(b"\x89PNG\r\n\x1a\n"),
                    "jpeg": data.startswith(b"\xff\xd8\xff"),
                    "jpg": data.startswith(b"\xff\xd8\xff"),
                    "gif": data.startswith((b"GIF87a", b"GIF89a")),
                    "webp": data.startswith(b"RIFF") and data[8:12] == b"WEBP",
                }[subtype]
                if not valid:
                    raise ValueError("signature does not match image type")
            except (ValueError, binascii.Error) as error:
                errors.append(f"{label}: invalid base64 image: {error}.")
    if len(texts) >= 10 and sum(len(text) == 1 for text in texts) / len(texts) > 0.5:
        warnings.append("Many single-character text objects: inspect for prohibited per-character reconstruction.")
    if not texts:
        warnings.append("No native text found; confirm this is intentionally an artwork-only SVG.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="One SVG file or a directory of SVG files")
    parser.add_argument("--output", type=Path, help="Write JSON to a project output path")
    args = parser.parse_args()
    files = sorted(args.source.glob("*.svg")) if args.source.is_dir() else [args.source]
    if not files:
        parser.error("No SVG files found.")
    results = [audit_file(path) for path in files]
    report = {
        "schema_version": 1,
        "structure_ok": all(not item["errors"] for item in results),
        "powerpoint_validation": "not_performed",
        "files": results,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0 if report["structure_ok"] else 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
