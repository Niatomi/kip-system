export default {
  async GET_DEVICE_POOL_BY_ID_TO_CHOSE ({commit, state, dispatch}, deviceId) {
    await dispatch('GET_DEVICE_POOL_BY_ID_TO_CHOSE_API', {deviceId: deviceId});
    return true;
  },
  
};
