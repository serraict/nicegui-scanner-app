from nicegui import ui, app
from scanner import BarcodeScanner

# Serve node_modules for potential future JS dependencies
app.add_static_files("/node_modules", "node_modules")


def on_scan(event):
    """Handle barcode scan results."""
    barcode_text = event.args
    print(f"Scanned barcode: {barcode_text}")
    ui.notify(f"Scanned: {barcode_text}")


ui.label("Barcode Scanner Demo")

# Scanner component
BarcodeScanner(on_scan=on_scan)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=3001)
