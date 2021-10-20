<template>
  <div class="container">
    <img
        :src="src"
        alt=""
    />
  </div>
  <div class="footer">
    <label class="footer__btn">
      <input
          id="input"
          class="footer__btn-inputfile"
          type="file"
          @change="handleFileChange"
      />
      <p class="footer__btn-title">Добавить фотографию</p>
      <img
          class="footer__btn-icon"
          src="../assets/fileinput.png"
          alt=""
      />
    </label>
    <!-- <div class="footer__name">
      Вы используете фотографию :{{ amount?.slice(0, -4) }}
    </div> -->
  </div>
  <app-options @optionChanged="handleOptionsChange"/>
  <app-information :info="info"/>
</template>

<script>
import AppOptions from "./AppOptions";
import AppInformation from "./AppInformation";

export default {
  name: "AppWrapper",
  components: {AppOptions, AppInformation},
  data() {
    return {
      file: '',
      src: require('../assets/placeholder.png'),
      options: {},
      info: {}
    }
  },
  methods: {
    handleOptionsChange(newOptions) {
      this.options = newOptions;
      if (this.file) this.getData();
    },
    async process(request) {
      let url = new URL('http://fastapi.space/');

      for (const option in request.options) {
        url.searchParams.set(option.replace(/[A-Z]/,
            match => `_${match.toLowerCase()}`), request.options[option]);
      }

      let result = await fetch(url, {
        method: "POST",
        body: request.formData
      });
      result = await result.json();
      return result;
    },
    handleFileChange(e) {
      this.file = e.target.files[0];
      this.src = URL.createObjectURL(this.file);
      this.getData();
    },
    async getData() {
      const formData = new FormData();
      formData.append('file', this.file);
      let options = this.options;
      let request = {formData, options};
      let result = await this.process(request);
      this.src = "data:image/png;base64, " + result.image;
      this.info = {
        amount: result.amount,
        maxSize: result.maxSize,
        minSize: result.minSize,
        sizes: result.sizes,
        mean: result.mean,
        median: result.median
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.container {
  grid-column: 2;
  grid-row: 1/3;
  border: 2px solid #000000;
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
  border-top: 0;
  padding: 10px;


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
