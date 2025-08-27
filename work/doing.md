# Doing

## Add Configuration Support

**Goal**: Enable configuration of scanner properties using the `self._props` pattern for passing settings to Vue component.

**Current State**: 
- Scanner only accepts `on_scan` callback parameter
- Vue component has hardcoded video dimensions and viewport settings
- No way to customize scanner behavior from Python side

**Tasks**:
1. **Python API Enhancement**
   - Add configuration parameters to `BarcodeScanner.__init__()` 
   - Use `self._props` pattern to pass config to Vue component
   - Support video width/height, viewport settings, scanning behavior

2. **Vue Component Updates**
   - Accept configuration props from Python side
   - Make video dimensions configurable via props
   - Add viewport/display customization options
   - Update component to use prop values instead of hardcoded settings

3. **Integration & Testing**
   - Update example app to demonstrate configuration options
   - Test with different size and viewport combinations
   - Verify props are correctly passed from Python to Vue

**Success Criteria**:
- `BarcodeScanner(width=500, height=400)` sets custom video dimensions
- Configuration is passed through `self._props` to Vue component
- Manual browser testing confirms visual changes work correctly

**Result**: Working app with customizable scanner configuration
