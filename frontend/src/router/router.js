import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/home/home-page";
import AuthPage from "@/views/auth/auth-page";
import JobPage from "@/views/home/job-page/job-page";
import AboutPage from "@/views/home/about-page/about-page";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
