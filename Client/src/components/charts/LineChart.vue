<template>
  <canvas :id="chartName"></canvas>
</template>

<script>
import { Chart } from 'chart.js';

export default {
  props: {
    chartName: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      dataset: [42, 48, 52, 40, 40, 45, 60, 55, 50, 45, 47, 43, 47, 45, 43, 42, 48, 45, 43, 43],
      dates: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    }
  },
  mounted() {
    var ctx = document.getElementById(this.chartName);
    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: this.dates,
        datasets: [
          {
            label: 'Avg. Temp',
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
          text: 'Temperature with Chart.js'
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