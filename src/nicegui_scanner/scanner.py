from typing import Any, Callable, Optional
from nicegui.element import Element


class BarcodeScanner(Element, component="barcode_scanner.vue"):

    def __init__(self, *, on_scan: Optional[Callable] = None, **kwargs: Any) -> None:
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

    def _handle_scanning_failed(self, event) -> None:
        """Handle when Vue component fails to start scanning."""
        self._scanning = False
