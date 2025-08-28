#!/usr/bin/env python3
"""Test NiceGUI scanner in page context (not just ui.run())."""

from nicegui import ui, app
from nicegui_scanner import BarcodeScanner

# Serve node_modules for ZXing library
app.add_static_files("/node_modules", "../node_modules")


@ui.page("/single")
def single_page():

    def on_scan(event):
        barcode_text = event.args
        ui.notify(f"Page Context - Scanned: {barcode_text}")

    scanner = BarcodeScanner(on_scan=on_scan).style("width: 400px; height: 300px;")
    scanner.create_control_buttons()


@ui.page("/multiple")
def multiple_page():

    ui.markdown(
        """
        > Running multiple scanners on a single page does not work really well.
        >
        > During testing I found that after switching cameras on and off,
        > a camera might stop scanning and I have not found the cause of this yet.
        """
    )

    def on_scan_1(event):
        ui.notify(f"Scanner 1: {event.args}", type="positive")

    def on_scan_2(event):
        ui.notify(f"Scanner 2: {event.args}", type="info")

    scanner1 = BarcodeScanner(on_scan=on_scan_1).style("width: 300px; height: 200px;")
    scanner1.create_control_buttons()

    scanner2 = BarcodeScanner(on_scan=on_scan_2).style("width: 500px; height: 300px;")
    scanner2.create_control_buttons()


if __name__ in {"__main__", "__mp_main__"}:
    ui.link("Single Scanner", "/single")
    ui.link("Multiple Scanners", "/multiple")
    ui.run(port=3002)
