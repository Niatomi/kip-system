export default {
  async GET_DEVICE_FULL_INFO ({commit, state, dispatch}, deviceId) {
    await dispatch('GET_DEVICE_BY_ID', {deviceId: deviceId})
    await dispatch('GET_DEVICE_AMMORTIZATION_BY_ID', {deviceId: deviceId})
    await dispatch('GET_DEVICE_TIME_IN_USE_BY_ID', {deviceId: deviceId})
    await dispatch('GET_DEVICE_RESOURCE_UNTIL_CHECK', {deviceId: deviceId})
    return true;
  },
  
  async GET_AVAILABLE_RESPONSIBLES_ACTION({commit, state, dispatch}) {
    let responsibles_ids = [];
    await dispatch('GET_AVAILABLE_RESPONSIBLES').then((result) => {
      responsibles_ids = result;
    })
    await commit('SET_CLEAR_ON_RESPONSIBLES');
    await dispatch('GET_DETAILED_INFO_ABOUT_RESPONSIBLE', responsibles_ids)
  },

  CLEAR_SPECIFICATION_DEVICES({commit}) {
    commit('SET_CLEAR_BY_SPECIFICATION')
  }
};


