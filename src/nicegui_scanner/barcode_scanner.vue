<template>
  <div class="scanner-container">
    <video ref="scanner" autoplay></video>
    <div v-if="lastScan" class="scan-result">{{ lastScan }}</div>
  </div>
</template>

<script>
export default {
  name: "barcode-scanner",

  data() {
    return {
      codeReader: null,
      lastScan: null,
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
            this.lastScan = result.text;
            console.log('Barcode detected:', result.text);
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

.scan-result {
  position: absolute;
  bottom: 10px;
  left: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 5px 10px;
  border-radius: 3px;
  font-family: monospace;
  max-width: 90%;
  word-break: break-all;
}
</style>