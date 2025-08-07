from nicegui import ui, app
from scanner import BarcodeScanner

# Serve node_modules for the ZXing library
app.add_static_files('/node_modules', 'node_modules')

ui.label("Barcode Scanner Demo")

BarcodeScanner()

ui.run(port=3001)
