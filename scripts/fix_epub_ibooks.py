#!/usr/bin/env python3
"""Patch Apple Books display options so themes work on iOS dark mode."""

from __future__ import annotations

import sys
import tempfile
import zipfile
from pathlib import Path

DISPLAY_OPTIONS = "META-INF/com.apple.ibooks.display-options.xml"
PATCHED = b"""<?xml version="1.0" encoding="UTF-8"?>
<display_options>
  <platform name="*">
    <option name="specified-fonts">false</option>
  </platform>
</display_options>
"""


def patch_epub(path: Path) -> None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".epub") as tmp:
        tmp_path = Path(tmp.name)

    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(
        tmp_path, "w", compression=zipfile.ZIP_DEFLATED
    ) as zout:
        for info in zin.infolist():
            data = (
                PATCHED
                if info.filename == DISPLAY_OPTIONS
                else zin.read(info.filename)
            )
            new_info = zipfile.ZipInfo(
                filename=info.filename,
                date_time=info.date_time,
            )
            new_info.compress_type = info.compress_type
            new_info.external_attr = info.external_attr
            new_info.internal_attr = info.internal_attr
            if info.filename == "mimetype":
                new_info.compress_type = zipfile.ZIP_STORED
            zout.writestr(new_info, data)

    tmp_path.replace(path)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <file.epub>", file=sys.stderr)
        return 1
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"error: {path} not found", file=sys.stderr)
        return 1
    patch_epub(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
