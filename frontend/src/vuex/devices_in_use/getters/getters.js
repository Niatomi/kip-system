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
    return state.avaialableStatuses
  },
  DEVICES_BY_STATUS(state) {
    return state.devicesByStatus;
  }
};
