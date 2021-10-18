<template>
  <div class="options">
    <h1>Параметры</h1>
    <div class="options__menu">
      <div class="options__menu-checkbox">
        <div>
          <label class="options__menu-checkbox-item" for="showSize"
            >Показать размер:</label
          >
          <input
            @change="emit"
            v-model="options.show_size"
            type="checkbox"
            id="showSize"
          />
        </div>
        <div>
          <label class="options__menu-checkbox-item" for="showBorder"
            >Показать границу:</label
          >
          <input
            @change="emit"
            v-model="options.show_border"
            type="checkbox"
            id="showBorder"
          />
        </div>
        <div>
          <label class="options__menu-checkbox-item" for="showСontours"
            >Показать контуры:</label
          >
          <input
            @change="emit"
            v-model="options.show_contours"
            type="checkbox"
            id="showСontours"
          />
        </div>
        <div>
          <label class="options__menu-checkbox-item" for="OperatorCanny"
            >Оператор Кэнни:</label
          >
          <input
            @change="emit"
            v-model="options.canny"
            type="checkbox"
            id="OperatorCanny"
            placeholder="19"
          />
        </div>
      </div>
      <div class="options__menu-numeric">
        <div>
          <label for="particlesSizeNm">Размер частицы (нм):</label>
          <input
            @change="emit"
            v-model="options.particles_size_nm"
            type="number"
            id="particlesSizeNm"
          />
        </div>
        <div>
          <label for="lowerThreshold">Нижняя граница оператора Кэнни:</label>
          <input
            @change="emit"
            v-model="options.lower_threshold"
            type="number"
            id="lowerThreshold"
          />
        </div>
        <div>
          <label for="upperThreshold">Верхняя граница оператора Кэнни:</label>
          <input
            @change="emit"
            v-model="options.upper_threshold"
            type="number"
            id="upperThreshold"
          />
        </div>
        <div>
          <label for="sizeAccuracy">Масштаб:</label>
          <input
            @change="emit"
            v-model="options.size_accuracy"
            type="number"
            id="sizeAccuracy"
          />
        </div>
        <div>
          <label for="gaussianAccuracy">Точность фильтра Гаусса:</label>
          <label class="options__menu-numeric-value" for="gaussianAccuracy"
            >Значение: {{ options.gaussian_accuracy }}</label
          >
          <input
            class="options__menu-numeric-range"
            @change="emit"
            v-model="options.gaussian_accuracy"
            type="range"
            id="gaussianAccuracy"
            min="3"
            max="25"
            step="2"
          />
          
        </div>
      </div>
    </div>
  </div>
  <div class="advertising"></div>
</template>

<script>
export default {
  name: "AppOptions",
  data() {
    return {
      options: {
        show_size: true,
        show_border: false,
        show_contours: true,
        particles_size_nm: 200,
        gaussian_accuracy: 9,
        lower_threshold: 50,
        upper_threshold: 100,
        size_accuracy: 19,
        canny: false,
      },
    };
  },
  methods: {
    emit() {
      this.$emit("optionChanged", this.options);
    },
  },
  emits: ["optionChanged"],
};
</script>

<style lang="scss">
.options {
  grid-column: 1;
  grid-row: 1 / 3;
  width: 450px;
  border: 5px solid rgb(2, 2, 2);
  background: #f5f5dc;

  &__menu {
    display: grid;
    justify-content: center;
    grid-template-rows: repeat(2, minmax(100px, auto));

    &-checkbox {
      display: grid;
      grid-template-columns: repeat(2, minmax(100px, 170px));
      grid-template-rows: repeat(4, minmax(50px, auto));
      grid-row: 1;

      div {
        display: flex;
        grid-column: 1;
        justify-content: space-between;
      }

      &-item {
        font-size: 16px;
        font-family: "Heebo", sans-serif;
        font-style: normal;
        line-height: 10px;
        align-items: center;
        text-align: center;
        justify-content: center;
      }
    }

    &-numeric {
      &-value {
        position: absolute;
        left: 316px;
        margin-top: 70px;
      }
      &-range {
        -webkit-appearance: none;
        grid-column: 2/3;
        min-width: 160px;
        height: 16px;
        border: 2px solid rgb(36, 35, 35);
        background-color: rgb(255, 255, 255);
        
        &::-webkit-slider-thumb {
          appearance: none;
          width: 16px;
          height: 17px;
          background: #3b3939;
          border-radius: 50%;
          cursor: pointer;
        }
        &::after {
          content: "25";
          position: absolute;
          margin-top: 38px;
          left: 430px;
          font-size: 14px;
          font-weight: bold;
        }
        &::before {
          content: "0";
          position: absolute;
          margin-top: 38px;
          
          font-size: 14px;
          font-weight: bold;
        }

      }
      div {
        margin-top: 20px;
        display: flex;
        grid-column: 1;
        justify-content: space-between;
        align-items: center;
      }

      label {
        font-size: 16px;
        font-family: "Heebo", sans-serif;
        font-style: normal;
        line-height: 10px;
      }
    }

    input {
      border-radius: 12px;
      margin-left: 10px;
      align-items: center;
      text-align: center;
      border: 2px solid rgb(36, 35, 35);
    }
  }

  h1 {
    font-size: 26px;
    grid-row: 1;
    font-family: "Heebo", sans-serif;
    font-style: normal;
    font-weight: bold;
    line-height: 60px;
    margin: 10px;
    text-align: center;
  }
}

.advertising {
  width: 450px;
  display: flex;
  font-size: 26px;
  grid-row: 3;
  justify-content: center;
  border: 5px solid rgb(0, 0, 0);
  border-top: 0px;
  align-items: center;
  background-image: url("../assets/brawl.jpg");
  background-size: cover;
}
</style>
