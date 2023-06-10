import cookie from 'vue-cookies'
import router from '@/router/router'


export default {
    SET_ACCESS_TOKEN_TO_STATE: (state, token_data) => {
        state.isLoggedIn = true;
        state.token_type = token_data.data.token_type
        state.access_token = token_data.data.access_token
        state.accessHeader = {
            'Authorization': state.token_type + ' ' + state.access_token
        };
        cookie.remove('Authorization')
        cookie.set('Authorization', token_data.data.access_token)
        return true;
    },
    SET_COOKIE_DATA: (state) => {
        if (cookie.isKey('cookieAccepted')) {
            state.cookieAccepted = true
        }
        
        state.isLoggedIn = false;
        if (cookie.isKey('Authorization')) {
            state.token_type = 'Bearer'
            state.access_token = cookie.get('Authorization')
            state.accessHeader = {
                'Authorization': state.token_type + ' ' + state.access_token
            };
            state.isLoggedIn = true;
            router.push('/chiefPage');
        } 
        return state.isLoggedIn
    },
    SET_CURRENT_USER: (state, user) => {
        state.current_user = user;
        return user
    },
    REMOVE_COOKIE_AUTH: (state) => {
        cookie.remove('Authorization');
        state.isLoggedIn = false;
        state.current_user = {};
        return true;
    }
    
    
};
