export default {
  ALL_DEVICES_PAGE(state) {
    return state.allDevicesPage;
  },
  ALL_DEVICES_INFO(state) {
    return state.allDevicesInfo;
  },

  CHOSEN_DEVICE(state) {
    return state.popupChosenDevice;
  },

  AVAILABLE_CATEGORIES(state) {
    return state.availableCategories;
  },
  CATEGORIZED_DEVICES(state) {
    return state.categorizedDevices;
  },
  
  AVAILABLE_STATUSES(state) {
    return state.avaialableStatuses;
  },
  DEVICES_BY_STATUS(state) {
    return state.devicesByStatus;
  },

  AVAILABLE_PLACES(state) {
    return state.availablePlaces;
  },
  DEVICES_BY_PLACE(state) {
    return state.devicesByPlace;
  },
  
  AVAILABLE_RESPONSIBLES(state) {
    return state.availableResposibles;
  },
  DEVICES_BY_RESPONSIBLE(state) {
    return state.devicesByPerson;
  },

  AVAILABLE_SPECIFICATIONS(state) {
    return state.availableSpecifications;
  },
  DEVICES_BY_SPECIFICATIONS(state) {
    return state.devicesBySpecifications
  },

  ALL_USERS(state) {
    return state.allUsers;
  },
  DEVICE_POOL_ADD(state) {
    return state.devicesToAdd
  }
  
};
