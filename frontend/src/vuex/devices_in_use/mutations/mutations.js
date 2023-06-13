
export default {
  SET_ALL_DEVICES_TO_STATE: (state, devices) => {
    state.allDevicesPage = []
    if (devices.hasOwnProperty('items')) {
      state.allDevicesPage.push(...devices.items);
    } else {
      state.allDevicesPage.push(...devices);
    }
    state.allDevicesInfo = [];
  },
  SET_ALL_INFO_INTO_ALL_DEVICES: (state, device) => {
    state.allDevicesInfo.push(device);
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
  SET_DEVICE_RESOURCE_ON_NEXT_CHECK: (state, value) => {
    Object.assign(state.popupChosenDevice, {'resourceOnNextCheck': value});
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
  
  SET_PLACES_TO_STATE: (state, places) => {
    state.availablePlaces = [];
    state.availablePlaces = places;
  },
  SET_PLACED_DEVICES: (state, devices) => {
    state.devicesByPlace = [];
    state.devicesByPlace = devices;
  },

  SET_CLEAR_ON_RESPONSIBLES: (state) => {
    state.availableResposibles = [];
  },
  SET_RESPONSBILE_TO_STATE: (state, user) => {
    state.availableResposibles.push(user);
  },
  SET_RESPONSIBLES_DEVICES: (state, devices) => {
    state.devicesByPerson = devices;
  },
  
  SET_CLEAR_BY_SPECIFICATION: (state) => {
    state.devicesBySpecifications = [];
  },
  SET_SPECIFICATIONS_TO_STATE: (state, specifications) => {
    state.availableSpecifications = [];
    state.availableSpecifications = specifications;
  },
  SET_SPECIFICATED_DEVICES: (state, devices) => {
    state.devicesBySpecifications = [];
    state.devicesBySpecifications = devices;
  },

  SET_ALL_USERS: (state, users) => {
    state.allUsers = [];
    state.allUsers = users;
  },
  SET_DEVICE_POOL_ON_ADD: (state, devices) => {
    state.devicesToAdd = [];
    state.devicesToAdd = devices;
  },
  

};
