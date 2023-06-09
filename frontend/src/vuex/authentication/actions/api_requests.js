import axios from "axios";
const qs = require('qs');
import { isProxy, toRaw } from 'vue';

export default {
    SET_LOGIN({commit, dispatch}, data) {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/auth/sign_in', {
        method: "POST",
        data : qs.stringify(data)
      }).then((token_data) => {
          commit('SET_ACCESS_TOKEN_TO_STATE', token_data);
          dispatch('SET_CURRENT_USER')
          return token_data;
        })
        .catch((error) => {
          return error;
        })
    }, 
    SET_CURRENT_USER({commit, state}) {
      let accessHeader = state.accessHeader
      if (isProxy(state.accessHeader)) {
        accessHeader = toRaw(state.accessHeader)
      }

      return axios(process.env.VUE_APP_ROOT_API+'/v1/users/me', {
        method: "GET",
        headers: accessHeader
      }).then((user) => {
        console.log(user.data);
        commit('SET_CURRENT_USER', user.data);
      })
      .catch((error) => {
        return error;
      })
    },
    REFRESH_ACCESS_TOKEN({commit, state}) {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/auth/refresh_token', 
      {
        method: "PUT",
        data: {
          access_token: state.access_token,
          token_type: "Bearer"
        }
      })
      .then((token_data) => {
        commit('SET_ACCESS_TOKEN_TO_STATE', token_data);
      })
      .catch((error) => {
        return error;
      })
    }
} 