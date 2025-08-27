# NiceGUI barcode scanner app

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
    barcode = event.args
    ui.notify(f"Scanned: {barcode}")

ui.html("<h1>My Barcode Scanner</h1>")

# Create scanner with custom styling  
scanner = BarcodeScanner(on_scan=on_scan).style(
    "width: 400px; height: 300px; border: 2px solid #007acc;"
)

# Add controls
with ui.row():
    ui.button("Start", on_click=scanner.start_scanning)
    ui.button("Stop", on_click=scanner.stop_scanning)

ui.run()
```

Then run: `python scanner_app.py`

**Note**: The ZXing JavaScript library is automatically bundled with the package - no additional setup required!

### Features

- **Easy Integration**: Drop-in component for NiceGUI apps
- **Camera Selection**: Automatic camera detection with settings UI
- **Flexible Styling**: Use standard CSS via `.style()` method
- **Multiple Formats**: Supports QR codes, barcodes, and more via ZXing
- **Page Context**: Works in both `ui.run()` and `@ui.page()` contexts

### Examples

See the `examples/` directory for:
- `app.py` - Multiple scanner configurations
- `page_example.py` - Usage with NiceGUI pages

## Development

To develop this component, install dependencies and run the hello world app:

```bash
npm install  # Install ZXing library
uv sync      # Install Python dependencies
make dev     # Run example app
```

This will start the example app on <http://localhost:3001> with multiple scanner demos.

## Questions

- How to bundle node module with NiceGUI elements?
- What is the nicegui way of handling errors from vue components?

[ZXing library]: https://www.npmjs.com/package/@zxing/library
[NiceGUI]: https://nicegui.io/
[custom vue component example]: https://github.com/zauberzeug/nicegui/tree/main/examples/custom_vue_component
