import cookie from 'vue-cookies'

export default {
    SET_COOKIES ({commit, state, dispatch}) {
        commit('SET_COOKIE_DATA');
        if (state.isLoggedIn) {
            dispatch('REFRESH_ACCESS_TOKEN');
            dispatch('SET_CURRENT_USER')
        }
        return true;
    },
    SET_ACCEPT_ON_COOKIE({state}) {
        state.cookieAccepted = true
        cookie.set('cookieAccepted', true)
    },
    LOGOUT({commit}) {
        commit('REMOVE_COOKIE_AUTH');
        return true;
    }
};
