<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <app-options></app-options>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import AppOptions from './components/AppOptions.vue'

export default {
  name: 'App',
  components: {HelloWorld, AppOptions}
}
</script>

<style>

* {
  margin: 0;
  padding: 0;
}
#app {
    display: grid;
    grid-template-columns: minmax(150px, 450px) minmax(150px, 750px) minmax(150px,auto);
    grid-template-rows: repeat(3, minmax(150px, auto));
    height: 100vh;
    background: #F5F5DC;
    background:linear-gradient(to right, rgb(118, 217, 238) 0%, rgb(160, 234, 250) 100%);
    /* background:linear-gradient(to right, rgb(137, 226, 255), rgb(166, 142, 255)); */
}
</style>
