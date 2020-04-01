import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueSocketIO from 'vue-socket.io';
import store from './store'

Vue.config.productionTip = false;

Vue.use(new VueSocketIO({ connection: 'http://localhost:80' }));

new Vue({
  vuetify,
  store,
  render: h => h(App),
}).$mount('#app');