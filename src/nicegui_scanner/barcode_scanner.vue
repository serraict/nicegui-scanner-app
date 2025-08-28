<template>
  <div class="scanner-container">
    <video ref="scanner" autoplay v-bind="$attrs"></video>
    
    <!-- Settings overlay -->
    <div v-if="showSettings" class="fixed-full bg-black-transparent flex flex-center">
      <div class="bg-white q-pa-md rounded-borders shadow-5" style="min-width: 250px;">
        <h6 class="q-ma-none q-mb-md">Camera Settings</h6>
        <div v-if="availableCameras.length > 1" class="q-mb-md">
          <q-select
            v-model="selectedCameraId"
            :options="cameraOptions"
            option-label="label"
            option-value="deviceId"
            @update:model-value="selectCamera"
            outlined
            label="Camera"
            emit-value
            map-options
          />
        </div>
        <q-btn 
          @click="showSettings = false" 
          color="primary" 
          class="full-width"
          label="Close"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "barcode-scanner",
  inheritAttrs: false,

  data() {
    return {
      codeReader: null,
      isScanning: false,
      availableCameras: [],
      selectedCameraId: null,
      showSettings: false,
    };
  },

  async mounted() {
    await this.loadZXing();
    await this.detectCameras();
  },

  beforeUnmount() {
    if (this.codeReader) {
      this.codeReader.reset();
    }
  },

  computed: {
    cameraOptions() {
      const options = [
        { label: 'Auto-select best camera', deviceId: null }
      ];
      
      this.availableCameras.forEach(camera => {
        options.push({
          label: camera.label || `Camera ${camera.deviceId.substring(0, 8)}...`,
          deviceId: camera.deviceId
        });
      });
      
      return options;
    }
  },

  methods: {
    async loadZXing() {
      // Dynamically loads ZXing barcode detection library
      // Uses UMD build to avoid ES module complexity
      return new Promise((resolve, reject) => {
        if (window.ZXing) {
          resolve();
          return;
        }

        const script = document.createElement('script');
        script.src = '/static/nicegui-scanner/zxing.min.js';
        script.onload = () => resolve();
        script.onerror = () => reject(new Error('Failed to load ZXing'));
        document.head.appendChild(script);
      });
    },

    async detectCameras() {
      try {
        // Create temporary codeReader to detect cameras
        const tempCodeReader = new window.ZXing.BrowserMultiFormatReader();
        this.availableCameras = await tempCodeReader.listVideoInputDevices();
        
        // Set default camera selection (ZXing will auto-select best if null)
        this.selectedCameraId = null;
      } catch (error) {
        this.availableCameras = [];
      }
    },

    async initCamera() {
      try {
        // Initialize ZXing barcode reader - it will handle camera access
        this.codeReader = new window.ZXing.BrowserMultiFormatReader();
      } catch (error) {
        this.codeReader = null;
        // Emit event to Python for user notification
        this.$emit('camera_error', { type: error.name, message: error.message });
      }
    },

    async startScanning() {
      if (this.isScanning) return;
      
      // Initialize camera and scanner if not done yet
      if (!this.codeReader) {
        await this.initCamera();
        // If camera initialization failed, don't proceed
        if (!this.codeReader) {
          // Emit event to inform Python that scanning failed to start
          this.$emit('scanning_failed');
          return;
        }
      }
      
      // Only set scanning state and start detection if camera is ready
      this.isScanning = true;
      // Start continuous barcode detection from video stream with selected camera
      // Callback fires whenever a barcode is detected
      this.codeReader.decodeFromVideoDevice(this.selectedCameraId, this.$refs.scanner, (result, err) => {
        if (result && this.isScanning) {
          // Send scan result to Python via NiceGUI event system
          this.$emit('scan', result.text);
        }
      });
    },

    stopScanning() {
      if (!this.isScanning) return;
      
      this.isScanning = false;
      if (this.codeReader) {
        this.codeReader.reset();
      }
    },

    selectCamera(cameraId) {
      this.selectedCameraId = cameraId;
      
      // If currently scanning, restart with new camera
      if (this.isScanning) {
        this.stopScanning();
        this.$nextTick(() => {
          this.startScanning();
        });
      }
    },

    toggleSettings() {
      // Always allow settings to be toggled
      this.showSettings = !this.showSettings;
    },

  },
};
</script>

<style scoped>
.scanner-container {
  position: relative;
  display: inline-block;
}

video {
  display: block;
  background-color: #f5f5f5;
  object-fit: cover;
  width: 400px;
  height: 300px;
}

.fixed-full {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
}

.bg-black-transparent {
  background: rgba(0, 0, 0, 0.5);
}
</style>