<template>
  <div class="options">
    <h1>Параметры</h1>
    <div class="options__menu">
      <div class="options__menu-checkbox">
        <div>
          <label
              class="options__menu-checkbox-item"
              for="show_size"
          >
            Показать размер:
          </label>
          <input
              id="show_size"
              v-model="options.showSize"
              type="checkbox"
              @change="emit"
          />
        </div>
        <div>
          <label
              class="options__menu-checkbox-item"
              for="show_border"
          >
            Показать границу:
          </label>
          <input
              id="show_border"
              v-model="options.showBorder"
              type="checkbox"
              @change="emit"
          />
        </div>
        <div>
          <label
              class="options__menu-checkbox-item"
              for="show_contours"
          >
            Показать контуры:
          </label>
          <input
              id="show_contours"
              v-model="options.showContours"
              type="checkbox"
              @change="emit"
          />
        </div>
        <div>
          <label
              class="options__menu-checkbox-item"
              for="canny"
          >
            Оператор Кэнни:
          </label>
          <input
              id="canny"
              v-model="options.canny"
              type="checkbox"
              placeholder="19"
              @change="emit"
          />
        </div>
      </div>
      <div class="options__menu-numeric">
        <div>
          <label for="particles_size">Размер частицы (нм):</label>
          <input
              id="particles_size"
              v-model="options.particlesSize"
              type="number"
              @change="emit"
          />
        </div>
        <div>
          <label for="lower_threshold">Нижняя граница оператора Кэнни:</label>
          <input
              id="lower_threshold"
              v-model="options.lowerThreshold"
              type="number"
              @change="emit"
          />
        </div>
        <div>
          <label for="upper_threshold">Верхняя граница оператора Кэнни:</label>
          <input
              id="upper_threshold"
              v-model="options.upperThreshold"
              type="number"
              @change="emit"
          />
        </div>
        <div>
          <label for="size_accuracy">Масштаб:</label>
          <input
              id="size_accuracy"
              v-model="options.sizeAccuracy"
              type="number"
              @change="emit"
          />
        </div>
        <div>
          <label for="gaussian_accuracy">Точность фильтра Гаусса:</label>
          <label for="gaussian_accuracy">{{ options.gaussianAccuracy }}</label>
          <input
              id="gaussian_accuracy"
              v-model="options.gaussianAccuracy"
              class="options__menu-numeric-range"
              type="range"
              min="3"
              max="25"
              step="2"
              @change="emit"
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
        showSize: true,
        showBorder: false,
        showContours: true,
        particlesSize: 200,
        gaussianAccuracy: 9,
        lowerThreshold: 50,
        upperThreshold: 100,
        sizeAccuracy: 19,
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
  border-top: 0;
  align-items: center;
  background-image: url("../assets/brawl.jpg");
  background-size: cover;
}
</style>
