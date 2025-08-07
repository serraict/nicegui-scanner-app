# NiceGUI barcode scanner app

This project shows how to wrap the [vue-barcode-scanner] component into a [NiceGUI] ui element.
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

## Project Structure

```
├── src/nicegui_scanner/    # Main application code
├── examples/               # Reference examples (from NiceGUI)
├── work/                   # Project management files
│   ├── backlog.md          # Product backlog
│   └── doing.md            # Current work
├── pyproject.toml          # Project configuration
└── CLAUDE.md               # AI assistant guidance
```

[vue-barcode-scanner]: https://www.npmjs.com/package/vue-barcode-reader
[NiceGUI]: https://nicegui.io/
[custom vue component example]: https://github.com/zauberzeug/nicegui/tree/main/examples/custom_vue_component
