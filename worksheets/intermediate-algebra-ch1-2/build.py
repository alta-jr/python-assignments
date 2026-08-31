#!/usr/bin/env python3
"""Render the Chapter 1-2 handouts to print-ready PDFs.

Usage:  python3 build.py            # renders every handout into pdf/
        python3 build.py quiz-review.html

Requires: pip install playwright  (and a Chromium build).
Set CHROME_PATH if Playwright's bundled browser is not the one you want.
"""

import os
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent.resolve()
OUT = HERE / "pdf"

DOCS = [
    "review-worksheet.html",
    "review-solutions.html",
    "quiz-review.html",
]


def find_chrome():
    """Prefer $CHROME_PATH, then any Chromium already on this machine."""
    if os.environ.get("CHROME_PATH"):
        return os.environ["CHROME_PATH"]
    for pattern in ("chromium-*/chrome-linux/chrome", "chromium-*/chrome-mac/Chromium.app"):
        for candidate in sorted(pathlib.Path("/opt/pw-browsers").glob(pattern), reverse=True):
            if candidate.exists():
                return str(candidate)
    return None  # let Playwright use its own download


def main(names):
    OUT.mkdir(exist_ok=True)
    chrome = find_chrome()
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=chrome) if chrome else pw.chromium.launch()
        page = browser.new_page()
        for name in names:
            src = HERE / name
            if not src.exists():
                sys.exit(f"no such handout: {name}")
            dest = OUT / (src.stem + ".pdf")
            page.goto(src.as_uri())
            page.emulate_media(media="print")
            page.pdf(
                path=str(dest),
                format="Letter",
                print_background=True,
                margin={"top": "0.6in", "bottom": "0.7in", "left": "0.65in", "right": "0.65in"},
                display_header_footer=True,
                header_template="<div></div>",
                footer_template=(
                    '<div style="width:100%;font-size:8pt;color:#888;'
                    'padding:0 0.65in;font-family:Helvetica,Arial,sans-serif;">'
                    '<span style="float:right">Page <span class="pageNumber"></span> '
                    'of <span class="totalPages"></span></span></div>'
                ),
            )
            print(f"{name}  ->  pdf/{dest.name}")
        browser.close()


if __name__ == "__main__":
    main(sys.argv[1:] or DOCS)
