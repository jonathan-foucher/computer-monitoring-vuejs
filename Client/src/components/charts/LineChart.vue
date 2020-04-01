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
      required: false,
      default: ''
    }
  },
  computed: {
    ...mapState({
      dataset: 'data',
    }),
  },
  data() {
    return {
      chart: undefined,
      dates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    }
  },
  watch: {
    'dataset': {
      immediate: false,
      deep: true,
      handler(newValue) {
        this.chart.data.datasets[0].data = newValue;
        this.chart.update();
      },
    },
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    
    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: this.dates,
        datasets: [
          {
            backgroundColor: 'rgba(54, 162, 235, 0.3)',
            borderColor: 'rgb(54, 162, 235)',
            fill: true,
            data: this.dataset,
            lineTension: 0,
          }
        ]
      },
      options: {
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
          callbacks: {
            label: function(tooltipItem, data) {
              var label = data.datasets[tooltipItem.datasetIndex].label || '';

              if (label) {
                label += ': ';
              }

              label += Math.floor(tooltipItem.yLabel);
              return label + '°C';
            }
          }
        },
        legend: {
          display: false,
        },
        scales: {
          xAxes: [
            {
              gridLines: {
                display: true,
                color: '#FFFFFF',
              },
              borderColor: 'white',
              type: 'time',
              time: {
                unit: 'hour',
                displayFormats: {
                  hour: 'M/DD @ hA'
                },
                tooltipFormat: 'MMM. DD @ hA'
              },
            }
          ],
          yAxes: [
            {
              ticks: {
                callback: function(value) {
                  return value + '°C';
                }
              }
            }
          ]
        }
      }
    });
  }
}
</script>

<style scoped>
</style>