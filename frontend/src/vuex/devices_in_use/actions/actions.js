export default {
  async GET_DEVICE_FULL_INFO ({commit, state, dispatch}, deviceId) {
    await dispatch('GET_DEVICE_BY_ID', {deviceId: deviceId})
    await dispatch('GET_DEVICE_AMMORTIZATION_BY_ID', {deviceId: deviceId})
    await dispatch('GET_DEVICE_TIME_IN_USE_BY_ID', {deviceId: deviceId})
    return true;
  },
};
