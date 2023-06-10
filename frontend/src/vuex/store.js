import auth_module from "./authentication/auth_module";
import device_pool_module from "./device_pool/device_pool_module";
import devices_in_use_module from "./devices_in_use/devices_in_use_module";
import users_module from "./users/users_module";
import { createStore } from "vuex";

let store = createStore({
    modules: {
        auth: auth_module,
        device_pool: device_pool_module,
        devices_in_use: devices_in_use_module,
        users: users_module
    }
});

export default store;
