<template>
  <div class="information overflow-y-hidden">
    <div
        class="bg-gray-900 md:bg-gray-900 px-2 text-center bottom-0 md:pt-8 md:top-0 md:left-0 h-16 md:h-screen"
    >
      <div class="w-full md:relative mx-auto lg:float-right lg:px-6">
        <ul class="list-reset flex flex-row md:flex-col text-center md:text-left mt-8">
          <li class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 ">Количество частиц:
            <strong>{{ info.amount }}</strong></li>
          <li class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 ">Максимальный размер:
            <strong>{{ info.maxSize }}</strong></li>
          <li class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 ">Минимальный размер:
            <strong>{{ info.minSize }}</strong></li>
          <li class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 ">Средний размер: <strong>{{
              info.mean
            }}</strong></li>
          <li class="block py-1 md:py-3 pl-1 align-middle text-white no-underline border-b-2 ">Медианный размер:
            <strong>{{ info.median }}</strong></li>
        </ul>
      </div>
    </div>
  </div>

</template>
<script>
export default {
  name: "AppInformation",
  props: {
    info: Object
  }
};
</script>

<style scoped>

</style>
