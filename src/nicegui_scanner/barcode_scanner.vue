<template>
  <div class="scanner-container">
    <video ref="scanner" autoplay></video>
  </div>
</template>

<script>
export default {
  name: "barcode-scanner",

  async mounted() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      this.$refs.scanner.srcObject = stream;
    } catch (error) {
      console.log("Camera error:", error);
    }
  },
};
</script>

<style scoped>
video {
  width: 100%;
  max-width: 400px;
}
</style>