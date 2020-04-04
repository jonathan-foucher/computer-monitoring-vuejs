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

      <v-col cols="4">
        <DonutChart
          dataStateName="gpuRamLoad"
          name="gpu-ram-load"
          :title="['GPU RAM load %', '', '']"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>

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
      <v-col cols="3">
        <DisksComponent />
      </v-col>
      <v-col cols="0.5" />

      <v-col cols="4" justify="center" align="center">
        <br>
        <span id="date">
          {{ datenow | formatDate }}
        </span>
        <br>
        <span id="time">
          {{ datenow | formatTime }}
        </span>
      </v-col>
      
      <v-col cols="4">
        <DonutChart
          dataStateName="ramLoad"
          name="ram-load"
          :title="['RAM load %', '', '']"
          :colorsLimits="[
            { color: 'green', value: 0},
            { color: 'yellow', value: 60},
            { color: 'orange', value: 75},
            { color: 'red', value: 90},
          ]" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import LineChart from './charts/LineChart';
import DonutChart from './charts/DonutChart';
import RadarChart from './charts/RadarChart';
import DisksComponent from './DisksComponent';

export default {
  name: 'Dashboard',
  components: {
    LineChart,
    DonutChart,
    RadarChart,
    DisksComponent,
  },
  mounted() {
    setInterval(() => { this.datenow = Date.now() }, 1000);
  },
  data() {
    return {
      datenow: Date.now(),
    }
  },
  watch : {
    datenow() {},
  },
  filters: {
    formatDate(date) {
      let temp = new Date(date);
      return temp.toLocaleString('en-GB', { year: 'numeric', month: 'long', day: '2-digit' });
    },
    formatTime(time) {
      let temp = new Date(time);
      return temp.toLocaleTimeString('en-GB', {hour: '2-digit', minute: '2-digit', second: '2-digit'});
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