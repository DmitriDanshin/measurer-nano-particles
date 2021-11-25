<template>
  <li class="mr-6 my-2 md:my-0">
    <a
        :class="{'active': isActive}"
        href="#"
        class="block py-1 md:py-3 pl-1 align-middle text-blue-400 no-underline hover:text-gray-100 "
        @click="changePage"
    >
      {{ name }}
    </a>
  </li>
</template>

<script>
export default {
  name: "AppNavItem",
  props: {
    name: {
      type: String,
      required: true,
    },
    pageName: {
      type: String,
      required: true,
    },
    isActive: {
      type: Boolean,
      required: true,
    }
  },
  methods: {
    changePage() {
      this.$emit("change-page", this.pageName)
    }
  }

}
</script>

<style scoped>
.active {
  @apply border-b-2 border-blue-400 hover:border-blue-400;
}
</style>
