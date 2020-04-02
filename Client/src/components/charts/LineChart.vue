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
    },
    stateName: {
      type: String,
      required: true,
    },
  },
  computed: {
    ...mapState({
      dataset (state) {
        return state[this.stateName]
      },
      time: 'time',
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
        this.chart.data.datasets[0].data = newValue;
        this.chart.update();
      },
    },
    'time': {
      immediate: false,
      deep: true,
      handler(newValue) {
        this.chart.data.labels = newValue;
        this.chart.update();
      },
    },
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    
    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: this.time,
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