<template>
  <canvas :id="name"></canvas>
</template>

<script>
import { Chart } from 'chart.js';
import { mapState } from 'vuex';

export default {
   props: {
    name: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: false,
      default: ''
    },
    dataStateName: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState({
      dataset (state) {
        return state[this.dataStateName]
      },
    }),
  },
  data() {
    return {
      chart: undefined,
    }
  },
  watch: {
    'dataset': {
      immediate: false,
      deep: true,
      handler(newValue) {
        this.chart.data.datasets[0].data.length = 0;
        this.chart.data.datasets[0].data.push(newValue, 100 - newValue);
        this.chart.update();
      },
    },
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    this.chart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        datasets: [
          {
            backgroundColor: ['rgba(54, 162, 235, 0.3)', 'rgba(200, 162, 235, 0.02)'],
            borderColor: ['rgb(54, 162, 235)', 'rgba(200, 162, 235, 0.5)'],
            fill: true,
            data: this.dataset,
            lineTension: 0,
          }
        ]
      },
      options: {
        circumference: Math.PI,
        rotation: Math.PI,
        title: {
          display: true,
          text: this.title
        },
        animation: {
          duration: 0,
        },
        responsive: true,
        layout: {
          padding: {
            left: 20,
            right: 20,
            top: 0,
            bottom: 20,
          },
        },
        tooltips: {
          enabled: false,
        },
        legend: {
          display: false,
        },
      }
    });
  }
}
</script>

<style scoped>
</style>