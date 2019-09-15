<template>
  <div class="graph" style="background-color: #212121">
    <svg :id="chartID" width="100%" height="300" />
    <!--<h2>{{ title }}</h2>-->
  </div>
</template>

<script>
// d3 imports
import * as d3 from "d3-selection";
import * as d3Scale from "d3-scale";
import * as d3Shape from "d3-shape";
import * as d3Collection from "d3-collection";

export default {
  name: "DonutChart",
  data() {
    return {
      margin: { top: 25, right: 25, bottom: 25, left: 25 },
      width: 0,
      height: 0,
      svg: 0,
      graph: 0,
      line: 0
    };
  },
  props: {
    chartID: String,
    dataReceived: Array,
    title: String
  },
  watch: {
    dataReceived: function() {
      this.svg.remove();
      this.drawGraph();
    }
  },
  methods: {
    drawGraph() {
      // calcul the dimensions
      this.width = 287 - this.margin.left - this.margin.right;
      this.height = 200 - this.margin.top - this.margin.bottom;

      // define the graph area
      this.svg = d3
        .selectAll("#" + this.chartID)
        .append("g")
        .attr(
          "transform",
          "translate(" + (this.width / 2 + this.margin.left) + "," + (this.height / 2 + this.margin.top) + ")"
        );;

      const dataset = { val: this.dataReceived[0], remain: (100 - this.dataReceived[0]) };

      const color = d3Scale
        .scaleOrdinal()
        .domain(dataset)
        .range(["#4682B4", "#696969"]);

      const pie = d3Shape.pie().value(d => d.value).sort(null);

      const arc = d3Shape
        .arc()
        .innerRadius(60)
        .outerRadius(90);

      const part = this.svg
        .selectAll(".part")
        .data(pie(d3Collection.entries(dataset)))
        .enter()
        .append("g");

      part
        .append("path")
        .attr("d", arc)
        .attr("fill", (d, i) => color(i));

      /*part
        .append("text")
        .attr("transform", d => "translate(" + arc.centroid(d) + ")")
        .text(d => d.data.key)
        .attr("fill", "white");*/
    }
  },
  mounted() {
    this.drawGraph();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* chart css style */
  div {
    text-align: center
  }
</style>
