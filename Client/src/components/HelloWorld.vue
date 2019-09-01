<template>
  <div class="hello">
    <svg id="svg-graphique" viewBox="0 0 900 600" />
    <h1>{{ this.$vnode.key }}</h1>
    <h1>{{ apiResponse }}</h1>
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
      apiResponse: "",
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
      area: 0,
      dataGraph: [
        { time: new Date("2019-09-01 13:32:54"), value: 54 },
        { time: new Date("2019-09-01 13:32:55"), value: 55 },
        { time: new Date("2019-09-01 13:32:56"), value: 58 },
        { time: new Date("2019-09-01 13:32:57"), value: 59 },
        { time: new Date("2019-09-01 13:32:58"), value: 61 },
        { time: new Date("2019-09-01 13:32:59"), value: 60 },
        { time: new Date("2019-09-01 13:33:00"), value: 59 },
        { time: new Date("2019-09-01 13:33:01"), value: 62 },
        { time: new Date("2019-09-01 13:33:02"), value: 65 },
        { time: new Date("2019-09-01 13:33:03"), value: 67 },
        { time: new Date("2019-09-01 13:33:04"), value: 62 },
        { time: new Date("2019-09-01 13:33:05"), value: 68 },
        { time: new Date("2019-09-01 13:33:06"), value: 70 },
        { time: new Date("2019-09-01 13:33:07"), value: 73 },
        { time: new Date("2019-09-01 13:33:08"), value: 75 },
        { time: new Date("2019-09-01 13:33:09"), value: 76 },
        { time: new Date("2019-09-01 13:33:10"), value: 76 },
        { time: new Date("2019-09-01 13:33:11"), value: 76 },
        { time: new Date("2019-09-01 13:33:12"), value: 77 },
        { time: new Date("2019-09-01 13:33:13"), value: 79 },
        { time: new Date("2019-09-01 13:33:14"), value: 76 },
        { time: new Date("2019-09-01 13:33:15"), value: 72 },
        { time: new Date("2019-09-01 13:33:16"), value: 68 },
        { time: new Date("2019-09-01 13:33:17"), value: 67 },
        { time: new Date("2019-09-01 13:33:18"), value: 65 },
        { time: new Date("2019-09-01 13:33:19"), value: 66 },
        { time: new Date("2019-09-01 13:33:20"), value: 64 },
        { time: new Date("2019-09-01 13:33:21"), value: 62 },
        { time: new Date("2019-09-01 13:33:22"), value: 60 },
        { time: new Date("2019-09-01 13:33:23"), value: 58 },
        { time: new Date("2019-09-01 13:33:24"), value: 54 },
        { time: new Date("2019-09-01 13:33:25"), value: 55 },
        { time: new Date("2019-09-01 13:33:26"), value: 54 },
        { time: new Date("2019-09-01 13:33:27"), value: 55 },
        { time: new Date("2019-09-01 13:33:28"), value: 55 },
        { time: new Date("2019-09-01 13:33:29"), value: 55 },
        { time: new Date("2019-09-01 13:33:30"), value: 56 },
        { time: new Date("2019-09-01 13:33:31"), value: 55 },
        { time: new Date("2019-09-01 13:33:32"), value: 55 },
        { time: new Date("2019-09-01 13:33:33"), value: 54 },
        { time: new Date("2019-09-01 13:33:34"), value: 54 },
        { time: new Date("2019-09-01 13:33:35"), value: 54 },
        { time: new Date("2019-09-01 13:33:36"), value: 54 },
        { time: new Date("2019-09-01 13:33:37"), value: 55 },
        { time: new Date("2019-09-01 13:33:38"), value: 56 },
        { time: new Date("2019-09-01 13:33:39"), value: 58 },
        { time: new Date("2019-09-01 13:33:40"), value: 60 },
        { time: new Date("2019-09-01 13:33:41"), value: 62 },
        { time: new Date("2019-09-01 13:33:42"), value: 61 },
        { time: new Date("2019-09-01 13:33:43"), value: 64 },
        { time: new Date("2019-09-01 13:33:44"), value: 67 },
        { time: new Date("2019-09-01 13:33:45"), value: 64 },
        { time: new Date("2019-09-01 13:33:46"), value: 68 },
        { time: new Date("2019-09-01 13:33:47"), value: 73 },
        { time: new Date("2019-09-01 13:33:48"), value: 76 },
        { time: new Date("2019-09-01 13:33:49"), value: 78 },
        { time: new Date("2019-09-01 13:33:50"), value: 79 },
        { time: new Date("2019-09-01 13:33:51"), value: 80 },
        { time: new Date("2019-09-01 13:33:52"), value: 81 },
        { time: new Date("2019-09-01 13:33:53"), value: 76 }
      ]
    };
  },
  methods: {
    initGraph() {
      console.log(this.dataGraph);
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
      this.x.domain(d3Array.extent(this.dataGraph, d => d.time));
      this.y.domain(d3Array.extent(this.dataGraph, d => d.value));

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
        .datum(this.dataGraph)
        .style("fill", "steelblue")
        .style("fill-opacity", 0.3)
        .style("stroke", "none")
        .attr("d", this.area);

      this.line = d3Shape
        .line()
        .x(d => this.x(d.time))
        .y(d => this.y(d.value));

      this.svg
        .append("path")
        .datum(this.dataGraph)
        .style("fill", "none")
        .style("stroke", "steelblue")
        .style("stroke-width", "1.5px")
        .attr("d", this.line);
    }
  },
  mounted() {
    const axios = require("axios");
    /*axios
      .get("http://localhost:3000/url")
      .then(response => (this.apiResponse = response.data));*/

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
