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
  GET_DEVICE_RESOURCE_UNTIL_CHECK({ commit, state, rootState }, payload) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+payload.deviceId+'/remaining_resource_until_check', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader)
    })
    .then((response) => {
      commit('SET_DEVICE_RESOURCE_ON_NEXT_CHECK', response.data);
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

  GET_AVAILABLE_RESPONSIBLES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/reposponsible_persons', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DETAILED_INFO_ABOUT_RESPONSIBLE({commit, state, dispatch, rootState}, responsbiles) {

    responsbiles.forEach(responsbile => {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/users/'+responsbile, {
        method: "GET",
        headers: toRaw(rootState.auth.accessHeader),
      })
      .then((response) => {
        commit('SET_RESPONSBILE_TO_STATE', response.data)
        return response.data;
      })
      .catch((error) => {
        return error;
      })
    })
  },
  GET_DEVICES_BY_RESPONSIBLE({commit, state, dispatch, rootState}, responsible) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params : {'person_id': responsible.id}
    })
    .then((response) => {
      commit('SET_RESPONSIBLES_DEVICES', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  
  GET_AVAILABLE_SPECIFICATIONS({commit, state, dispatch, rootState}, responsible) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/specifications', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_SPECIFICATIONS_TO_STATE', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICES_BY_SPECIFICATIONS({commit, state, dispatch, rootState}, specificationsArray) {
    let rawParams = '';
    let spec = toRaw(specificationsArray)
    let isFirst = true;
    specificationsArray.forEach(value => {
      if (!isFirst) {
          rawParams += '&'
      }
      isFirst = false;
      rawParams += 'specifications=' + value
    })
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/by_specification?'+rawParams, {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_SPECIFICATED_DEVICES', response.data);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  
  GET_USERS({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/users/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_ALL_USERS', response.data.items);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_POOL_ADD({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/device_pool', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_DEVICE_POOL_ON_ADD', response.data.items);
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  ADD_ACTIVE_DEVICE({commit, state, dispatch, rootState}, data) {
    let selectedPersonId = data.selectedPersonId
    delete data.selectedPersonId
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use', {
      method: "POST",
      headers: toRaw(rootState.auth.accessHeader),
      params: {'responsible_person': selectedPersonId},
      data: data
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_NEXT_CHECK({commit, state, dispatch, rootState}, deviceId) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/' +deviceId+ '/on_check', {
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
  PATCH_NEW_DEVICE_STATUS({commit, state, dispatch, rootState}, payload) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/' +payload.deviceId, {
      method: "PATCH",
      headers: toRaw(rootState.auth.accessHeader),
      params: {'action': payload.deviceStatus}
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_DEVICE_STATUSES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/actions', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  
  
  
} 