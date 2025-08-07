from typing import Callable, Optional
from nicegui.element import Element


class BarcodeScanner(Element, component="barcode_scanner.vue"):

    def __init__(self, *, on_scan: Optional[Callable] = None) -> None:
        super().__init__()
        self.on("scan", on_scan)
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
