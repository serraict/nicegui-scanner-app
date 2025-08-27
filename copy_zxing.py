#!/usr/bin/env python3
"""Copy ZXing library to package static directory."""

import shutil
import os

# Ensure the directory exists
os.makedirs("src/nicegui_scanner/static", exist_ok=True)

# Copy the ZXing library
shutil.copy2(
    "node_modules/@zxing/library/umd/index.min.js",
    "src/nicegui_scanner/static/zxing.min.js",
)

print("ZXing library copied to package static directory")
