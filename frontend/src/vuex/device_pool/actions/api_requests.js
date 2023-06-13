import axios from "axios";
const qs = require('qs');
import { toRaw } from 'vue'

export default {
  GET_POOL_DEVICES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/device_pool/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((devices) => {
      commit('SET_POOL_DEVICES_TO_STATE', devices.data.items);
      return devices.data;
    })
    .catch((error) => {
      return error;
    })
  },
  ADD_INTO_POOL_DEVICES({commit, state, dispatch, rootState}, data) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/device_pool/', {
      method: "POST",
      headers: toRaw(rootState.auth.accessHeader),
      data: toRaw(data)
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_POOL_BY_ID_TO_CHOSE_API({commit, state, dispatch, rootState}, deviceId) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/device_pool/device/' + deviceId, {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_POOL_DEVICE_TO_CHOSE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
} 