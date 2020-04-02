import Vue from 'vue';
import Vuex from 'vuex';
import { cloneDeep } from 'lodash';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cpuLoad: [],
    cpuCoresLoad: [],
    cpuTemperatures: [],
    gpuLoad: [],
    gpuRamLoad: 0,
    gpuTemperatures: [],
    ramLoad: 0,
    ssd1Name: '',
    ssd1UsedSpace: 0,
    ssd2UsedSpace: 0,
    hdd1UsedSpace: 0,
    time: [],
  },
  actions: {
    updateData({ commit }, data) {
      commit('updateData', data);
    },
  },
  mutations: {
    updateData(state, data) {
      state.cpuLoad = cloneDeep(data.cpu.load);
      state.cpuCoresLoad = cloneDeep(data.cpu.coresLoad);
      state.cpuTemperatures = cloneDeep(data.cpu.temperatures);

      state.gpuLoad = cloneDeep(data.gpu.load);
      Vue.set(state, 'gpuRamLoad', data.gpu.ramLoad);
      state.gpuTemperatures = cloneDeep(data.gpu.temperatures);

      Vue.set(state, 'ramLoad', data.ram.load);

      Vue.set(state, 'ssd1Name', data.ssd1.name);
      Vue.set(state, 'ssd1UsedSpace', data.ssd1.usedSpace);
      Vue.set(state, 'ssd2Name', data.ssd2.name);
      Vue.set(state, 'ssd2UsedSpace', data.ssd2.usedSpace);
      Vue.set(state, 'hddd1Name', data.hdd1.name);
      Vue.set(state, 'hdd1UsedSpace', data.hdd1.usedSpace);

      state.time = cloneDeep(data.time);
    },
  },
});

