from nicegui import ui, app
from nicegui_scanner import BarcodeScanner

# Serve node_modules for potential future JS dependencies
app.add_static_files("/node_modules", "../node_modules")


def on_scan(event):
    """Handle barcode scan results."""
    barcode_text = event.args
    print(f"Scanned barcode: {barcode_text}")
    ui.notify(f"Scanned: {barcode_text}")


# Example 1: Basic scanner with minimal styling
scanner_basic = BarcodeScanner(on_scan=on_scan)
scanner_basic.create_control_buttons()

# Example 2: Large scanner - twice the default width
scanner_large = BarcodeScanner(on_scan=on_scan).style("width: 800px; height: 300px;")
with ui.button_group():
    ui.button("Start", on_click=lambda: scanner_large.start_scanning())
    ui.button("Stop", on_click=lambda: scanner_large.stop_scanning())

# Example 3: Wild styled scanner with colors and effects
ui.html("<h3>3. Stylish Scanner</h3>")
scanner_wild = (
    BarcodeScanner(on_scan=on_scan)
    .style(
        """
    width: 600px;
    height: 250px;
    border: 4px solid #ff6b35;
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(255, 107, 53, 0.3);
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 15px;
    transform: rotate(-1deg);
    transition: all 0.3s ease;
"""
    )
    .classes("hover:scale-105 cursor-pointer")
)

with ui.row().classes():
    ui.button("Start Stylish", on_click=lambda: scanner_wild.start_scanning())
    ui.button(
        "Stop All",
        on_click=lambda: [
            s.stop_scanning() for s in [scanner_basic, scanner_large, scanner_wild]
        ],
    ).props("color=red")

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=3001)
