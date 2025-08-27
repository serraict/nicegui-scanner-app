"""NiceGUI barcode scanner component."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version(__name__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"  # Fallback for development mode

from .scanner import BarcodeScanner

__all__ = ["BarcodeScanner", "__version__"]
