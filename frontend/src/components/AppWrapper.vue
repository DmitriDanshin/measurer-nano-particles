<template class>
  <!-- В отдельный компонент -->
  <nav
      id="header"
      class="bg-gray-900 w-full z-10 top-0 shadow absolute"
  >
    <div class="w-full container mx-auto flex flex-wrap items-center mt-0 pb-3 md:pb-0">
      <div class="w-1/2 pl-2 md:pl-0"></div>
      <div class="w-1/2 pr-0"></div>
      <div
          id="nav-content"
          class="w-full flex-grow lg:flex lg:items-center lg:w-auto hidden lg:block mt-2 lg:mt-0 bg-gray-900 z-20"
      >
        <ul class="list-reset lg:flex flex-1 items-center px-4 md:px-0">
          <li class="mr-6 my-2 md:my-0">
            <a
                href="#"
                class="block py-1 md:py-3 pl-1 align-middle text-blue-400 no-underline"
            >
              <label for="input">Выбрать файл</label>
              <input
                  id="input"
                  class="hidden"
                  type="file"
                  @change="handleFileChange"
              />
            </a>

          </li>
          <li class="mr-6 my-2 md:my-0">
            <a
                href="#"
                class="block py-1 md:py-3 pl-1 align-middle text-blue-400 no-underline hover:text-gray-100 border-b-2 border-blue-400 hover:border-blue-400"
            >
              Главная
            </a>
          </li>
          <li class="mr-6 my-2 md:my-0">
            <a
                href="#"
                class="block py-1 md:py-3 pl-1 align-middle text-blue-400 no-underline hover:text-gray-100 hover:border-blue-400"
            >
              История
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- В отдельный компонент / страницу -->
  <section v-if=false class="py-8">
    <div class="container mx-auto flex items-center flex-wrap pt-4 pb-12">
      <div class="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col">
        <img
            class="hover:grow hover:shadow-lg cursor-pointer h-64"
            src="https://picsum.photos/200/300?grayscale"
            alt="img"
        >
      </div>
      <div class="w-full md:w-1/3 xl:w-1/4 p-6 flex flex-col">
        <img
            class="hover:grow hover:shadow-lg cursor-pointer h-64"
            src="https://picsum.photos/200/300?grayscale"
            alt="img"
        >
      </div>
    </div>
  </section>

  <!-- В отдельный компонент / страницу -->
  <section v-if="true">
    <div class="flex justify-between bg-gray-800">
      <app-options @optionChanged="handleOptionsChange"/>
      <div class="px-auto pt-32  content-center">
        <img
            :src="src"
            class="mx-auto w-2/3 h-2/3"
            alt="nanoparticles"
        />
      </div>
      <app-information :info="info"/>
    </div>
  </section>
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
      info: {},
      isHistory: false
    }
  },
  methods: {
    handleOptionsChange(newOptions) {
      this.options = newOptions;
      if (this.file) {
        this.getData();
      }
    },
    async process(request) {
      const url = new URL('https://fastapi.space/images/');

      for (const option in request.options) {
        url.searchParams.set(option.replace(/[A-Z]/g,
            match => `_${match.toLowerCase()}`), request.options[option]);
      }

      const result = await fetch(url.toString(), {
        method: "POST",
        body: request.formData
      });

      return await result.json();
    },
    handleFileChange(e) {
      this.file = e.target.files[0];
      this.src = URL.createObjectURL(this.file);
      this.getData();
    },
    async getData() {
      const formData = new FormData();
      formData.append('img', this.file);
      const options = this.options;
      const request = {formData, options};
      const result = await this.process(request);

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

<style lang="scss" scoped>

</style>
