<template>
  <v-container fluid>
      <v-row>
        <v-col>
          <LineChart name="test1" title="test1"/>
        </v-col>
        <v-col>
          <DonutChart name="test2" title="test2"/>
        </v-col>
        <v-col>
         <RadarChart name="test3" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <LineChart name="test4" />
        </v-col>
        <v-col>
          <LineChart name="test5" />
        </v-col>
        <v-col>
          <LineChart name="test6" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <LineChart name="test7" />
        </v-col>
        <v-col>
          <LineChart name="test8" />
        </v-col>
        <v-col>
          <LineChart name="test9" />
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import LineChart from './charts/LineChart';
import DonutChart from './charts/DonutChart';
import RadarChart from './charts/RadarChart';

export default {
  name: 'Dashboard',
  components: {
    LineChart,
    DonutChart,
    RadarChart,
  },
}
</script>

<style scoped>
</style>