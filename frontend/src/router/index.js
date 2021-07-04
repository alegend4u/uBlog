import { createRouter, createWebHistory } from "vue-router";
import About from "../views/About.vue";
import Portfolio from "../views/Portfolio.vue";
import Contact from "../views/Contact.vue";

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
  {
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
