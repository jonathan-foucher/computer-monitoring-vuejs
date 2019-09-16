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
            :limits="{ min: 0, max: 100, minR: 0, minG: 255, minB: 0, maxR: 255, maxG: 127, maxB: 0 }"
          />
        </b-col>
        <b-col>
          <DonutChart
            ref="svg-graph-gup-memory-usage"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-gup-memory-usage'"
            :dataReceived="usageGpuMemoryProp"
            :title="'GPU memory usage %'"
            :limits="{ min: 0, max: 100, minR: 0, minG: 255, minB: 0, maxR: 255, maxG: 127, maxB: 0 }"
          />
        </b-col>
        <b-col>
          <LineChart
            ref="svg-graph-gpu-temp"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-gpu-temp'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Temperature °C'"
            :yScaling="'auto'"
            :limits="{ min: 40, max: 70, minR: 0, minG: 255, minB: 0, maxR: 255, maxG: 0, maxB: 0 }"
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
      usageGpuProp: [],
      usageGpuMemoryProp: []
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

          usageGpuMemoryProp.length = 0;
          usageGpuMemoryProp.push(response.data.utilizationmemory.substr(0, response.data.utilizationmemory.length - 2));
          usageGpuMemoryProp.push(response.data.memoryused);
          usageGpuMemoryProp.push(response.data.memorytotal);
        }
      });
    }
  },
  created: function() {
    const cron = require("node-cron");
    global.component = this;
    global.temperatureGpuProp = this.temperatureGpuProp;
    global.usageGpuProp = this.usageGpuProp;
    global.usageGpuMemoryProp = this.usageGpuMemoryProp;

    cron.schedule("* * * * * *", function() {
      component.updateGpuInfo();
    });
  }
};
</script>

<style>
</style>