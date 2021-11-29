<template>
  <button
      :class="{disabled: userContourMode || deleteContourMode || contours === []}"
      class="button_toggle"
      @click="toggleUserContourMode"
  >
    Пользовательский контур
  </button>
  <button
      :class="{disabled: userContours.length === 0 || userContourMode || deleteContourMode || contours}"
      class="button_clear"
      @click="clearContours"
  >
    Очистить контуры
  </button>
  <button
      :class="{disabled: userContourMode || deleteContourMode || contours}"
      class="button_clear"
      @click="clearContours"
  >
    Удалить контур
  </button>
  <div class="px-auto pt-32 content-center">
    <img
        draggable="false"
        :src="src"
        class="image"
        alt="nanoparticles"
        @click="handleNewUserPoint"
    />
  </div>
</template>

<script>
export default {
  name: "AppImage",
  data() {
    return {
      currentContour: [],
      userContours: [],
      userContourMode: false,
      deleteContourMode: false
    }
  },
  props: {
    src: {
      type: String,
      required: true,
    },
    contours: {
      type: Array,
      required: false,
    }
  },
  computed: {
    orderedUserContours() {
      let userContours = this.userContours;
      userContours = userContours.map(contour => {
        contour = contour.sort((firstEl, secondEl) => firstEl[1] - secondEl[1]);
        let pointsTop = contour.slice(0, 2);
        let pointsBottom = contour.slice(2);
        pointsTop.sort((firstEl, secondEl) => firstEl[0] - secondEl[0]);
        pointsBottom.sort((firstEl, secondEl) => secondEl[0] - firstEl[0]);
        contour = pointsTop.concat(pointsBottom);
        return contour
      })
      return userContours;
    }
  },
  emits: ["user-contours-drawn"],
  methods: {
    emit() {
      this.$emit("user-contours-drawn", JSON.stringify(this.orderedUserContours));
    },
    clearContours() {
      this.userContours = []
      this.emit()
    },
    toggleUserContourMode() {
      this.userContourMode = !this.userContourMode;
    },
    handleNewUserPoint(e) {
      if (this.userContourMode) {
        if (this.currentContour.length < 4) {
          this.currentContour.push(this.getClickCoordinates(e));
        }

        if (this.currentContour.length === 4) {
          this.userContours.push(this.currentContour)
          this.currentContour = []
          this.emit()
          this.toggleUserContourMode()
        }
      }
    },
    getClickCoordinates(e) {
      const rect = e.target.getBoundingClientRect();
      const x = Math.round(e.clientX - rect.left);
      const y = Math.round(e.clientY - rect.top);
      return [x, y]
    }
  }
}
</script>

<style scoped>
.image {
  box-sizing: border-box;
}

.button_toggle {
  position: absolute;
  bottom: 100px;
  right: 100px;
  background-color: white;
}

.button_clear {
  position: absolute;
  bottom: 50px;
  right: 100px;
  background-color: white;
}

.disabled {
  display: none;
}
</style>
