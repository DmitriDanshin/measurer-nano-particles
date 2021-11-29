<template>
  <section v-if="true">
    <div class="flex justify-between bg-gray-800">
      <app-options
          :class="{disabled: imageFullSize}"
          @optionChanged="handleOptionsChange"
      />
      <app-image
          :src="src"
          :contours="info.contours"
          @newContourSettings="handleNewContourSettings"
          @toggleImageFullSize="toggleImageFullSize"
      />
      <app-information
          :class="{disabled: imageFullSize}"
          :info="info"
      />
    </div>
  </section>
</template>

<script>
import AppImage from "./AppImage";
import AppOptions from "./AppOptions";
import AppInformation from "./AppInformation";

export default {
  components: {AppImage, AppOptions, AppInformation},
  name: "AppMain",
  data() {
    return {
      imageFullSize: false
    }
  },
  methods: {
    toggleImageFullSize(imageFullSize) {
      this.imageFullSize = imageFullSize
    },
    handleOptionsChange(options) {
      this.$emit('handle-options-change', options);
    },
    handleNewContourSettings(contours) {
      this.$emit("new-contour-settings", contours);
    }
  },
  props: {
    src: {
      type: String,
      required: true
    },
    info: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
.disabled {
  display: none;
}
</style>
