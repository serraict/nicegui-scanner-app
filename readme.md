# NiceGUI barcode scanner app

[![PyPI version](https://badge.fury.io/py/nicegui-scanner.svg)](https://pypi.org/project/nicegui-scanner/)
[![Release](https://github.com/serraict/nicegui-scanner-app/actions/workflows/release.yml/badge.svg)](https://github.com/serraict/nicegui-scanner-app/actions/workflows/release.yml)

This project demonstrates how to create a barcode scanner using the [ZXing library] wrapped in a [NiceGUI] custom Vue component.
Based on [this discussion](https://github.com/zauberzeug/nicegui/discussions/5016),
and inspired by the [custom vue component example].

## Usage

Install the package from PyPI:

```bash
pip install nicegui nicegui-scanner
```

### Basic Example

Create a simple barcode scanner app (save as `scanner_app.py`):

```python
from nicegui import ui
from nicegui_scanner import BarcodeScanner

def on_scan(event):
    ui.notify(f"Scanned: {event.args}")

scanner = BarcodeScanner(on_scan=on_scan)
scanner.create_controls()

ui.run()
```

Then run: `python scanner_app.py`

### Features

- **Easy Integration**: Drop-in component for NiceGUI apps - no additional setup require after pip install
- **Camera Selection**: Automatic camera detection with settings UI
- **Flexible Styling**: Use standard CSS via `.style()` method
- **Multiple Formats**: Supports QR codes, barcodes, and more via ZXing

### Examples

See the `examples/` directory for:

- `app.py` - Multiple scanner configurations
- `pages.py` - Usage with NiceGUI pages

## Development

To develop this component, install dependencies and run the example app:

```bash
npm install  # Install ZXing library
uv sync      # Install Python dependencies
make dev     # Run example app
```

This will start the example app on <http://localhost:3001> with multiple scanner demos.

[ZXing library]: https://www.npmjs.com/package/@zxing/library
[NiceGUI]: https://nicegui.io/
[custom vue component example]: https://github.com/zauberzeug/nicegui/tree/main/examples/custom_vue_component
