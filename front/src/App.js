window.Vue = require("vue");
Vue.component("container", require("./components/Container.vue"));
const app = new Vue({
  el: "#app",
});
