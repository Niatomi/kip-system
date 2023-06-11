export default {
  GET_DEVICE_FULL_INFO ({commit, state, dispatch}, deviceId) {
    // commit('SET_COOKIE_DATA');
    // if (state.isLoggedIn) {
    //     dispatch('REFRESH_ACCESS_TOKEN');
    //     dispatch('SET_CURRENT_USER')
    // }
    // return true;
    dispatch('GET_DEVICE_BY_ID', {deviceId: deviceId})
    dispatch('GET_DEVICE_AMMORTIZATION_BY_ID', {deviceId: deviceId})
    dispatch('GET_DEVICE_TIME_IN_USE_BY_ID', {deviceId: deviceId})
  },
};
