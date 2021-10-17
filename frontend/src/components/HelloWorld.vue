<template>
  <div class="container">
    <img src="" alt="" ref="img" />
  </div>
  <div class="footer">
    <label class="footer__btn">
      <input
        class="footer__btn-inputfile"
        @change="getImage"
        type="file"
        id="input"
      />
      <p class="footer__btn-title">Добавить фотографию</p>
      <img class="footer__btn-icon" src="../assets/fileinput.png" alt="" />
    </label>
    <!-- <div class="footer__name">
      Вы используете фотографию :{{ amount?.slice(0, -4) }}
    </div> -->
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

      formData.append("file", file);
      fetch("http://fastapi.space/", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          return response.json();
        })
        .then((response) => {
          image.src = "data:image/png;base64, " + response.image;
          console.log(response);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.container {
  grid-column: 2;
  grid-row: 1/3;
  border: 5px solid #000000;
  text-align: center;

  img {
    grid-row: 1 / 3;
    grid-column: 2 / 3;
    width: 100%;
    height: 100%;
  }
}
.footer {
  display: flex;
  align-items: center;
  justify-content: center;
  grid-column: 2;
  grid-row: 3/4;
  border: 5px solid #000000;
  border-top: 0px;
  padding: 10px;
  border-right: 5px solid rgb(0, 0, 0);
  border-left: 5px solid rgb(0, 0, 0);

  &__name {
    font-size: 18px;
    font-family: "Heebo", sans-serif;
    color: #f5f5dc;
    margin-top: 40px;
  }
  &__btn {
    margin-top: 20px;

    width: 200px;
    height: 50px;
    background-color: #f5f5dc;
    display: flex;
    cursor: pointer;
    border-radius: 20px;
    justify-content: space-around;
    align-items: center;
    border: 3px solid rgb(0, 0, 0);
    padding: 5px;
    transition: 0.8s;
    &:hover {
      color: #fff;
      transition: 0.8s;
      background-color: #a8a89a;
    }
    &-inputfile {
      display: none;
    }
    &-title {
      display: flex;
      font-size: 14px;
      font-family: "Heebo", sans-serif;
      align-items: center;
    }
    &-icon {
      width: 24px;
      height: 24px;
    }
  }
}
</style>
