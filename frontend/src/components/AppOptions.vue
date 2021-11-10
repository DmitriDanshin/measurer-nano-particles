<template>
  <div class="options overflow-y-hidden">
    <div
        class="bg-gray-900 md:bg-gray-900 px-2 text-center bottom-0 md:pt-8 md:top-0 md:left-0 h-16 md:h-screen  overflow-y-auto pb-8"
    >
      <div class="w-full md:relative mx-auto lg:float-right lg:px-6">
        <ul class="list-reset flex flex-row md:flex-col text-center md:text-left mt-8">
          <li class="flex align-center">
            <label
                :class="options.showSize ? 'border-blue-800 text-blue-500' : 'border-gray-900 hover:text-pink-500 hover:border-pink-500'"
                class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 "
                for="show_size"
            >
              Размеры
            </label>
            <input
                id="show_size"
                v-model="options.showSize"
                type="checkbox"
                class="hidden"
                @change="emit"
            />
          </li>
          <li class="flex align-center">
            <label
                :class="options.showBorder ? 'border-blue-800 text-blue-500' : 'border-gray-900 hover:text-pink-500 hover:border-pink-500'"
                class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 "
                for="show_border"
            >
              Границы
            </label>
            <input
                id="show_border"
                v-model="options.showBorder"
                type="checkbox"
                class="hidden"
                @change="emit"
            />
          </li>
          <li class="flex align-center">
            <label
                :class="options.canny ? 'border-blue-800 text-blue-500' : 'border-gray-900 hover:text-pink-500 hover:border-pink-500'"
                class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 "
                for="canny"
            >
              Оператор Кэнни
            </label>
            <input
                id="canny"
                v-model="options.canny"
                type="checkbox"
                class="hidden"
                @change="emit"
            />
          </li>
          <li class="flex align-center">
            <label
                :class="options.showContours ? 'border-blue-800 text-blue-500' : 'border-gray-900 hover:text-pink-500 hover:border-pink-500'"
                class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 "
                for="show_contours"
            >
              Контуры
            </label>
            <input
                id="show_contours"
                v-model="options.showContours"
                type="checkbox"
                class="hidden"
                @change="emit"
            />
          </li>
          <li class="flex align-center">
            <label
                :class="options.showMidpoints ? 'border-blue-800 text-blue-500' : 'border-gray-900 hover:text-pink-500 hover:border-pink-500'"
                class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 "
                for="show_midpoints"
            >
              Средние линии
            </label>
            <input
                id="show_midpoints"
                v-model="options.showMidpoints"
                type="checkbox"
                class="hidden"
                @change="emit"
            />
          </li>
        </ul>
        <br>
        <hr>
        <ul class="list-reset  flex-row md:flex-col text-center md:text-left mt-8">
          <li>
            <label
                class="text-white no-underline block"
                for="particles_size_nm"
            >
              Масштаб ( нм ):
            </label>
            <input
                id="particles_size_nm"
                v-model="options.particlesSizeNm"
                class="mt-1 block border rounded-lg px-3 bg-black border-blue-800 placeholder-white-500 text-white"
                @change="emit"
            />
          </li>
          <li>
            <label
                class="text-white no-underline mt-2"
                for="lower_threshold"
            >
              Нижняя граница оператора Кэнни:
            </label>
            <input
                id="lower_threshold"
                v-model="options.lowerThreshold"
                class="mt-1 block"
                type="range"
                min="0"
                max="1000"
                step="10"
                @change="emit"
            />
          </li>
          <li>
            <label
                class="text-white no-underline mt-2"
                for="upper_threshold"
            >
              Верхняя граница оператора Кэнни:
            </label>
            <input
                id="upper_threshold"
                v-model="options.upperThreshold"
                class="mt-1 block"
                type="range"
                min="0"
                max="1000"
                step="10"
                @change="emit"
            />
          </li>
          <li>
            <label
                class="text-white no-underline mt-2"
                for="gaussian_accuracy_width"
            >
              Точность фильтра Гаусса по ширине:
            </label>
            <label
                class="text-white no-underline mt-2"
                for="gaussian_accuracy_width"
            >
              {{ options.gaussianAccuracyWidth }}
            </label>
            <input
                id="gaussian_accuracy_width"
                v-model="options.gaussianAccuracyWidth"
                class="mt-1 block"
                type="range"
                min="3"
                max="25"
                step="2"
                @change="emit"
            />
          </li>
          <li>
            <label
                class="text-white no-underline mt-2"
                for="gaussian_accuracy_height"
            >
              Точность фильтра Гаусса по высоте:
            </label>
            <label
                class="text-white no-underline mt-2"
                for="gaussian_accuracy_height"
            >
              {{ options.gaussianAccuracyHeight }}
            </label>
            <input
                id="gaussian_accuracy_height"
                v-model="options.gaussianAccuracyHeight"
                class="mt-1 block"
                type="range"
                min="3"
                max="25"
                step="2"
                @change="emit"
            />
          </li>
          <li>
            <label
                class="text-white no-underline mt-2"
                for="size_accuracy"
            >
              Точность учитывания размера:
            </label>
            <input
                id="size_accuracy"
                v-model="options.sizeAccuracy"
                class="mt-1 border rounded-lg px-3 bg-black border-blue-800 placeholder-white-500 text-white block "
                @change="emit"
            />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppOptions",
  data() {
    return {
      options: {
        showMidpoints: true,
        showSize: true,
        showBorder: false,
        showContours: true,
        particlesSizeNm: 200,
        gaussianAccuracyWidth: 7,
        gaussianAccuracyHeight: 7,
        lowerThreshold: 50,
        upperThreshold: 100,
        sizeAccuracy: 10,
        canny: false,
      },
    };
  },
  methods: {
    emit() {
      this.$emit("option-changed", this.options);
    },
  },
  emits: ["option-changed"],
};
</script>

<style>

</style>
