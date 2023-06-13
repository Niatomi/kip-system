export default {
  SET_POOL_DEVICES_TO_STATE: (state, devices) => {
    state.devices_pool = devices;
  },
  SET_POOL_DEVICE_TO_CHOSE: (state, device) => {
    state.chosenDevice = device;
  },
  
};
