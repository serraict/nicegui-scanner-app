from typing import Callable, Optional
from nicegui.element import Element


class BarcodeScanner(Element, component="barcode_scanner.vue"):

    def __init__(self, *, on_scan: Optional[Callable] = None) -> None:
        super().__init__()
        self.on('scan', on_scan)
