export default {
  async GET_PLANED_DEVICES({dispatch}) {
    await dispatch('GET_PLAN')
    await dispatch('GET_PLANED_DEVICES_API')
  },
  async GET_ON_CHECK_DEVICES({dispatch}) {
    await dispatch('GET_ON_CHECK')
    await dispatch('GET_ON_CHECKED_DEVICES_API')
  },
  
};
