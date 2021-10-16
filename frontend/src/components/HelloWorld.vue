<template>

  <div>
    <input type="checkbox" id="show_size">
    <input type="checkbox" id="show_border">
    <input type="checkbox" id="show_contours">
    <label for="gaussian_accuracy">Гауссово</label>
    <input v-model="number" type="range" min="3" max="25" id="gaussian_accuracy" step="2">
    <label for="gaussian_accuracy">{{number}}</label>
    <input type="number" id="lower_threshold">
    <input type="number" id="upper_threshold">
    <input type="number" id="size_accuracy">
    <input type="checkbox" id="canny">
  </div>


  <img :src="src" alt="">
  <div>{{ amount?.slice(0, -4) }}</div>

  <div class="hello">
    <input @change="getimage" type="file" id="input">
  </div>
  <button @click="getImage">sss</button>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      image: null,
      amount: "",
      file: '',
      src: '',
      number: 3

    }
  },
  methods: {
    async aaa(formData) {
      let result = await fetch('http://fastapi.space/?show_size=true&show_border=false&show_contours=true&particles_size_nm=250&gaussian_accuracy=19&blur_accuracy=60&size_accuracy=19', {
        method: "POST",
        body: formData
      });
      result = await result.json();
      return "data:image/png;base64, " + result.image ;
    },

    async getImage() {
      let file = this.file;
      this.amount = file.name;

      const formData = new FormData();
      formData.append('file', file);
      this.src = await this.aaa(formData);
    },
    getimage(e) {
      this.file = e.target.files[0];
      this.src = URL.createObjectURL(this.file);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img {
  border: 5px solid black;
  max-height: 750px;
  width: auto;
}

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
