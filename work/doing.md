# Doing

**Goal:** Add error handling

Handle camera permissions gracefully and show user-friendly error messages for various failure scenarios.

## Design

### Error Scenarios & NiceGUI Integration Strategy

**Focus: Wrap JavaScript errors into NiceGUI element patterns**

**1. Initialization Errors (Constructor-time)**
- **ZXing Library Loading**: Script fails to load → Component shows loading error state
- **Browser Compatibility**: Missing `getUserMedia` → Component shows compatibility warning
- **Strategy**: Handle in Vue `mounted()`, emit 'error' event to Python with error type

**2. Runtime Camera Errors (Method-call time)**  
- **Permission Denied** (`NotAllowedError`): User blocks camera access
- **Hardware Unavailable** (`NotFoundError`): No camera detected  
- **Hardware Busy** (`NotReadableError`): Camera in use by another app
- **Strategy**: Catch in `initCamera()`, emit specific error events to Python

**3. ZXing Scanning Errors (Continuous operation)**
- **NotFoundException**: No barcode detected (normal, don't treat as error)
- **ReaderException**: Barcode format/checksum issues (log but continue)
- **Strategy**: ZXing already handles these gracefully in callback - minimal intervention needed

### Minimal Error Handling Strategy

**Principle: Only catch errors where user action is needed**

**Vue Component (Minimal Intervention):**
- Use Vue's global error handler for unexpected errors
- Only catch specific errors that require user feedback:
  - Camera permission denied → Show permission prompt UI
  - Camera hardware unavailable → Show "no camera" message
- Let other errors (ZXing loading, scanning failures) bubble naturally
- Emit targeted error events only for user-actionable scenarios

**Python Element (Error Integration):**
- Register error handler for user-actionable errors: `self.on('camera_error', handler)`
- Use `ui.notify()` for immediate feedback on critical errors
- Expose error state properties for application-level handling
- Maintain element stability (errors don't crash the element)

**Error Flow:**
1. **Library/Technical errors** → Browser console + Python logging (no user UI)
2. **User-actionable errors** → Vue UI state + Python notification
3. **Application-level errors** → Python business logic handling

**Benefits:**
- Clean Vue component without scattered try-catch blocks
- Focused error handling where users can actually do something
- Technical errors handled by normal browser/Python debugging tools
- User experience focused on actionable feedback

### Testing Strategy

**1. Camera Permission Denied (`NotAllowedError`)**
- **How to test**: 
  - Open browser dev tools → Settings → Privacy → Camera: Block
  - Or click "Block" when browser prompts for camera permission
  - Or use Chrome's camera icon in address bar → Block camera
- **Expected**: App shows permission prompt UI, emits camera_error event

**2. No Camera Hardware (`NotFoundError`)**
- **How to test**:
  - Use a desktop/laptop without camera hardware
  - Or disable camera in Device Manager (Windows) / System Preferences (Mac)
  - Or use Chrome dev tools → Settings → Camera: "No camera"
- **Expected**: App shows "no camera detected" message, emits camera_error event

**3. Camera Busy/In Use (`NotReadableError`)**
- **How to test**:
  - Open another app that uses camera (Zoom, Skype, Photo Booth)
  - Keep that app running while starting our scanner
  - Or open multiple tabs with our scanner app
- **Expected**: App shows "camera busy" message with retry option

**4. ZXing Library Loading Failure**
- **How to test**:
  - Block the script in browser: Dev Tools → Network → Block `/node_modules/@zxing/library/umd/index.min.js`
  - Or temporarily rename the ZXing file to break the path
  - Or use browser with JavaScript disabled
- **Expected**: Error logged to console, scanner shows generic error state

**5. Browser Compatibility Issues**
- **How to test**:
  - Use very old browser without `getUserMedia` support
  - Or simulate with: `delete navigator.mediaDevices` in console before loading
- **Expected**: App shows compatibility warning, graceful degradation

## Acceptance Criteria

- [ ] Camera permissions handled gracefully (denied/unavailable)
- [ ] User-friendly error messages for common failure scenarios
- [ ] App remains functional when errors occur (no crashes)
- [ ] Error states clearly communicated to users
- [ ] *Result: Working app that handles edge cases*

## Tasks

- [x] Identify error scenarios and design minimal handling strategy
- [ ] Add camera permission error handling to Vue component
- [ ] Add camera hardware error handling to Vue component  
- [ ] Create error UI states for user-actionable scenarios
- [ ] Add Python-side camera error event handling
- [ ] Test camera permission and hardware error scenarios
- [ ] Update documentation with minimal error handling patterns
