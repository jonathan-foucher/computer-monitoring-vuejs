<template>
  <div id="app">
    <LineChart ref="graphComponent" v-if="temperatureGpuProp.length > 1" :dataReceived="temperatureGpuProp" />
  </div>
</template>

<script>
import LineChart from "./components/LineChart";

export default {
  name: "App",
  components: {
    LineChart
  },
  data() {
    return {
      temperatureGpuProp: []
    };
  },
  methods: {
    updateGpuTemperature() {
      const axios = require("axios");

      axios.get("http://localhost:3000/getGpuInfo").then(response => {
        var timeValueReceived = new Date(response.data.timestamp);
        timeValueReceived.setMilliseconds(0);

        while (temperatureGpuProp.length > 1 && (timeValueReceived - temperatureGpuProp[0].time) > 59000) {
          temperatureGpuProp.shift();
        }

        if (temperatureGpuProp.length == 0 || temperatureGpuProp[temperatureGpuProp.length - 1].time.getSeconds() != timeValueReceived.getSeconds()) {
          temperatureGpuProp.push({
            time: timeValueReceived,
            value: response.data.temperaturegpu
          });
        }
      });
    }
  },
  created: function() {
    const cron = require("node-cron");
    global.component = this;
    global.temperatureGpuProp = this.temperatureGpuProp;

    cron.schedule("* * * * * *", function() {
      component.updateGpuTemperature();
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>