import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/about/home/HomePage.vue";
import Edit from "@/pages/about/edit_pixel/EditPixelPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/edit_pixel",
    name: "Edit_pixel",
    component: Edit,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
