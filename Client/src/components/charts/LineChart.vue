<template>
  <canvas :id="name" />
</template>

<script>
import { Chart } from 'chart.js';
import { mapState } from 'vuex';
import chartColorsMixin from '../../mixins/chartColorsMixin';
import utilsMixin from '../../mixins/utilsMixin';

export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: false,
      default: '',
    },
    dataStateName: {
      type: String,
      required: true,
    },
    unit: {
      type: String,
      required: true,
    },
    colorsLimits: {
      type: Array,
      required: true,
      validator: function(value) {
        value.sort().reverse();
        return true;
      },
    },
    useAvgForColor: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  computed: {
    ...mapState({
      dataset (state) {
        return state[this.dataStateName]
      },
      time: 'time',
    }),
  },
  data() {
    return {
      chart: undefined,
    }
  },
  methods: {
    getChartColor(value) {
      let limit = this.colorsLimits.find(limit => limit.value <= value);
      return limit ? limit.color : 'grey';
    },
  },
  watch: {
    'dataset': {
      immediate: false,
      deep: true,
      handler(newValue) {
        // data
        this.chart.data.datasets[0].data = newValue;

        const min = Math.min(...newValue);
        const max = Math.max(...newValue);
        const avg = this.arrayAverage(newValue);

        // colors
        this.chart.data.datasets[0].backgroundColor = this.getColorWithAlpha(this[this.getChartColor(this.useAvgForColor ? avg : max)], 0.3);
        this.chart.data.datasets[0].borderColor = this[this.getChartColor(this.useAvgForColor ? avg : max)];

        // y range
        this.chart.options.scales.yAxes[0].ticks.min = this.unit === '%' ? 0 : 10 * Math.floor((min - 10) / 10);
        this.chart.options.scales.yAxes[0].ticks.max = this.unit === '%' ? 100 : 10 * Math.ceil((max + 10) / 10);

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
  mixins: [
    chartColorsMixin,
    utilsMixin,
  ],
  mounted() {
    var ctx = document.getElementById(this.name);
    
    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: this.time,
        datasets: [
          {
            backgroundColor: this.getColorWithAlpha(this[this.getChartColor(Math.max(...this.dataset))], 0.3),
            borderColor: this[this.getChartColor(Math.max(...this.dataset))],
            fill: true,
            data: this.dataset,
            lineTension: 0,
          }
        ]
      },
      options: {
        title: {
          display: true,
          fontSize: 20,
          fontColor: this.blue,
          text: this.title,
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
              return label + this.unit;
            }.bind(this)
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
                drawOnChartArea: false,
                drawTicks: false,
                color: this.grey,
              },
              ticks: {
                display: false,
              },
              borderColor: this.grey,
              type: 'time',
              time: {
                unit: 'minutes',
                tooltipFormat: 'HH:mm:ss'
              },
            }
          ],
          yAxes: [
            {
              gridLines: {
                display: true,
                drawOnChartArea: false,
                color: this.grey,
              },
              ticks: {
                min: this.unit === '%' ? 0 : 10 * Math.floor((Math.min(...this.dataset) - 10) / 10),
                max: this.unit === '%' ? 100 : 10 * Math.ceil((Math.max(...this.dataset) + 10) / 10),
                stepSize: 10,
                callback: function(value) {
                  return value + this.unit + ' ';
                }.bind(this)
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