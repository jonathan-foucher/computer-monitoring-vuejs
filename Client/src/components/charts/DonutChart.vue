<template>
  <canvas :id="name" />
</template>

<script>
import { Chart } from 'chart.js';
import { mapState } from 'vuex';
import chartColorsMixin from '../../mixins/chartColorsMixin';

export default {
   props: {
    name: {
      type: String,
      required: true,
    },
    title: {
      type: Array,
      required: true,
    },
    dataStateName: {
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
  methods: {
    getChartColor(value) {
      let limit = this.colorsLimits.find(limit => limit.value <= value);
      return limit ? limit.color : 'grey';
    },
  },
  mixins: [chartColorsMixin],
  watch: {
    'dataset': {
      immediate: false,
      deep: true,
      handler(newValue) {
        this.chart.data.datasets[0].data = [newValue, 100 - newValue];

        this.chart.data.datasets[0].backgroundColor[0] = this.getColorWithAlpha(this[this.getChartColor(newValue)], 0.3);
        this.chart.data.datasets[0].borderColor[0] = this[this.getChartColor(newValue)];

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
            backgroundColor: [
              this.getColorWithAlpha(this[this.getChartColor(this.dataset)], 0.3),
              this.getColorWithAlpha(this.white, 0.08),
            ],
            borderColor: [
              this[this.getChartColor(this.dataset)],
              this.getColorWithAlpha(this.grey, 0.5),
            ],
            fill: true,
            data: [this.dataset, 100 - this.dataset],
            lineTension: 0,
            devicePixelRatio: 5,
          }
        ]
      },
      options: {
        circumference: Math.PI,
        rotation: Math.PI,
        title: {
          display: true,
          fontSize: 20,
          fontColor: this.blue,
          text: this.title,
        },
        responsive: true,
        animation: {
          duration: 0,
        },
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