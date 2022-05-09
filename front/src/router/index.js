import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/home/HomePage.vue";
import Edit from "@/pages/edit_pixel/EditPixelPage.vue";
import Load from "@/pages/load_canva/LoadPixelPage.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/edit_pixel/:id",
    name: "Edit_pixel_id",
    component: Edit,
  },
  {
    path: "/load_canva",
    name: "Load",
    component: Load,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
