import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/home/home-page";
import AuthPage from "@/views/auth/auth-page";
import JobPage from "@/views/home/job-page/job-page";
import AboutPage from "@/views/home/about-page/about-page";
import Error404Page from "@/views/404-page/404-error-page";
import ChiefPage from "@/views/chief-page/chief-main-page";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/auth",
    name: "auth",
    component: AuthPage,
  },
  {
    path: "/jobPage",
    name: "jobPage",
    component: JobPage,
  },
  {
    path: "/aboutCompany",
    name: "aboutPage",
    component: AboutPage,
  },
  {
    path: '/chiefPage', 
    name: "ChiefPage",
    component: ChiefPage,
  },
  {
    path: '/:pathMatch(.*)*', 
    name: "404Error",
    component: Error404Page,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
