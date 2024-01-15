import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExperienceView from '../views/ExperienceView.vue'
import ProjetView from '../views/ProjetView.vue'
import FormationView from '../views/FormationView.vue'
import CertificationView from '../views/CertificationView.vue'
import ImplicationView from '../views/ImplicationView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/experience',
    name: 'experience',
    component: ExperienceView
  },
  {
    path: '/projet',
    name: 'projet',
    component: ProjetView
  },
  {
    path: '/formation',
    name: 'formation',
    component: FormationView
  },
  {
    path: '/certification',
    name: 'certification',
    component: CertificationView
  },
  {
    path: '/implication',
    name: 'implication',
    component: ImplicationView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
