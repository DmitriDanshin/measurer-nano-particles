<template class>
  <app-nav
      @change-page="changePage"
      @handle-file-change="handleFileChange"
  />
  <component
      :is="currentPage"
      :src="src"
      :info="info"
      @handle-options-change="handleOptionsChange"
      @handle-new-user-contours="handleNewUserContours"
  />
</template>

<script>

import AppHistory from "./AppHistory";
import AppMain from "./AppMain";
import AppNav from "./AppNav";
import AppChartDistribution from "./AppChartDistribution";

export default {
  name: "AppWrapper",
  components: {AppNav, AppMain, AppHistory, AppChartDistribution},
  data() {
    return {
      currentPage: "AppMain",
      file: '',
      src: require('../assets/placeholder.png'),
      options: {},
      userContours: '[]',
      excludedContours: '[]',
      info: {},
      isHistory: false
    }
  },
  methods: {
    changePage(page) {
      this.currentPage = page;
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
    handleNewUserContours(newContours) {
      this.userContours = newContours
      this.getData()
    },
    handleFileChange(e) {
      this.file = e.target.files[0];
      this.src = URL.createObjectURL(this.file);
      this.getData();
    },
    handleOptionsChange(newOptions) {
      this.options = newOptions;
      if (this.file) {
        this.getData();
      }
    },
    async getData() {
      const formData = new FormData();
      formData.append('img', this.file);
      formData.append('user_contours', this.userContours);
      formData.append('excluded_contours', "[]");
      const options = this.options;
      console.log(this.userContours)
      const request = {formData, options};
      const result = await this.process(request);

      this.src = "data:image/png;base64, " + result.image;

      this.info = {
        amount: result.amount,
        maxSize: result.maxSize,
        minSize: result.minSize,
        sizes: result.sizes,
        mean: result.mean,
        median: result.median,
        contours: result.contours,
      }
      console.log(result.contours)
    }
  }
};
</script>

<style lang="scss" scoped>

</style>
