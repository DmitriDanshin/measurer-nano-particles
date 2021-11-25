<template>
  <div class="px-auto pt-32  content-center">
    <img
        :src="src"
        class="mx-auto w-2/3 h-2/3"
        alt="nanoparticles"
    />
  </div>
</template>

<script>
export default {
  name: "AppImage",
  props: {
    src: {
      type: String,
      required: true,
    }
  }
}
</script>

<style scoped>
</style>
