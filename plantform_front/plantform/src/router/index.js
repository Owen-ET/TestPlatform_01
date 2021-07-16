import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp.vue'
import Main from '../components/Main.vue'
import TestReport from '../components/TestReport.vue'
import TestCase from '../components/TestCase.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/signUp',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/main',
    name: 'Main',
    component: Main,
    meta: {requiresAuth: true},
    children:[
      {
        path: '/report',
        name: 'TestReport',
        component: TestReport
      },
      {
        path: '/case',
        name: 'TestCase',
        component: TestCase
      },
    ]
  }
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!auth.loggedIn()) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next() // 确保一定要调用 next()
  }
})


export default router
