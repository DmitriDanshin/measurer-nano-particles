<template>
  <div class="px-auto pt-32 content-center">
    <img
        :src="src"
        class="mx-auto w-2/3 h-2/3 image"
        alt="nanoparticles"
    />
  </div>
</template>

<script>
import interact from 'interactjs'

export default {
  name: "AppImage",
  props: {
    src: {
      type: String,
      required: true,
    }
  },
  mounted() {
    interact('.image')
        .resizable({
          edges: { top: true, left: true, bottom: true, right: true },
          listeners: {
            move: function (event) {
              let { x, y } = event.target.dataset
              x = (parseFloat(x) || 0) + event.deltaRect.left
              y = (parseFloat(y) || 0) + event.deltaRect.top
              Object.assign(event.target.style, {
                width: `${event.rect.width}px`,
                height: `${event.rect.height}px`,
                transform: `translate(${0}px, ${y}px)`
              })
              Object.assign(event.target.dataset, { x, y })
            }
          }
        })
  }
}
</script>

<style scoped>
.image {
  box-sizing: border-box;
}
</style>
