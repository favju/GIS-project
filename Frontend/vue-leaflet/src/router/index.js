import { createRouter, createWebHashHistory } from "vue-router"
import Home from "../views/Home.vue"

const routes = [
    {
        path: "/",
        name: "home",
        component: Home
    },
    {
        path: "/PathFinder",
        name: "PathFinder",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ "../views/PathFinder.vue")
    },
    {
        path: "/WeatherApp",
        name: "WeatherApp",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ "../views/WeatherApp.vue")
    },
    {
        path: "/Admin",
        name: "Admin",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ "../views/Admin.vue")
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
