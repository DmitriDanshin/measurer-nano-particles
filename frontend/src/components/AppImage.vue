<template>
  <button
      :class="{disabled: userContourMode || deleteContourMode || !contours}"
      class="button_toggle"
      @click="toggleUserContourMode"
  >
    Пользовательский контур
  </button>
  <button
      :class="{disabled: userContourMode || deleteContourMode || !contours}"
      class="button_clear"
      @click="toggleDeleteContourMode"
  >
    Удалить контур
  </button>
  <div class="px-auto pt-32 content-center">
    <img
        draggable="false"
        :src="src"
        class="image"
        :class="{'mx-auto w-2/3 h-2/3': !imageFullSize, 'image_full-size': imageFullSize}"
        alt="nanoparticles"
        @click="handleClick"
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
      deleteContourMode: false,
      imageFullSize: false,
      excludedContours: []
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
  emits: ["new-contour-settings", "toggle-image-full-size"],
  methods: {
    emit() {
      const contours = {
        userContours: JSON.stringify(this.orderedUserContours),
        excludedContours: JSON.stringify(this.excludedContours)
      }
      this.$emit("new-contour-settings", contours);
    },
    clearContours() {
      this.userContours = []
      this.emit()
    },
    toggleImageFullSize() {
      this.imageFullSize = !this.imageFullSize
      this.$emit("toggle-image-full-size", this.imageFullSize)
    },
    toggleUserContourMode() {
      this.userContourMode = !this.userContourMode;
      this.toggleImageFullSize()
    },
    toggleDeleteContourMode() {
      this.deleteContourMode = !this.deleteContourMode;
      this.toggleImageFullSize()
    },
    handleClick(e) {
      if (this.userContourMode) {
        this.handleNewUserPoint(e)
      } else if (this.deleteContourMode) {
        this.handleDeleteContour(e)
      }
    },
    handleNewUserPoint(e) {
      if (this.currentContour.length < 4) {
        this.currentContour.push(this.getClickCoordinates(e));
      }

      if (this.currentContour.length === 4) {
        this.userContours.push(this.currentContour)
        this.currentContour = []
        this.emit()
        this.toggleUserContourMode()
      }
    },
    handleDeleteContour(e) {
      const point = this.getClickCoordinates(e)
      const contour = this.getContourToDelete(point)
      this.deleteContour(contour)
      this.emit()
      this.toggleDeleteContourMode()
    },
    getContourToDelete(point) {
      const pointInPolygon = require('point-in-polygon');
      const contoursToDelete = this.contours.filter(contour => pointInPolygon(point, contour))
      return contoursToDelete.find(contour => !this.arrayIncludesSubArray(this.excludedContours, contour))
    },
    deleteContour(contour) {
      this.excludedContours.push(contour)
    },
    getClickCoordinates(e) {
      const rect = e.target.getBoundingClientRect();
      const x = Math.round(e.clientX - rect.left);
      const y = Math.round(e.clientY - rect.top);
      return [x, y]
    },
    arrayIncludesSubArray(array, subArray) {
      return JSON.stringify(array).includes(JSON.stringify(subArray))
    }
  }
}
</script>

<style scoped>
.image {
  box-sizing: border-box;
}

.image_full-size {
  max-width: none;
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
