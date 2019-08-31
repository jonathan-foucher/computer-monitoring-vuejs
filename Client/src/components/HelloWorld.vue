<template>
  <div class="hello">
    <h1>{{ this.$vnode.key }}</h1>
    <h1>{{ apiResponse }}</h1>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      apiResponse: ""
    };
  },
  mounted() {
    const axios = require("axios");
    axios
      .get("http://localhost:3000/url")
      .then(response => (this.apiResponse = response.data));
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
</style>
