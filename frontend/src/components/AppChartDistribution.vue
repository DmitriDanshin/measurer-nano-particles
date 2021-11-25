<template>
  <section class="flex justify-between bg-gray-800 overflow-y-hidden">
    <div class="w-full h-4/5 mt-12">
      <canvas
          ref="ctx"
      ></canvas>
    </div>
    <AppInformation :info="info"/>
  </section>
</template>

<script>
import AppInformation from "./AppInformation";
import Chart from 'chart.js/auto';

export default {
  name: "AppChartDistribution",
  components: {AppInformation},
  mounted() {
    const myChart = new Chart(this.$refs.ctx.getContext('2d'), {
      type: 'bar',
      data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
          label: '# of Votes',
          data: [12, 19, 3, 5, 2, 3],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)',
            'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    console.log(myChart)
  },
  props: {
    info: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
