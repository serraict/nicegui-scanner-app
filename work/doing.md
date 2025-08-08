# Doing

**Goal:** Add error handling

Handle camera permissions gracefully and show user-friendly error messages for various failure scenarios.

## Design

### Error Scenarios & Handling Strategy

**1. ZXing Library Loading Failure**
- Error: Script fails to load from `/node_modules/@zxing/library/umd/index.min.js`
- Handling: Show error message "Barcode scanner unavailable", disable scanner component
- UI State: Show error message instead of video element

**2. Camera Permission Denied**
- Error: `getUserMedia()` throws `NotAllowedError`
- Handling: Show "Camera access required" message with instructions to enable
- UI State: Show permission prompt/instructions, keep scanner controls disabled

**3. No Camera Available**
- Error: `getUserMedia()` throws `NotFoundError`
- Handling: Show "No camera detected" message
- UI State: Inform user no camera found, disable scanner

**4. Camera Already in Use**
- Error: `getUserMedia()` throws `NotReadableError`
- Handling: Show "Camera busy" message, suggest closing other apps
- UI State: Temporary error with retry option

### Error Communication Pattern

**Vue Component:**
- Track error state in component data (`errorState: null | 'library' | 'permission' | 'hardware'`)
- Show error UI conditionally instead of video element
- Emit error events to Python side for logging/notifications

**Python Integration:**
- Listen for error events from Vue component
- Show `ui.notify()` messages for immediate feedback
- Maintain app functionality (other features still work)

**User Experience:**
- Clear, actionable error messages (not technical jargon)
- Graceful degradation (app doesn't crash)
- Visual feedback in the scanner area
- Option to retry when appropriate

## Acceptance Criteria

- [ ] Camera permissions handled gracefully (denied/unavailable)
- [ ] User-friendly error messages for common failure scenarios
- [ ] App remains functional when errors occur (no crashes)
- [ ] Error states clearly communicated to users
- [ ] *Result: Working app that handles edge cases*

## Tasks

- [ ] Identify error scenarios (camera denied, no camera, ZXing load failure)
- [ ] Add error handling to Vue component camera initialization
- [ ] Add error handling to ZXing library loading
- [ ] Create user-friendly error messages and UI states
- [ ] Add Python-side error handling for scan events
- [ ] Test error scenarios manually
- [ ] Update documentation with error handling patterns
