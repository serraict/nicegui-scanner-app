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
    };
  },

  async mounted() {
    await this.loadZXing();
    await this.startCamera();
  },

  beforeUnmount() {
    if (this.codeReader) {
      this.codeReader.reset();
    }
  },

  methods: {
    async loadZXing() {
      // Load ZXing library via script tag
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

    async startCamera() {
      try {
        // Initialize ZXing barcode reader
        this.codeReader = new window.ZXing.BrowserMultiFormatReader();
        
        // Start camera and barcode detection
        this.codeReader.decodeFromVideoDevice(undefined, this.$refs.scanner, (result, err) => {
          if (result) {
            console.log('Barcode detected:', result.text);
            // Emit event to Python backend
            this.$emit('scan', result.text);
          }
        });
      } catch (error) {
        console.log("Scanner error:", error);
      }
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
}

</style>