import actions from "./actions/actions";
import api_actions from "./actions/api_requests";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";

const const_actions = { ...actions, ...api_actions };

export default {
  state: {
    devices_pool: [],
    chosenDevice: {}
  },
  mutations,
  actions: const_actions,
  getters,
};
