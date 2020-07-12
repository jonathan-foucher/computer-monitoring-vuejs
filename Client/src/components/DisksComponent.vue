<template>
  <div>
    <span class="graph-title">
      SSD/HDD used space %
    </span>
    <br />

    <v-progress-linear
      background-opacity="0.3"
      :background-color="grey"
      height="35px"
      :rounded="true"
      :value="ssd1UsedSpace"
      :color="getDiskColor(ssd1UsedSpace)"
    >
      <span class="text-progress-bar">
        {{ ssd1Name }} ({{ Math.round(ssd1UsedSpace) }} %)
      </span>
    </v-progress-linear>
    <br />

    <v-progress-linear
      background-opacity="0.3"
      :background-color="grey"
      height="35px"
      :rounded="true"
      :value="ssd2UsedSpace"
      :color="getDiskColor(ssd2UsedSpace)"
    >
      <span class="text-progress-bar">
        {{ ssd2Name }} ({{ Math.round(ssd2UsedSpace) }} %)
      </span>
    </v-progress-linear>
    <br />

    <v-progress-linear
      background-opacity="0.3"
      :background-color="grey"
      height="35px"
      :rounded="true"
      :value="hdd1UsedSpace"
      :color="getDiskColor(hdd1UsedSpace)"
    >
      <span class="text-progress-bar">
        {{ hddd1Name }} ({{ Math.round(hdd1UsedSpace) }} %)
      </span>
    </v-progress-linear>
  </div>
</template>

<script>
import { mapState } from "vuex";
import chartColorsMixin from "@/mixins/chartColorsMixin";

export default {
  mixins: [chartColorsMixin],
  computed: {
    ...mapState([
      "ssd1Name",
      "ssd1UsedSpace",
      "ssd2Name",
      "ssd2UsedSpace",
      "hddd1Name",
      "hdd1UsedSpace",
    ]),
  },
  methods: {
    getDiskColor(value) {
      if (value >= 90) return this.getColorWithAlpha(this.red, 0.9);
      else if (value >= 75) return this.getColorWithAlpha(this.orange, 0.9);
      else if (value >= 60) return this.getColorWithAlpha(this.yellow, 0.9);

      return this.getColorWithAlpha(this.green, 0.9);
    },
  },
};
</script>

<style scoped>
.text-progress-bar {
  font-weight: 1000;
}

.graph-title {
  color: rgb(20, 150, 230);
  font-weight: bold;
  padding: 10px;
  font-size: 20px;
  font-family: "Arial";
  display: block;
  text-align: center;
}
</style>
