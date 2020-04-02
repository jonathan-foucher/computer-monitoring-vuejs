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
      type: String,
      required: false,
      default: '',
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
  mixins: [chartColorsMixin],
  watch: {
  'dataset': {
    immediate: false,
    deep: true,
    handler(newValue) {
      this.chart.data.datasets[0].data = newValue;

      this.chart.data.labels.length = 0;
      for(let i = 1; i <= newValue.length; i++) {
        this.chart.data.labels.push('Core #' + i + ' - ' + (Math.round(newValue[i - 1]).toString().length === 1 ? '  ' : '') + Math.round(newValue[i - 1]) + '%');
      }

      this.chart.update();
    },
  },
  },
  mounted() {
    var ctx = document.getElementById(this.name);
    this.chart = new Chart(ctx, {
      type: 'radar',
      data: {
				labels: [],
        datasets: [
          {
						backgroundColor: this.getColorWithAlpha(this.blue, 0.3),
            borderColor: this.blue,
						pointBackgroundColor: this.grey,
						pointBorderColor: '#fff',
            fill: true,
            data: this.dataset,
          }
        ]
      },
      options: {
        title: {
          display: true,
          fontColor: this.blue,
          fontSize: 20,
          text: this.title,
        },
        responsive: true,
        maintainAspectRatio: true,
        layout: {
          padding: {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
          },
        },
        tooltips: {
          enabled: false,
        },
        legend: {
          display: false,
				},
				scale: {
					gridLines: {
						color: this.purple,
					},
					ticks: {
						display: false,
						beginAtZero: true,
						max: 100
          },
          pointLabels: {
            fontColor: this.blue,
            fontSize: 14,
          },
				}
      }
    });
  }
}
</script>

<style scoped>
</style>