import actions from "./actions/actions";
import api_actions from "./actions/api_requests";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";


import { createStore, mapGetters } from "vuex";

const const_actions = { ...actions, ...api_actions };
export default {
  state: {
    planed_devices: [],
    plan: [],

    on_check_devices: [],
    on_check_list: [],
  },
  mutations,
  actions: const_actions,
  getters,
};
