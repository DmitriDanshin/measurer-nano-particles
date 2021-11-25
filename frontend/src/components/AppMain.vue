<template>
  <section v-if="true">
    <div class="flex justify-between bg-gray-800">
      <app-options @optionChanged="handleOptionsChange"/>
      <app-image :src="src"/>
      <app-information :info="info"/>
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
  methods: {
    handleOptionsChange(options) {
      this.$emit('handle-options-change', options);
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

</style>
