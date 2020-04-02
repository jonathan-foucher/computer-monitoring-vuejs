<template>
  <v-container fluid>
    <!-- CPU -->
    <v-row  justify="center" align="center">
      <v-col>
        <LineChart 
          dataStateName="cpuLoad"
          name="cpu-load"
          title="CPU load %"
          unit="%"
          :useAvgForColor="true"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>
      <v-col cols="4.5">
        <RadarChart
          dataStateName="cpuCoresLoad"
          name="cores-load"
          title="CPU cores load %" />
      </v-col>
      <v-col>
        <LineChart
          dataStateName="cpuTemperatures"
          name="cpu-temperatures"
          title="CPU temperatures °C"
          unit="°C"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 50},
            { color: 'orange', value: 60},
            { color: 'red', value: 70},
          ]" />
      </v-col>
    </v-row>
    <!-- GPU -->
    <v-row justify="center" align="center">
      <v-col cols="4">
        <LineChart
          dataStateName="gpuLoad"
          name="gpu-usage"
          title="GPU load %"
          unit="%"
          :useAvgForColor="true"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>
      <v-col cols="0.5" />
      <v-col cols="3">
        <DonutChart
          dataStateName="gpuRamLoad"
          name="gpu-ram-load"
          title="GPU RAM load %"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>
       <v-col cols="0.5" />
      <v-col cols="4">
        <LineChart
          dataStateName="gpuTemperatures"
          name="gpu-temperatures"
          title="GPU temperatures °C"
          unit="°C"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 70},
            { color: 'red', value: 80},
          ]" />
      </v-col>
    </v-row>
    <!-- RAM / Disk -->
    <v-row  justify="center" align="center">
      <v-col cols="0.5" />
      <v-col cols="4">
        <DonutChart
          dataStateName="ramLoad"
          name="ram-load"
          title="RAM load %"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>
      <v-col cols="0.5" />
      <v-col cols="2">
        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          width="10px"
          :rounded="true"
          :value="ssd1UsedSpace"
          :color="getDiskColor(ssd1UsedSpace)">
            <font :color="`blue`">
              {{ ssd1Name }} ({{ Math.round(ssd1UsedSpace) }} %)
            </font>
          </v-progress-linear>
        <br>
        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          :rounded="true"
          :value="ssd2UsedSpace"
          :color="getDiskColor(ssd2UsedSpace)">
            <font :color="`blue`">
              {{ ssd2Name }} ({{ Math.round(ssd2UsedSpace) }} %)
            </font>
          </v-progress-linear>
        <br>
        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          :rounded="true"
          :value="hdd1UsedSpace"
          :color="getDiskColor(hdd1UsedSpace)">
            <font :color="`blue`">
              {{ hddd1Name }} ({{ Math.round(hdd1UsedSpace) }} %)
            </font>
          </v-progress-linear>
      </v-col>
      <v-col cols="1" />
      <v-col cols="4" justify="center" align="center">
        <span id="date">
          {{ datenow | formatDate }}
        </span>
        <br>
        <span id="time">
          {{ datenow | formatTime }}
        </span>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from './charts/LineChart';
import DonutChart from './charts/DonutChart';
import RadarChart from './charts/RadarChart';
import { mapState } from 'vuex';
import chartColorsMixin from '../mixins/chartColorsMixin';

export default {
  name: 'Dashboard',
  components: {
    LineChart,
    DonutChart,
    RadarChart,
  },
  mixins: [chartColorsMixin],
  mounted() {
    setInterval(() => { this.datenow = Date.now() }, 1000);
  },
  data() {
    return {
      datenow: Date.now(),
    }
  },
  methods: {
    getDiskColor(value) {
      if(value >= 90)
        return this.getColorWithAlpha(this.red, 0.9);

      else if(value >= 75)
        return this.getColorWithAlpha(this.orange, 0.9);

      else if(value >= 60)
        return this.getColorWithAlpha(this.yellow, 0.9);

      return this.getColorWithAlpha(this.green, 0.9);
    }
  },
  computed: {
    ...mapState([
      'cpuTemperatures',
      'gpuTemperatures',
      'ssd1Name',
      'ssd1UsedSpace',
      'ssd2Name',
      'ssd2UsedSpace',
      'hddd1Name',
      'hdd1UsedSpace',
    ]),
  },
  watch : {
    datenow() {},
  },
  filters: {
    formatDate(date) {
      let temp = new Date(date);
      return (temp.getDay() < 10 ? '0' : '') + temp.getDay() + '/'
        + (temp.getMonth() < 10 ? '0' : '') + temp.getMonth() + '/'
        + temp.getFullYear();
    },
    formatTime(time) {
      let temp = new Date(time);
      return (temp.getHours() < 10 ? '0' : '') + temp.getHours() + ':'
        + (temp.getMinutes() < 10 ? '0' : '') + temp.getMinutes() + ':'
        + (temp.getSeconds() < 10 ? '0' : '') + temp.getSeconds();
    },
    calculateTemperaturesRange(temperatures) {
      return [
        Math.floor(Math.min(temperatures) + 5),
        Math.ceil(Math.max(temperatures) + 5)
      ];
    },
  }
}
</script>

<style scoped>
  #date {
    color: white;
    font-size: 2.5em;
  }

  #time {
    color: white;
    font-size: 5em;
  }
</style>