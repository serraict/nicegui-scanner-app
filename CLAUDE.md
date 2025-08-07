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
- Manual verification is our primary testing approach
- Focus on delivering value over perfect code

## Architecture

We follow the pattern from NiceGUI's custom vue component example, which is included in the examples directory for reference.

### Custom Vue Component Pattern

The project follows NiceGUI's custom Vue component pattern with two implementation approaches:

1. **JavaScript Components** (`counter.js` + `counter.py`)
   - Frontend: Pure JavaScript Vue component definition
   - Backend: Python Element subclass with `component='counter.js'`

2. **Vue SFC Components** (`on_off.vue` + `on_off.py`)
   - Frontend: Single-File Component with template, script, and style sections
   - Backend: Python Element subclass with `component='on_off.vue'`

### Component Structure

- Python classes extend `nicegui.element.Element`
- Frontend components emit 'change' events to communicate with Python backend
- Backend methods can be called from frontend using `run_method()`
- Props are passed from Python to Vue components via `self._props`

### Development Notes

- Browser cache must be disabled when making changes to `.js` files
- Use `uvicorn_reload_includes='*.py,*.js,*.vue'` for auto-reload during development
- Components communicate bidirectionally: Python→Vue via props, Vue→Python via events
