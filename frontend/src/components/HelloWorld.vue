<template>
  <div class="container">
    <img src="" alt="" ref="img" />
  </div>
  <div class="footer">
    <div class="hello">
      <input @change="getImage" type="file" id="input" />
    </div>
    <div v-if="amount">Фотография :{{ amount?.slice(0, -4) }}</div>
    
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      image: null,
      amount: "",
    };
  },
  methods: {
    getImage(e) {

      const image = this.$refs.img;
      const file = e.target.files[0];
      const formData = new FormData();

      formData.append('file', file);
      fetch('http://fastapi.space/', {
        method: "POST",
        body: formData
      }).then((response) => {
        return response.json()
      }).then(response => {
        image.src = "data:image/png;base64, " + response.image;
        console.log(response)
      })
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

.container{ 
  grid-column: 2;
  grid-row: 1/3;
  border: 1px solid rgb(2, 2, 2);
  text-align: center;
 
  
  
  img {
    grid-row: 1 / 3;
    grid-column: 2 / 3;
    border: 5px solid rgb(11, 68, 77) ;
    width: 99%;
    height: 99%;
        
    
  }
}
.footer {
  margin: 20px;
  grid-column: 2;
  grid-row: 3/4;
}








</style>
