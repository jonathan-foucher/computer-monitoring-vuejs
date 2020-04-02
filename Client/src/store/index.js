import Vue from 'vue';
import Vuex from 'vuex';
import { cloneDeep } from 'lodash';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cpuTemperatures: [],
    time: [],
  },
  actions: {
    updateData({ commit }, data) {
      commit('updateData', data);
    },
  },
  mutations: {
    updateData(state, data) {
      state.cpuTemperatures = cloneDeep(data.cpu.temperatures);
      state.time = cloneDeep(data.time);
    },
  },
});

