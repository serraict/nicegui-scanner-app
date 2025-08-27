#!/usr/bin/env python3
"""Test NiceGUI scanner in page context (not just ui.run())."""

from nicegui import ui, app
from nicegui_scanner import BarcodeScanner

# Serve node_modules for ZXing library
app.add_static_files("/node_modules", "../node_modules")


@ui.page('/')
def main_page():
    """Main page using NiceGUI page decorator."""
    ui.html("<h1>NiceGUI Scanner - Page Context Test</h1>")
    
    def on_scan(event):
        """Handle barcode scan results."""
        barcode_text = event.args
        print(f"Scanned barcode in page context: {barcode_text}")
        ui.notify(f"Page Context - Scanned: {barcode_text}")
    
    # Test scanner in page context
    ui.html("<h3>Scanner in Page Context</h3>")
    scanner = BarcodeScanner(on_scan=on_scan).style("width: 400px; height: 300px;")
    
    with ui.row().classes("gap-4 mt-4"):
        ui.button("Start Scanner", 
                 on_click=lambda: scanner.start_scanning()).props("color=primary")
        ui.button("Stop Scanner", 
                 on_click=lambda: scanner.stop_scanning()).props("color=secondary")
        ui.button("Settings", 
                 on_click=lambda: scanner.run_method("toggleSettings")).props("icon=settings")


@ui.page('/multiple')  
def multiple_page():
    """Test multiple scanners in page context."""
    ui.html("<h1>Multiple Scanners - Page Context</h1>")
    
    def on_scan_1(event):
        ui.notify(f"Scanner 1: {event.args}", type="positive")
        
    def on_scan_2(event):  
        ui.notify(f"Scanner 2: {event.args}", type="info")
    
    ui.html("<h3>Scanner 1</h3>")
    scanner1 = BarcodeScanner(on_scan=on_scan_1).style("width: 300px; height: 200px;")
    
    ui.html("<h3>Scanner 2</h3>") 
    scanner2 = BarcodeScanner(on_scan=on_scan_2).style("width: 500px; height: 300px;")
    
    with ui.row():
        ui.button("Start Both", on_click=lambda: [scanner1.start_scanning(), scanner2.start_scanning()])
        ui.button("Stop Both", on_click=lambda: [scanner1.stop_scanning(), scanner2.stop_scanning()])


if __name__ in {"__main__", "__mp_main__"}:
    # Add navigation
    ui.link("Single Scanner", "/")
    ui.link("Multiple Scanners", "/multiple") 
    ui.run(port=3002)