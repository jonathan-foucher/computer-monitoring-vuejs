<template>
  <div id="app" class="pa-0">
    <Dashboard />
  </div>
</template>

<script>
import Dashboard from "./components/Dashboard.vue";

export default {
  name: 'App',
  components: {
    Dashboard,
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
