<template>
  <div id="app">
    <b-container fluid>
      <b-row>
        <b-col>
          <LineChart
            ref="svg-graph-1'"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-1'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Temperature'"
          />
        </b-col>
        <b-col>
          <LineChart
            ref="svg-graph-2"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-2'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Temperature2'"
          />
        </b-col>
        <b-col>
          <LineChart
            ref="svg-graph-3"
            v-if="temperatureGpuProp.length > 1"
            :chartID="'svg-graph-3'"
            :dataReceived="temperatureGpuProp"
            :title="'GPU Temperature3'"
          />
        </b-col>
      </b-row>
    </b-container>
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

        while (
          temperatureGpuProp.length > 1 &&
          timeValueReceived - temperatureGpuProp[0].time > 59000
        ) {
          temperatureGpuProp.shift();
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
.col {
  flex: 1 0 30%;
}
</style>