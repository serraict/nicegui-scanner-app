# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project demonstrates how to wrap the vue-barcode-scanner component into a NiceGUI UI element. It's based on the NiceGUI custom Vue component example and shows how to create custom Vue components in NiceGUI applications.

## Commands

Us `uv` for dependency management an project initialization.

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

## Architecture

We follow the pattern from NiceGUI's custom vue component example, which is included in the examples directory for reference.

### Custom Vue Component Pattern

We follow NiceGUI's custom Vue component pattern as shown in the examples directory:

**Our Implementation:**
- **Vue SFC Component** (`barcode_scanner.vue`)
  - Uses native browser APIs like `getUserMedia` for camera access
  - Minimal template with video element for camera feed
  - Component served from `src/nicegui_scanner/` directory

- **Python Element** (`scanner.py`)
  - `BarcodeScanner` class extends `nicegui.element.Element`
  - Specifies `component='barcode_scanner.vue'`
  - Minimal wrapper around Vue component

### Development Notes

- JavaScript dependencies managed via npm in project root
- Static files served via `app.add_static_files()` when needed
- Manual browser verification required for camera-based components
- Use `uvicorn_reload_includes='*.py,*.js,*.vue'` for auto-reload during development
