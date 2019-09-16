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
import * as d3Axis from "d3-axis";
import * as d3Time from "d3-time-format";

// local date format for french
import localFrJSON from "@/assets/fr-FR.json";

export default {
  name: "DonutChart",
  data() {
    return {
      localFr: localFrJSON,
      margin: { top: 25, right: 25, bottom: 25, left: 25 },
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
    chartID: String,
    dataReceived: Array,
    title: String,
    yScaling: String,
    limits: Object
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
      this.width = 620 - this.margin.left - this.margin.right;
      this.height = 200 - this.margin.top - this.margin.bottom;

      // define the graph area
      this.svg = d3
        .selectAll("#" + this.chartID)
        .append("g")
        .attr(
          "transform",
          "translate(" + this.margin.left + "," + this.margin.top + ")"
        );

      // get the area values
      this.area = d3Shape
        .area()
        .x(d => this.x(d.time))
        .y0(this.height)
        .y1(d => this.y(d.value));

      // french time format as default
      d3Time.timeFormatDefaultLocale(this.localFr);

      // define scales
      this.x = d3Scale.scaleTime().range([0, this.width]);
      this.y = d3Scale.scaleLinear().range([this.height, 0]);

      // calcul the x domain
      var lastTimeValue = this.dataReceived[this.dataReceived.length - 1].time;
      this.x.domain([
        new Date(lastTimeValue).setSeconds(lastTimeValue.getSeconds() - 59),
        new Date(lastTimeValue)
      ]);

      // calcul the y domain
      if (this.yScaling == "auto") {
        var minY = Math.min.apply(
          Math,
          this.dataReceived.map(function(o) {
            return parseInt(o.value) - 5;
          })
        );
        var maxY = Math.max.apply(
          Math,
          this.dataReceived.map(function(o) {
            return parseInt(o.value) + 5;
          })
        );
      } else if (this.yScaling == "%") {
        var minY = 0;
        var maxY = 100;
      }
      this.y.domain([minY, maxY]);

      // draw the x axis
      this.svg
        .append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + this.height + ")")
        .style("color", "white")
        .call(
          d3Axis
            .axisBottom(this.x)
            .ticks(0)
            .tickFormat(d3Time.timeFormat("%H:%M:%S"))
        );

      // draw the y axis
      this.svg
        .append("g")
        .attr("class", "axis axis--y")
        .style("color", "white")
        .call(d3Axis.axisLeft(this.y).ticks(2));

      // color calculation
      const lastValue = this.dataReceived[this.dataReceived.length - 1].value;
      
      let percent = ((lastValue - this.limits.min) / (this.limits.max - this.limits.min));

      if (percent > 1) {
        percent = 1;
      }

      const red = this.calculateColor(
        this.limits.minR,
        this.limits.maxR,
        percent
      );
      const green = this.calculateColor(
        this.limits.minG,
        this.limits.maxG,
        percent
      );
      const blue = this.calculateColor(
        this.limits.minB,
        this.limits.maxB,
        percent
      );

      // draw the area under the line
      this.svg
        .append("path")
        .data([this.dataReceived])
        .style("fill", "rgb(" + red + "," + green + "," + blue + ")")
        .style("fill-opacity", 0.35)
        .style("stroke", "none")
        .attr("d", this.area)
        .attr("class", "data");

      // get the line values
      this.line = d3Shape
        .line()
        .x(d => this.x(d.time))
        .y(d => this.y(d.value));

      // draw the line
      this.svg
        .append("path")
        .data([this.dataReceived])
        .style("fill", "none")
        .style("stroke", "rgb(" + red + "," + green + "," + blue + ")")
        .style("stroke-width", "1.5px")
        .attr("d", this.line)
        .attr("class", "data");
    },
    calculateColor(min, max, percent) {
      return parseInt(min + (max - min) * percent);
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
  stroke: none;
  opacity: 0.3;
}
</style>
