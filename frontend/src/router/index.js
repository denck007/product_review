import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MyAccount from '../views/MyAccount.vue'
import MyReviews from '../views/MyReviews.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import ReviewDetail from '../views/ReviewDetail.vue'
import ReviewCreate from '../views/ReviewCreate.vue'
import ProductDetail from '../views/ProductDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true,
    }
  },
  {
    path: '/review-create',
    name: 'ReviewCreate',
    component: ReviewCreate,
    meta: {
      requireLogin: true,
    }
  },
  {
    path: '/',
    redirect: '/reviews'
  },
  {
    path: '/reviews',
    name: 'MyReviews',
    component: MyReviews,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/reviews/:review_id',
    name: 'Review',
    component: ReviewDetail,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/products',
    name: 'Product',
    component: ProductDetail,
    meta: {
      requireLogin: true
    }
  },
]

const router = new VueRouter({
  routes,
  mode: 'history',
})

//
//router.beforeEach((to, from, next) => {
//  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//    console.log(" store.state.isAuthenticated: " + store.state.isAuthenticated)
//    next({ name: 'Login', query: { to: to.path } });
//  } else {
//    console.log("store.state.isAuthenticated: " + store.state.isAuthenticated)
//    next()
//  }
//})

export default router
