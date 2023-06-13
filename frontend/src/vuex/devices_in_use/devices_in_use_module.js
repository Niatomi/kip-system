import actions from "./actions/actions";
import api_actions from "./actions/api_requests";
import mutations from "./mutations/mutations";
import getters from "./getters/getters";

import { createStore, mapGetters } from "vuex";

const const_actions = { ...actions, ...api_actions };

export default {
  state: {
    currentDevicePage: 1,
    allDevicesPage: [],
    allDevicesInfo: [],

    popupChosenDevice: {},

    availableCategories: [],
    categorizedDevices: [],

    avaialableStatuses: [],
    devicesByStatus: [],

    availablePlaces: [],
    devicesByPlace: [],
    
    availableResposibles: [],
    devicesByPerson: [],

    availableSpecifications: [],
    devicesBySpecifications: [],

    allUsers: [],
    devicesToAdd: []
    
  },
  mutations,
  actions: const_actions,
  getters,
};
