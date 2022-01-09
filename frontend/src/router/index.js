import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MyAccount from '../views/MyAccount.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import ReviewDetail from '../views/ReviewDetail.vue'
import ReviewCreate from '../views/ReviewCreate.vue'
import ReviewsByTag from '../views/ReviewsByTag.vue'

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
    path: '/',
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
    path: '/reviews/:review_id',
    name: 'Review',
    component: ReviewDetail,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/tags/:tag_slug',
    name: 'ReviewsByTag',
    component: ReviewsByTag,
    meta: {
      requireLogin: true
    }
  },
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'Login', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
