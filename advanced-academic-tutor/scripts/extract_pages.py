#!/usr/bin/env python3
"""Extract PDF text page by page so tutoring citations point to real pages.

Writes one file per page, <stem>.pNNN.txt, into the output directory and
reports pages with no text layer (likely scanned; they need OCR).

Backends, in order: pdftotext/pdfinfo (Poppler), then the pypdf package.
Write the output into the learner's course folder, never into the skill package.

Usage:
    python3 extract_pages.py Notes.pdf --out ~/course/extracted
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def page_count_poppler(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True).stdout
    match = re.search(r"^Pages:\s+(\d+)", out, re.MULTILINE)
    if not match:
        raise RuntimeError("pdfinfo did not report a page count")
    return int(match.group(1))


def pages_poppler(pdf):
    for n in range(1, page_count_poppler(pdf) + 1):
        text = subprocess.run(
            ["pdftotext", "-f", str(n), "-l", str(n), "-layout", str(pdf), "-"],
            capture_output=True, text=True, check=True,
        ).stdout
        yield n, text


def pages_pypdf(pdf):
    from pypdf import PdfReader  # imported lazily: optional dependency

    for n, page in enumerate(PdfReader(str(pdf)).pages, start=1):
        yield n, page.extract_text() or ""


def choose_backend():
    if shutil.which("pdftotext") and shutil.which("pdfinfo"):
        return "pdftotext", pages_poppler
    try:
        import pypdf  # noqa: F401
        return "pypdf", pages_pypdf
    except ImportError:
        return None, None


def main():
    parser = argparse.ArgumentParser(description="Extract PDF text one file per page.")
    parser.add_argument("pdf", type=Path, help="PDF file to extract")
    parser.add_argument("--out", type=Path, required=True,
                        help="output directory (in the learner's course folder)")
    args = parser.parse_args()

    pdf = args.pdf.expanduser()
    if not pdf.is_file():
        sys.exit(f"error: {pdf} not found")

    name, backend = choose_backend()
    if backend is None:
        sys.exit("error: no PDF backend found. Install Poppler (pdftotext, pdfinfo) "
                 "or run: pip install pypdf")

    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)

    empty, total = [], 0
    try:
        for n, text in backend(pdf):
            total = n
            (out / f"{pdf.stem}.p{n:03d}.txt").write_text(text, encoding="utf-8")
            if not text.strip():
                empty.append(n)
    except Exception as exc:  # report and stop; partial output stays on disk
        sys.exit(f"error: extraction failed after page {total} ({name}): {exc}")

    print(f"{pdf.name}: {total} pages extracted to {out} using {name}")
    if empty:
        print(f"No text layer (likely needs OCR): pages {', '.join(map(str, empty))}")
    print("Note: printed page labels may differ from PDF page indices; "
          "cite the printed label when visible.")


if __name__ == "__main__":
    main()
