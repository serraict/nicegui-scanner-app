# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project demonstrates how to create a barcode scanner using ZXing library wrapped in a NiceGUI UI element.
It's based on the NiceGUI custom Vue component pattern and shows how to create custom Vue components in NiceGUI applications.

## Commands

Use `uv` for dependency management an project initialization.

Use `uv run ...` for running Python scripts and programs in the virtual environment.

## Workflow

Our development workflow follows an incremental approach:

1. **Vision** - Project goals described in `readme.md`
2. **Planning** - Work planned in `./work/backlog.md` (incremental working examples)
3. **Execution** - Current work tracked in `./work/doing.md`
4. **Quality** - Definition of Done in `./work/definition-of-done.md`
5. **Reflection** - After completing doing.md, reflect on process and adapt if needed
6. **Transition** - Clear doing.md and pull next item from backlog

**Key principles:**

- Each increment results in a working, runnable application
- Commit work regularly
- Manual verification is our primary testing approach - this means actually testing in a browser, not just checking that commands run without errors
- Focus on delivering value over perfect code
- We want to maintain as little code as possible

## Architecture

We follow the pattern from NiceGUI's custom Vue component example.

### Custom Vue Component Pattern

We follow NiceGUI's custom Vue component pattern:

**Our Implementation:**

- **Vue SFC Component** (`barcode_scanner.vue`)
  - Uses native browser APIs like `getUserMedia` for camera access
  - Integrates ZXing library via UMD build for barcode detection
  - Dynamic script loading: `/node_modules/@zxing/library/umd/index.min.js`
  - Visual overlay feedback showing detected barcode results
  - Component served from `src/nicegui_scanner/` directory

- **Python Element** (`scanner.py`)
  - `BarcodeScanner` class extends `nicegui.element.Element`
  - Specifies `component='barcode_scanner.vue'`
  - Accepts `on_scan` callback for handling Vue events
  - Uses `self.on('scan', callback)` to register event handlers

### Vue↔Python Communication

**Event Pattern:**

- **Vue**: `this.$emit('eventName', data)` - emits events with data
- **Python**: `self.on('eventName', callback)` - registers event handlers
- **Important**: Events come wrapped in `GenericEventArguments` - extract data via `event.args`

**Method Calling Pattern:**

- **Python**: `scanner.run_method("toggleSettings")` - calls Vue component methods from Python
- **Vue**: Define methods that can be called externally (e.g., `toggleSettings()`)

### Development Notes

- JavaScript dependencies managed via npm in project root
- **ZXing Integration**: Uses `@zxing/library` UMD build to avoid ES module complexity
- Static files served via `app.add_static_files()` when needed
- Manual browser verification required for camera-based components
- Use `uvicorn_reload_includes='*.py,*.js,*.vue'` for auto-reload during development
- **Import pattern**: Use relative imports (`from scanner import`) when running app.py directly
