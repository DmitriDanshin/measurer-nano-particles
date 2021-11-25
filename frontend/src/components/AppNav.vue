<template>
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
          <app-nav-item
              v-for="item in items"
              :key="item.pageName"
              :name="item.name"
              :page-name="item.pageName"
              :isActive="item.isActive"
              @change-page="changePage"
          />
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import AppNavItem from "./AppNavItem";

export default {
  name: "AppNav",
  components: {AppNavItem},
  data() {
    return {
      items: [
        {
          name: "Главная",
          pageName: "AppMain",
          isActive: true
        },
        {
          name: "Распределение",
          pageName: "AppChartDistribution",
          isActive: false
        },
        {
          name: "История",
          pageName: "AppHistory",
          isActive: false
        },

      ]
    }
  },
  methods: {
    handleFileChange(e) {
      this.$emit('handle-file-change', e);
    },
    changePage(page) {
      this.$emit('change-page', page);
      this.items.forEach(i => i.isActive = false)
      const pageToChange = this.items.find(i => i.pageName === page);
      pageToChange.isActive = true
    }
  }

}
</script>

<style scoped>

</style>
