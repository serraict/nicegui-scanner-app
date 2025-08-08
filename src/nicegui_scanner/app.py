from nicegui import ui, app
from scanner import BarcodeScanner

# Serve node_modules for potential future JS dependencies
app.add_static_files("/node_modules", "node_modules")


def on_scan(event):
    """Handle barcode scan results."""
    barcode_text = event.args
    print(f"Scanned barcode: {barcode_text}")
    ui.notify(f"Scanned: {barcode_text}")


# Scanner component
scanner = BarcodeScanner(on_scan=on_scan)

# Control buttons
with ui.row():

    def toggle_scanning():
        if scanner.is_scanning():
            scanner.stop_scanning()
            scan_toggle.props("icon=play_arrow color=primary")
            scan_toggle.text = "Start Scanning"
        else:
            scanner.start_scanning()
            scan_toggle.props("icon=stop color=negative")
            scan_toggle.text = "Stop Scanning"

    def on_scanning_failed(event):
        """Handle when scanning fails to start."""
        # Reset button to start state when scanning fails
        scan_toggle.props("icon=play_arrow color=primary")
        scan_toggle.text = "Start Scanning"

    scan_toggle = ui.button(
        "Start Scanning",
        icon="play_arrow",
        color="primary",
        on_click=toggle_scanning
    )

    # Set up scanning failed handler after button is created
    scanner.on("scanning_failed", on_scanning_failed)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=3001)
