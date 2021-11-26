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
import interact from "interactjs";

export default {
  name: "AppInformation",
  props: {
    info: Object,
  },
  mounted() {
    interact('.information')
        .resizable({
          edges: {left: true},
          listeners: {
            move: function (event) {
              let {x} = event.target.dataset
              x = (parseFloat(x) || 0) + event.deltaRect.left
              Object.assign(event.target.style, {
                width: `${event.rect.width}px`,
              })
              Object.assign(event.target.dataset, {x})
            }
          }
        })
  }
};
</script>

<style scoped>

</style>
