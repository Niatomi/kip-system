import { createApp } from "vue";
import App from "./App.vue";
import router from "./router/router";
import store from "./vuex/authentication/auth_module";
import { VueCookies } from "vue-cookies";
import 'material-design-icons-iconfont'

createApp(App).use(VueCookies, { expires: '7d'}).use(router).use(store).mount("#app");
