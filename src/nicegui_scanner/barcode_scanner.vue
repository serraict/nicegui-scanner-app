<template>
  <div class="scanner-container">
    <video ref="scanner" autoplay></video>
  </div>
</template>

<script>
export default {
  name: "barcode-scanner",

  data() {
    return {
      codeReader: null,
      isScanning: false,
    };
  },

  async mounted() {
    await this.loadZXing();
  },

  beforeUnmount() {
    if (this.codeReader) {
      this.codeReader.reset();
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
        script.src = '/node_modules/@zxing/library/umd/index.min.js';
        script.onload = () => resolve();
        script.onerror = () => reject(new Error('Failed to load ZXing'));
        document.head.appendChild(script);
      });
    },

    async initCamera() {
      try {
        // Request camera access first - this is where permission errors occur
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.$refs.scanner.srcObject = stream;
        
        // Only initialize ZXing barcode reader after successful camera access
        this.codeReader = new window.ZXing.BrowserMultiFormatReader();
      } catch (error) {
        this.handleCameraError(error);
        // Ensure codeReader stays null on camera error
        this.codeReader = null;
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
      // Start continuous barcode detection from video stream
      // Callback fires whenever a barcode is detected
      this.codeReader.decodeFromVideoDevice(undefined, this.$refs.scanner, (result, err) => {
        if (result && this.isScanning) {
          console.log('Barcode detected:', result.text);
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

    handleCameraError(error) {
      console.log('Camera error:', error.name, error.message);
    },

  },
};
</script>

<style scoped>
.scanner-container {
  position: relative;
}

video {
  width: 100%;
  max-width: 400px;
  height: 300px;
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 4px;
}

</style>