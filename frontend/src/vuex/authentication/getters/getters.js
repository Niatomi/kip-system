export default {
    USER(state) {
        return state.current_user;
    },
    IS_LOGGED_IN(state) {
        return state.isLoggedIn;
    },
    COOKIE_ACCEPTED(state) {
        return state.cookieAccepted
    }
};
