<template>
  <div id="app" class="pa-0">
    <Dashboard />
  </div>
</template>

<script>
import Dashboard from "./components/Dashboard";

export default {
  name: 'App',
  components: {
    Dashboard,
  },
  created() {
    this.sockets.subscribe('data', data => {
      this.$store.dispatch('updateData', JSON.parse(data));
    });
  }
}
</script>

<style>
  body {
    background: #1d2022;
  }

  body::-webkit-scrollbar {
    display: none;
  }
</style>
