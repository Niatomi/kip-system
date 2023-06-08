import cookie from 'vue-cookies'
export default {
    SET_ACCESS_TOKEN_TO_STATE: (state, token_data) => {
        state.isLoggedIn = true;
        state.accessHeader = {
            'Authorization': token_data.data.token_type + ' ' + token_data.data.access_token
        };
        cookie.set('Authorization', token_data.data.access_token, "7d")
    },
    SET_COOKIE_DATA: (state) => {
        state.isLoggedIn = false;
        if (cookie.isKey('Authorization')) {
            state.accessHeader = {
                'Authorization': cookie.get('Authorization')
            };
            state.isLoggedIn = true;
        } 
        return state.isLoggedIn
    }
};
