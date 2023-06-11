
export default {
  SET_ALL_DEVICES_TO_STATE: (state, devices) => {
    state.allDevicesPage = []
    if (devices.hasOwnProperty('items')) {
      state.allDevicesPage.push(...devices.items)
      Object.assign(state.allChosenDeviceInfo,{...devices.items[0]});
    } else {
      state.allDevicesPage.push(...devices)
      Object.assign(state.allChosenDeviceInfo,{...devices[0]});
    }
    state.allDevicesInfo = []
  },
  SET_ALL_INFO_INTO_ALL_DEVICES: (state, device) => {
    state.allDevicesInfo.push(device)
  },
  SET_ALL_CHOSEN_DEVICE_TO_STATE: (state, device) => {
    Object.assign(state.allChosenDeviceInfo,{...device});
  },
  SET_AMMORTIZATION: (state, value) => {
    Object.assign(state.allChosenDeviceInfo, {'ammortization': value});
  },
  SET_TIME_IN_USE: (state, value) => {
    Object.assign(state.allChosenDeviceInfo, {'timeInUse': value});
  }
  
};
