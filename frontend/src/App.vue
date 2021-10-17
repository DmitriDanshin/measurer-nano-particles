<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <app-options></app-options>
  <app-information></app-information>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import AppOptions from './components/AppOptions.vue'
import AppInformation from './components/AppInformation.vue'

export default {
  name: 'App',
  components: {HelloWorld, AppOptions, AppInformation}
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
    grid-template-rows: repeat(3, minmax(220px, auto));
    height: 100vh;
    background: #F5F5DC;
    background-color: #363535;
  
}
</style>
