
export default {
  SET_ALL_DEVICES_TO_STATE: (state, devices) => {
    state.allDevicesPage = []
    if (devices.hasOwnProperty('items')) {
      state.allDevicesPage.push(...devices.items)
    } else {
      state.allDevicesPage.push(...devices)
    }
    state.allDevicesInfo = []
  },
  SET_ALL_INFO_INTO_ALL_DEVICES: (state, device) => {
    state.allDevicesInfo.push(device)
  },
  SET_ALL_CHOSEN_DEVICE_TO_STATE: (state, device) => {
    Object.assign(state.popupChosenDevice,{...device});
  },
  SET_AMMORTIZATION: (state, value) => {
    Object.assign(state.popupChosenDevice, {'ammortization': value});
  },
  SET_TIME_IN_USE: (state, value) => {
    Object.assign(state.popupChosenDevice, {'timeInUse': value});
  },
  

  SET_CATEGORIES_TO_STATE: (state, categories) => {
    state.availableCategories = [];
    state.availableCategories = categories;
  },
  SET_CATEGORIZED_DEVICES: (state, devices) => {
    state.categorizedDevices = [];
    state.categorizedDevices = devices;
  },
  
  SET_STATUSES_TO_STATE: (state, statuses) => {
    state.avaialableStatuses = [];
    state.avaialableStatuses = statuses;
  },
  SET_STATUSED_DEVICES: (state, devices) => {
      state.devicesByStatus = [];
      state.devicesByStatus = devices;
    },
  

};
