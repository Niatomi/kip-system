export default {
  SET_PLAN_TO_STATE(state, plan) {
    state.plan = plan;
  },
  CLEAR_PLANNED_DEVICE(state) {
    state.planed_devices = [];
  },
  PUSH_PLANNED_DEVICE_TO_STATE(state, device) {
    state.planed_devices.push(device);
  },
  
  CLEAR_ON_CHECKED_DEVICES(state) {
    state.on_check_devices = [];
  },
  PUSH_ON_STATE_TO_STATE(state, devices) {
    state.on_check_list = [];
    state.on_check_list = devices;
  },
  PUSH_ON_CHECKED_DEVICE_TO_STATE(state, device) {
    state.on_check_devices.push(device);
  },
  
};
