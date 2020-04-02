<template>
  <div id="app" class="pa-0">
    <v-app>
      <v-content>
        <Dashboard />
      </v-content>
    </v-app>
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
  #app {
    background: #0f1011;
  }

  body::-webkit-scrollbar {
    display: none;
  }
</style>
