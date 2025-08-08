# Error Handling Tests

This document specifies manual tests to verify error handling functionality. Execute these tests after any changes to error handling code.

## Test Environment Setup

- Use Chrome browser (easiest camera permission controls)
- Run app with `python src/nicegui_scanner/app.py`
- Open browser dev tools console to observe error messages

## Test 1: Camera Permission Denied

**Setup:**
1. Block camera access: Chrome address bar → Camera icon → "Block camera access"
2. Refresh the page

**Test Steps:**
1. Observe initial state: Button should show "Start Scanning" (blue)
2. Click "Start Scanning" button

**Expected Results:**
- ✅ Console shows: "Camera error: NotAllowedError: Permission denied"
- ✅ Button briefly turns red, then immediately back to blue "Start Scanning"
- ✅ NO uncaught promise errors in console
- ✅ Button remains clickable for retry

**Failure Indicators:**
- ❌ Uncaught promise errors in console
- ❌ Button stays red/shows "Stop Scanning"
- ❌ Button becomes unresponsive

## Test 2: Normal Camera Access (Baseline)

**Setup:**
1. Allow camera access: Chrome address bar → Camera icon → "Always allow camera"
2. Refresh the page

**Test Steps:**
1. Click "Start Scanning" button
2. Click "Stop Scanning" button

**Expected Results:**
- ✅ Button changes from "Start Scanning" (blue) → "Stop Scanning" (red)
- ✅ Video feed appears in scanner area
- ✅ Button changes from "Stop Scanning" (red) → "Start Scanning" (blue)
- ✅ Video feed stops
- ✅ No errors in console

**Failure Indicators:**
- ❌ Button doesn't change state properly
- ❌ Video feed doesn't appear/disappear
- ❌ Console errors during normal operation

## Test 3: No Camera Hardware

**Setup:**
1. Simulate no camera hardware:
   - **Method A**: Chrome Dev Tools → Settings (gear icon) → Devices → Camera: "No camera"
   - **Method B**: Physically disconnect camera (if external USB camera)
   - **Method C**: Use computer without built-in camera
2. Refresh the page

**Test Steps:**
1. Observe initial state: Button should show "Start Scanning" (blue)
2. Click "Start Scanning" button

**Expected Results:**
- ✅ Console shows: "Camera error: NotFoundError: [message]"
- ✅ Button briefly turns red, then immediately back to blue "Start Scanning"
- ✅ NO uncaught promise errors in console
- ✅ Button remains clickable for retry

**Failure Indicators:**
- ❌ Uncaught promise errors in console
- ❌ Button stays red/shows "Stop Scanning"
- ❌ Different error message than expected

## Test 4: Camera Busy/In Use

**Setup:**
1. Try to create camera conflict:
   - **Method A**: Open multiple tabs of our scanner app, start scanning in first tab, then try second tab
   - **Method B**: Open OBS Studio or other streaming software with camera source
   - **Method C**: Open video conferencing app with exclusive camera access
   - **Method D**: If available, use external USB camera and physically disconnect/reconnect during use
2. **Note**: Some systems allow camera sharing, so this error might not occur on all setups

**Test Steps:**
1. Observe initial state: Button should show "Start Scanning" (blue)
2. Click "Start Scanning" button

**Expected Results:**
- ✅ **IF camera conflict occurs**: Console shows "Camera error: NotReadableError: [message]"
- ✅ **IF camera sharing works**: Normal operation (video appears, scanning works)
- ✅ NO uncaught promise errors in either case
- ✅ Button behavior matches the actual result (red if working, blue if failed)

**Failure Indicators:**
- ❌ Uncaught promise errors in console
- ❌ Button state doesn't match actual camera state

**Note:** This test may pass differently on different systems due to camera sharing capabilities.

## Test 5: Permission Denied → Allow → Normal Operation

**Setup:**
1. Start with camera blocked (Test 1 setup)

**Test Steps:**
1. Click "Start Scanning" (should fail as in Test 1)
2. Allow camera access: Chrome camera icon → "Always allow camera"
3. Click "Start Scanning" again
4. Click "Stop Scanning"

**Expected Results:**
- ✅ First click fails gracefully (as Test 1)
- ✅ Second click succeeds (video appears, button goes red)
- ✅ Stop works normally
- ✅ No persistent errors from previous failure

**Failure Indicators:**
- ❌ Second attempt doesn't work after allowing camera
- ❌ Errors persist from previous failed attempt

## Test Status

- [ ] Test 1: Camera Permission Denied
- [ ] Test 2: Normal Camera Access  
- [ ] Test 3: No Camera Hardware
- [ ] Test 4: Camera Busy/In Use
- [ ] Test 5: Permission Denied → Allow → Normal Operation

## Notes

- Tests should be run in order
- All tests should pass before committing error handling changes
- Console should be clear of uncaught promise errors after each test