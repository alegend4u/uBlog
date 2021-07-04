import { createRouter, createWebHistory } from "vue-router";
import About from "../views/About.vue";
import Portfolio from "../views/Portfolio.vue";

const routes = [
  {
    path: "/",
    name: "About",
    component: About,
  },
  {
    path: "/portfolio",
    name: "Portfolio",
    component: Portfolio,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
