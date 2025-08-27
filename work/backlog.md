# Backlog

## Incremental Working Examples

- **Add configuration**
  - Select barcode formats to scan (QR, Code128, etc.)
  - Use `self._props` pattern for passing config to Vue (e.g. viewport settings, video with and height)
  - *Result: Working app with customizable barcode format scanning*

- **Create PyPi package**
  - Design code api in a NiceGUI example app and in  a NiceGUI `page`.
  - add a makefile with a script to create a package
  - *Result: pip install into a new NiceGUI project allows us to simply add a scanner component to a NiceGUI project.*

- **Add manual trigger**
  - Single "Scan Once" button for one-time scans
  - Manual barcode detection without continuous scanning
  - *Result: Working app with on-demand scanning capability*
