import axios from "axios";
import { toRaw } from 'vue'

export default {
  GET_PLAN({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/next_check', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_PLAN_TO_STATE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_PLANED_DEVICES_API({commit, state, dispatch, rootState}) {
    commit('CLEAR_PLANNED_DEVICE')
    state.plan.forEach(value => {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+value.device_id, {
        method: "GET",
        headers: toRaw(rootState.auth.accessHeader),
      })
      .then((response) => {
        response.data['next_check_time'] = value.next_check_time
        commit('PUSH_PLANNED_DEVICE_TO_STATE', response.data)
        return response.data;
      })
      .catch((error) => {
        return error;
      })
    })
  },
  GET_ON_CHECKED_DEVICES_API({commit, state, dispatch, rootState}) {
    commit('CLEAR_ON_CHECKED_DEVICES')
    state.on_check_list.forEach(value => {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/device/'+value, {
        method: "GET",
        headers: toRaw(rootState.auth.accessHeader),
      })
      .then((response) => {
        console.log(value);
        commit('PUSH_ON_CHECKED_DEVICE_TO_STATE', response.data)
        return response.data;
      })
      .catch((error) => {
        return error;
      })
    })
  },
  GET_ON_CHECK({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/devices_in_use/on_check', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('PUSH_ON_STATE_TO_STATE', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  
} 