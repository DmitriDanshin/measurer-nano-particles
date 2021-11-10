<template>

  <app-wrapper/>
</template>

<script>
import AppWrapper from './components/AppWrapper.vue'

export default {
  name: 'App',
  components: {AppWrapper},
  data() {
    return {
      options: {}
    }
  }
}
</script>

<style>
body {
  @apply bg-gray-800;
}

* {
  margin: 0;
  padding: 0;
}

</style>
