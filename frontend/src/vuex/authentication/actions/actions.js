export default {
    SET_COOKIES ({commit, state, dispatch}) {
        commit('SET_COOKIE_DATA');
        return state.isLoggedIn;
    },
};
