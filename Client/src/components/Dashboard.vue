<template>
  <v-container fluid>
    <!-- CPU -->
    <v-row  justify="center" align="center">
      <v-col>
        <LineChart 
          dataStateName="cpuLoad"
          name="cpu-usage"
          title="CPU load %"
          unit="%" />
      </v-col>
      <v-col cols='4.5'>
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
          unit="°C" />
      </v-col>
    </v-row>
    <!-- GPU -->
    <v-row justify="center" align="center">
      <v-col cols="4">
        <LineChart
          dataStateName="gpuLoad"
          name="gpu-usage"
          title="GPU load %"
          unit="%" />
      </v-col>
      <v-col cols="0.5" />
      <v-col cols="3">
        <DonutChart
          dataStateName="gpuRamLoad"
          name="gpu-ram-load"
          title="GPU RAM load %" />
      </v-col>
       <v-col cols="0.5" />
      <v-col cols="4">
        <LineChart
          dataStateName="gpuTemperatures"
          name="gpu-temperatures"
          title="GPU temperatures °C"
          unit="°C" />
      </v-col>
    </v-row>
    <!-- RAM / Disk -->
    <v-row  justify="center" align="center">
      <v-col cols="3">
        <DonutChart
          dataStateName="ramLoad"
          name="ram-load"
          title="RAM load %" />
      </v-col>
      <v-col cols="2">
        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          width="10px"
          :rounded="true"
          :value="ssd1UsedSpace"
          color="light-blue">{{ ssd1Name }} ({{ Math.round(ssd1UsedSpace) }} %)</v-progress-linear>

        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          :rounded="true"
          :value="ssd2UsedSpace"
          color="light-blue">{{ ssd2Name }} ({{ Math.round(ssd2UsedSpace) }} %)</v-progress-linear>

        <v-progress-linear
          background-opacity="0.3"
          height="35px"
          :rounded="true"
          :value="hdd1UsedSpace"
          color="light-blue">{{ hddd1Name }} ({{ Math.round(hdd1UsedSpace) }} %)</v-progress-linear>
      </v-col>
      <v-col>
        {{ datenow | formatTime }}
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from './charts/LineChart';
import DonutChart from './charts/DonutChart';
import RadarChart from './charts/RadarChart';
import { mapState } from 'vuex';
import "vuetify/dist/vuetify.min.css";

export default {
  name: 'Dashboard',
  components: {
    LineChart,
    DonutChart,
    RadarChart,
  },
  mounted() {
    setInterval(() => { this.datenow = Date.now() }, 1000);
  },
  data() {
    return {
      datenow: Date.now(),
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
    formatTime(time) {
      let temp = new Date(time);
      return temp.getHours() + ":" + temp.getMinutes() + ":" + temp.getSeconds();
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
  v-progress-linear {
    padding: 60px!important;
  }
</style>