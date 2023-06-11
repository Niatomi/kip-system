import actions from "./actions/actions";
import api_actions from "./actions/api_requests";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";

const const_actions = { ...actions, ...api_actions };

export default {
  state: {
    accessHeader: {},
    isLoggedIn: Boolean,
    current_user: {},
    cookieAccepted: false
  },
  mutations,
  actions: const_actions,
  getters,
};