export default {
  async GET_USER_ROLES({dispatch}) {
    await dispatch('GET_API_USER_ROLES')
  }
};
