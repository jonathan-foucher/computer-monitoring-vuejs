<template>
  <v-container fluid>
      <v-row>
        <v-col>
          <LineChart chartName="test1" />
        </v-col>
        <v-col>
          <LineChart chartName="test2" />
        </v-col>
        <v-col>
         <LineChart chartName="test3" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <LineChart chartName="test4" />
        </v-col>
        <v-col>
          <LineChart chartName="test5" />
        </v-col>
        <v-col>
          <LineChart chartName="test6" />
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <LineChart chartName="test7" />
        </v-col>
        <v-col>
          <LineChart chartName="test8" />
        </v-col>
        <v-col>
          <LineChart chartName="test9" />
        </v-col>
      </v-row>
    </v-container>
</template>

<script>
import LineChart from './charts/LineChart'

export default {
  name: 'Dashboard',
  components: {
    LineChart,
  }
}
</script>

<style scoped>
</style>