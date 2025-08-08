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

    def toggle_settings():
        """Toggle camera settings if multiple cameras available."""
        scanner.run_method("toggleSettings")

    def on_scanning_failed(event):
        """Handle when scanning fails to start."""
        # Reset button to start state when scanning fails
        scan_toggle.props("icon=play_arrow color=primary")
        scan_toggle.text = "Start Scanning"

    def on_camera_error(event):
        """Handle camera errors and show user notification."""
        error_messages = {
            "NotAllowedError": "Camera access denied. Please allow camera access and try again.",
            "NotFoundError": "No camera detected. Please connect a camera and try again.",
            "NotReadableError": "Camera is busy. Please close other camera apps and try again.",
        }
        error_type = event.args.get("type", "Unknown")
        message = error_messages.get(
            error_type, "Camera error occurred. Please check your camera and try again."
        )
        ui.notify(message, type="negative")

    scan_toggle = ui.button(
        "Start Scanning", icon="play_arrow", color="primary", on_click=toggle_scanning
    )

    settings_button = ui.button("", icon="settings", on_click=toggle_settings)

    # Set up event handlers after button is created
    scanner.on("scanning_failed", on_scanning_failed)
    scanner.on("camera_error", on_camera_error)

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(port=3001)
