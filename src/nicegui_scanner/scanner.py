from typing import Any, Callable, Optional
from nicegui.element import Element
from nicegui import app, ui
import importlib.resources


class BarcodeScanner(Element, component="barcode_scanner.vue"):
    _static_files_configured = False

    def __init__(self, *, on_scan: Optional[Callable] = None, **kwargs: Any) -> None:
        # Configure static files once
        if not BarcodeScanner._static_files_configured:
            self._configure_static_files()
            BarcodeScanner._static_files_configured = True

        # Pass all unhandled kwargs to the base Element class
        super().__init__(**kwargs)

        # Set up event handlers
        if on_scan:
            self.on("scan", on_scan)
        self.on("scanning_failed", self._handle_scanning_failed)

        # Set internal state
        self._scanning = False

    def start_scanning(self) -> None:
        """Start continuous barcode scanning."""
        self._scanning = True
        self.run_method("startScanning")

    def stop_scanning(self) -> None:
        """Stop continuous barcode scanning."""
        self._scanning = False
        self.run_method("stopScanning")

    def is_scanning(self) -> bool:
        """Check if scanner is currently in scanning mode."""
        return self._scanning

    def create_control_buttons(self) -> None:
        """Create a button group with start, stop, and settings controls."""
        with ui.button_group():
            ui.button("", icon="qr_code_scanner", on_click=self.start_scanning).tooltip(
                "Start scanning"
            )
            ui.button("", icon="stop", on_click=self.stop_scanning).tooltip(
                "Stop scanning"
            )
            ui.button(
                "", icon="settings", on_click=lambda: self.run_method("toggleSettings")
            ).tooltip("Settings")

    def _configure_static_files(self) -> None:
        """Configure static file serving for ZXing library."""
        try:
            # Get the path to our package's static files
            if hasattr(importlib.resources, "files"):  # Python 3.9+
                static_path = importlib.resources.files("nicegui_scanner") / "static"
            else:  # Python 3.8
                with importlib.resources.path("nicegui_scanner", "static") as p:
                    static_path = p

            # Add static file serving
            app.add_static_files("/static/nicegui-scanner", static_path)
        except Exception as e:
            print(f"Warning: Could not configure static files for nicegui-scanner: {e}")

    def _handle_scanning_failed(self, event) -> None:
        """Handle when Vue component fails to start scanning."""
        self._scanning = False
