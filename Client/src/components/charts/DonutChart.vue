<template>
  <canvas :id="name"></canvas>
</template>

<script>
import { Chart } from 'chart.js';

export default {
   props: {
    name: {
      type: String,
      required: true,
    },
    title: {
      required: false,
      default: ''
    }
  },
 data() {
    return {
      dataset: [70, 30],
    }
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    this.chart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        datasets: [
          {
            backgroundColor: ['rgba(54, 162, 235, 0.3)', 'rgba(200, 162, 235, 0.3)'],
            borderColor: ['rgb(54, 162, 235)', 'rgb(200, 162, 235)'],
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
        responsive: true,
        layout: {
          padding: {
            left: 20,
            right: 20,
            top: 0,
            bottom: 20,
          },
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