import axios from "axios";
const qs = require('qs');

export default {
    SET_LOGIN({commit}, data) {
      console.log(process.env.VUE_APP_ROOT_API);
      return axios(process.env.VUE_APP_ROOT_API+'/v1/auth/sign_in', {
        method: "POST",
        data : qs.stringify(data)
      }).then((token_data) => {
          commit('SET_ACCESS_TOKEN_TO_STATE', token_data);
          return token_data;
        })
        .catch((error) => {
          return error;
        })
    }, 
    GET_CURRENT_USER({commit, state}) {
      return axios(process.env.VUE_APP_ROOT_API+'/v1/users/me', {
        method: "GET",
        headers: state.accessHeader
      }).then((user) => {
        commit('SET_CURRENT_USER', user);
      }).error((error) => {
      })
    }
} 