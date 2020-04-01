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
      required: true,
      default: ''
    }
  },
 data() {
    return {
      dataset: [70, 85, 50, 77, 62, 45],
    }
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    this.chart = new Chart(ctx, {
      type: 'radar',
      data: {
				labels: ['1', '2', '3', '4', '5', '6'],
        datasets: [
          {
						label: 'test',
						backgroundColor: 'rgba(54, 162, 235, 0.3)',
            borderColor: 'rgb(54, 162, 235)',
						pointBackgroundColor: 'rgba(179,181,198,1)',
						pointBorderColor: '#fff',
            fill: true,
            data: this.dataset,
          }
        ]
      },
      options: {
        title: {
          display: true,
          text: this.title
        },
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
          },
        },
        legend: {
          display: false,
				},
				maintainAspectRatio: true,
				scale: {
					gridLines: {
						color: 'rgb(200, 162, 235)'
					},
					ticks: {
						display: false,
						beginAtZero: true,
						max: 100
					}
				}
      }
    });
  }
}
</script>

<style scoped>
</style>