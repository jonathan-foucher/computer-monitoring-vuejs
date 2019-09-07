<template>
  <div class="hello">
    <svg id="svg-graphique" viewBox="0 0 900 600" />
  </div>
</template>

<script>
// d3 imports
import * as d3 from "d3-selection";
import * as d3Scale from "d3-scale";
import * as d3Shape from "d3-shape";
import * as d3Array from "d3-array";
import * as d3Axis from "d3-axis";
import * as d3Time from "d3-time-format";

import localFrJSON from "@/assets/fr-FR.json";

export default {
  name: "HelloWorld",
  data() {
    return {
      localFr: localFrJSON,
      margin: {
        top: 20,
        right: 20,
        bottom: 30,
        left: 50
      },
      width: 0,
      height: 0,
      svg: 0,
      x: 0,
      y: 0,
      graph: 0,
      line: 0,
      xDomain: 0,
      yDomain: 0,
      xScale: 0,
      yScale: 0,
      area: 0
    };
  },
  props: {
    temperatureGpuProp: Array
  },
  watch: {
    temperatureGpuProp: function(val) {
      this.svg.remove();
      this.initGraph();
    }
  },
  methods: {
    initGraph() {
      this.width = 500 - this.margin.left - this.margin.right;
      this.height = 200 - this.margin.top - this.margin.bottom;

      this.svg = d3
        .selectAll("#svg-graphique")
        .append("g")
        .attr(
          "transform",
          "translate(" + this.margin.left + "," + this.margin.top + ")"
        );

      this.area = d3Shape
        .area()
        .x(d => this.x(d.time))
        .y0(this.height)
        .y1(d => this.y(d.value));

      d3Time.timeFormatDefaultLocale(this.localFr);

      this.x = d3Scale.scaleTime().range([0, this.width]);
      this.y = d3Scale.scaleLinear().range([this.height, 0]);
      this.x.domain(d3Array.extent(this.temperatureGpuProp, d => d.time));
      this.y.domain([30, 80]);

      this.svg
        .append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + this.height + ")")
        .call(
          d3Axis
            .axisBottom(this.x)
            .ticks(6)
            .tickFormat(d3Time.timeFormat("%H:%M:%S"))
        )
        .append("text")
        .attr("class", "axis-title")
        .attr("y", -10)
        .attr("dx", "84.0em")
        .style("text-anchor", "end")
        .text("Date");

      this.svg
        .append("g")
        .attr("class", "axis axis--y")
        .call(d3Axis.axisLeft(this.y).ticks(null, "s"))
        .append("text")
        .attr("class", "axis-title")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Temperature");

      this.svg
        .append("path")
        .data([this.temperatureGpuProp])
        .style("fill", "steelblue")
        .style("fill-opacity", 0.3)
        .style("stroke", "none")
        .attr("d", this.area)
        .attr("class", "data");

      this.line = d3Shape
        .line()
        .x(d => this.x(d.time))
        .y(d => this.y(d.value));

      this.svg
        .append("path")
        .data([this.temperatureGpuProp])
        .style("fill", "none")
        .style("stroke", "steelblue")
        .style("stroke-width", "1.5px")
        .attr("d", this.line)
        .attr("class", "data");
    }
  },
  mounted() {
    this.initGraph();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

/* chart css style */
.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

.area {
  fill: steelblue;
  stroke: none;
  opacity: 0.3;
}

.zeroline {
  fill: none;
  stroke: red;
  stroke-width: 0.5px;
  stroke-dasharray: 5 5;
}

.zerolinetext {
  fill: red;
}

.circle {
  fill: white;
  stroke: steelblue;
  stroke-width: 2px;
}
</style>
