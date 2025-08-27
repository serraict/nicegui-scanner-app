# NiceGUI barcode scanner app

This project demonstrates how to create a barcode scanner using the [ZXing library] wrapped in a [NiceGUI] custom Vue component.
Based on [this discussion](https://github.com/zauberzeug/nicegui/discussions/5016),
and inspired by the [custom vue component example].

## Development

Install dependencies and run the hello world app:

```bash
npm install
uv sync
uv run src/nicegui_scanner/app.py
```

This will start the NiceGUI app on <http://localhost:3001>

## Questions

- How to bundle node module with NiceGUI elements?
- What is the nicegui way of handling errors from vue components?

[ZXing library]: https://www.npmjs.com/package/@zxing/library
[NiceGUI]: https://nicegui.io/
[custom vue component example]: https://github.com/zauberzeug/nicegui/tree/main/examples/custom_vue_component
