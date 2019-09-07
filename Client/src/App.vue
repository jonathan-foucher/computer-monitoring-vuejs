<template>
  <div id="app">
    <HelloWorld ref="graphComponent" :temperatureGpuProp="temperatureGpuProp" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",
  components: {
    HelloWorld
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
        if (temperatureGpuProp.length == 0) {
          var dateTime;
          for (var i = -59; i < 0; i++) {
            dateTime = new Date(response.data.timestamp);
            temperatureGpuProp.push({
              time: dateTime.setSeconds(dateTime.getSeconds() + i),
              value: 0
            });
          }
        } else {
          temperatureGpuProp.shift();
        }

        temperatureGpuProp.push({
          time: new Date(response.data.timestamp),
          value: response.data.temperaturegpu
        });
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