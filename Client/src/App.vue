<template>
  <div id="app">
    <HelloWorld :key="keyvalue" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

export default {
  name: "App",
  components: {
    HelloWorld
  },
  data() {
    return {
      keyvalue: 0
    };
  },
  methods: {
    updateKey() {
      this.keyvalue += 1;
    }
  },
  created: function() {
    const cron = require("node-cron");
    global.component = this;
    cron.schedule("* * * * * *", function() {
      component.updateKey();
    });
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>