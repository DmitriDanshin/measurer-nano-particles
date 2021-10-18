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

* {
  margin: 0;
  padding: 0;
}

#app {
  display: grid;
  grid-template-columns: minmax(150px, 450px) minmax(150px, 750px) minmax(150px, auto);
  grid-template-rows: repeat(3, minmax(220px, auto));
  height: 100vh;
  background: #F5F5DC;
  background-color: #363535;

}
</style>
