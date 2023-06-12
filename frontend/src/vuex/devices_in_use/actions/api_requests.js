import axios from "axios";
import { isProxy, toRaw } from 'vue';
const qs = require('qs');

export default {
  GET_ACTIVE_DEVICES_IN_PAGES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/pages', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((devices) => {
      commit('SET_ALL_DEVICES_TO_STATE', devices.data);
      dispatch('GET_DEVICE_FULL_INFO_IN_PAGES')
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_FULL_INFO_IN_PAGES({ commit, state, rootState }) {

    state.allDevicesPage.forEach(device => {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+device.id, {
        method: "GET",
        headers: toRaw(rootState.auth.accessHeader)
      })
      .then((device) => {
        commit('SET_ALL_INFO_INTO_ALL_DEVICES', device.data);
      })
      .catch((error) => {
        return error;
      })

    })
  },
  GET_DEVICE_BY_ID({ commit, state, rootState }, payload) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+payload.deviceId, {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((device) => {
      commit('SET_ALL_CHOSEN_DEVICE_TO_STATE', device.data);
      return device.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_AMMORTIZATION_BY_ID({ commit, state, rootState }, payload) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+payload.deviceId+'/ammortization', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((response) => {
      commit('SET_AMMORTIZATION', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_TIME_IN_USE_BY_ID({ commit, state, rootState }, payload) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+payload.deviceId+'/time_in_use', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((response) => {
      commit('SET_TIME_IN_USE', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_BY_SEARCH({commit, state, dispatch, rootState}, searchQuery) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/search', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params : {'name': searchQuery}
    })
    .then((devices) => {
      commit('SET_ALL_DEVICES_TO_STATE', devices.data);
      dispatch('GET_DEVICE_FULL_INFO_IN_PAGES');
      return devices.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_AVAILABLE_CATEGORIES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/categories', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_CATEGORIES_TO_STATE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICES_BY_CATEGORY({commit, state, dispatch, rootState}, category) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params : {'category': category}
    })
    .then((response) => {
      commit('SET_CATEGORIZED_DEVICES', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_AVAILABLE_STATUSES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/actions', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_STATUSES_TO_STATE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICES_BY_STATUS({commit, state, dispatch, rootState}, status) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params : {'action': status}
    })
    .then((response) => {
      commit('SET_STATUSED_DEVICES', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_AVAILABLE_PLACES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/places', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_PLACES_TO_STATE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICES_BY_PLACE({commit, state, dispatch, rootState}, place) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params : {'place': place}
    })
    .then((response) => {
      commit('SET_PLACED_DEVICES', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  
  
} 