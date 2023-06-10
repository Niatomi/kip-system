import actions from "./actions/actions";
import api_actions from "./actions/api_requests";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";

import { createStore, mapGetters } from "vuex";

const const_actions = { ...actions, ...api_actions };

let device_pool_module = createStore({
  state: {},
  mutations,
  actions: const_actions,
  getters,
});

export default device_pool_module;
