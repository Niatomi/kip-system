import axios from "axios";
const qs = require('qs');

export default {
    SET_LOGIN({commit}, data) {
        console.log(qs.stringify(data))
      return axios('http://localhost/v1/auth/sign_in', {
        method: "POST",
        data : qs.stringify(data)
      })
        .then((token_data) => {
          commit('SET_ACCESS_TOKEN_TO_STATE', token_data);
          return token_data;
        })
        .catch((error) => {
          console.log(error)
          return error;
        })
    }, 
} 