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
    addCenterTextOnDonutChart() {
      Chart.pluginService.register({
        // add the value in the center of the chart
        beforeDraw: function (chart) {
          if (chart.config.options.elements.center) {
            //Get ctx from string
            var ctx = chart.chart.ctx;

            //Get options from the center object in options
            var centerConfig = chart.config.options.elements.center;
            var fontStyle = centerConfig.fontStyle || 'Arial';
            var txt = centerConfig.text;
            var color = centerConfig.color || '#000';
            var sidePadding = centerConfig.sidePadding || 20;
            var sidePaddingCalculated = (sidePadding / 100) * (chart.innerRadius * 2)
            ctx.font = "30px " + fontStyle;

            //Get the width of the string and also the width of the element minus 10 to give it 5px side padding
            var stringWidth = ctx.measureText(txt).width;
            var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

            // Find out how much the font can grow in width.
            var widthRatio = elementWidth / stringWidth;
            var newFontSize = Math.floor(30 * widthRatio);
            var elementHeight = (chart.innerRadius);

            // Pick a new font size so it will not be larger than the height of label.
            var fontSizeToUse = Math.min(newFontSize, elementHeight);

            //Set font settings to draw it correctly.
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
            var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 1.45);
            ctx.font = fontSizeToUse + "px " + fontStyle;
            ctx.fillStyle = color;

            //Draw text in center
            ctx.fillText(txt, centerX, centerY);
          }
        }
      });
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

        this.chart.options.elements.center.text = Math.round(newValue) + '%';
        this.chart.options.elements.center.color = this[this.getChartColor(newValue)];
        console.log(newValue);

        this.chart.update();
      },
    },
  },
  mounted() {
    this.addCenterTextOnDonutChart();

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
        elements: {
          center: {
            text: Math.round(this.dataset) + '%',
            color: this[this.getChartColor(this.dataset)],
            fontStyle: 'Helvetica',
            sidePadding: 40,
          },
        },
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