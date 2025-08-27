# Doing

## Create PyPi Package

**Goal**: Make the barcode scanner available as an installable Python package so users can easily add it to their NiceGUI projects.

**Current State**:

- Scanner works well as a local component
- Code is organized in `src/nicegui_scanner/` directory
- Has Vue component, Python element, and example app
- Missing package configuration and distribution setup

**Tasks**:

1. **Package Structure Setup** ✅ COMPLETED
   - ✅ Create proper `pyproject.toml` with package metadata
   - ✅ Ensure `src/nicegui_scanner/` structure is pip-installable
   - ✅ Add `__init__.py` exports for clean API

2. **Create Distribution Build** ✅ COMPLETED
   - ✅ Add Makefile with build, package, and publish commands
   - ✅ Add github action for ci build and for publish on release
   - ✅ Use dynamic versioning with uv
   - ✅ Test local installation with `uv pip install -e .`
   - ✅ Example app placed outside src dir and references editable package
   - ✅ Verify package works (tested with examples/app.py)

3. **API Design & Testing** ✅ COMPLETED  
   - ✅ Design clean import API: `from nicegui_scanner import BarcodeScanner`
   - ✅ Test in example app using installed package
   - ✅ Test in NiceGUI `page` context (not just `ui.run()`)

**Success Criteria**:

- ✅ `uv pip install -e .` installs the package (editable mode tested)
- ✅ `from nicegui_scanner import BarcodeScanner` works
- ✅ Scanner component works in both app and page contexts (both tested)
- ✅ Makefile automates build and publish process
- ✅ Dynamic versioning works (v0.1.0 tag → nicegui_scanner-0.1.0 package)
- ✅ Package builds successfully (`make build` creates wheel and source dist)
- ✅ The package is uploaded to PyPi in the publish step (GitHub Actions configured)
- ⏳ Github actions builds package for every push to main
- ⏳ Github actions build package and pushes to PyPi for all version tags (`v0.4.1`) that are pushed to github

**Completed Implementation**:

- ✅ GitHub Actions CI/CD pipeline (`.github/workflows/ci.yml` & `release.yml`)
- ✅ Testing in NiceGUI `page` context (`examples/page_example.py`)

**Result**: ⏳ waiting on succesfull builds and PyPi publish
