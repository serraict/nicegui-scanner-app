from nicegui.element import Element


class BarcodeScanner(Element, component="barcode_scanner.vue"):

    def __init__(self) -> None:
        super().__init__()
