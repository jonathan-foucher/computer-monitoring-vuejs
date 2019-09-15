<template>
  <div id="app">
    <b-container fluid>
      <b-row>
        <b-col>
          <LineChart
            ref="svg-graph-gpu-usage"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-gpu-usage'"
            :dataReceived="usageGpuProp"
            :title="'GPU usage %'"
            :yScaling="'%'"
          />
        </b-col>
        <b-col>
          <DonutChart
            ref="svg-graph-gup-ram-usage'"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-gup-ram-usage'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Ram usage %'"
          />
        </b-col>
        <b-col>
          <LineChart
            ref="svg-graph-gpu-temp"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-gpu-temp'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Temperature'"
            :yScaling="'auto'"
          />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import LineChart from "./components/LineChart";
import DonutChart from "./components/DonutChart";

export default {
  name: "App",
  components: {
    LineChart,
    DonutChart
  },
  data() {
    return {
      temperatureGpuProp: [],
      usageGpuProp: []
    };
  },
  methods: {
    updateGpuInfo() {
      const axios = require("axios");

      axios.get("http://localhost:3000/getGpuInfo").then(response => {
        // extract gpu info
        var timeValueReceived = new Date(response.data.timestamp);
        timeValueReceived.setMilliseconds(0);

        while (
          temperatureGpuProp.length > 1 &&
          timeValueReceived - temperatureGpuProp[0].time > 59000
        ) {
          temperatureGpuProp.shift();
          usageGpuProp.shift();
        }

        if (
          temperatureGpuProp.length == 0 ||
          temperatureGpuProp[temperatureGpuProp.length - 1].time.getSeconds() !=
            timeValueReceived.getSeconds()
        ) {
          temperatureGpuProp.push({
            time: timeValueReceived,
            value: response.data.temperaturegpu
          });

          usageGpuProp.push({
            time: timeValueReceived,
            value: parseInt(response.data.utilizationgpu.substr(0, response.data.utilizationgpu.length - 2))
          });
        }
      });
    }
  },
  created: function() {
    const cron = require("node-cron");
    global.component = this;
    global.temperatureGpuProp = this.temperatureGpuProp;
    global.usageGpuProp = this.usageGpuProp;

    cron.schedule("* * * * * *", function() {
      component.updateGpuInfo();
    });
  }
};
</script>

<style>
</style>