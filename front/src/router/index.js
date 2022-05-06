import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/home/HomePage.vue";
import Edit from "@/pages/edit_pixel/EditPixelPage.vue";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
