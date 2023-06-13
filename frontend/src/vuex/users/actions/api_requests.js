import axios from "axios";
import { toRaw } from 'vue'

export default {
  GET_API_USER_ROLES({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/users/roles', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_USER_ROLES', response.data)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_ALL_USERS({commit, state, dispatch, rootState}) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/users/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
    })
    .then((response) => {
      commit('SET_USERS', response.data.items)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  GET_USERS_BY_ROLE({commit, state, dispatch, rootState}, role) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/users/', {
      method: "GET",
      headers: toRaw(rootState.auth.accessHeader),
      params: {'role': role}
    })
    .then((response) => {
      commit('SET_USERS', response.data.items)
      return response.data;
    })
    .catch((error) => {
      return error;
    })
  },
  SIGN_UP_USER({commit, state, dispatch, rootState}, data) {
    return axios(process.env.VUE_APP_ROOT_API+'/v1/users', {
      method: "POST",
      headers: toRaw(rootState.auth.accessHeader),
      data: data
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      return error;
    })
  },
  
  
  
} 