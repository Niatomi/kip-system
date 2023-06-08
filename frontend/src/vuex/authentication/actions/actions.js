export default {
    SET_COOKIES ({commit, state, dispatch}) {
        commit('SET_COOKIE_DATA')
        if (state.isLoggedIn) {
            dispatch('GET_CURRENT_USER');
        }
    },
};
