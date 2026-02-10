import { createRouter, createWebHistory } from 'vue-router'

import LandingPage from '../pages/LandingPage.vue'
import LoginPage from '../pages/LoginPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import DashboardPage from '../pages/DashboardPage.vue'
import AddDocumentPage from '../pages/AddDocumentPage.vue'
import EditItemPage from '../pages/EditItemPage.vue'
import SettingsPage from '../pages/SettingsPage.vue'
import ItemsPage from '../pages/ItemsPage.vue'
import ItemDetails from '../pages/ItemDetails.vue'

const routes = [
  { path: '/', component: LandingPage },

  // Guest-only routes
  { path: '/login', component: LoginPage, meta: { guestOnly: true } },
  { path: '/register', component: RegisterPage, meta: { guestOnly: true } },

  // Auth-required routes
  { path: '/dashboard', component: DashboardPage, meta: { requiresAuth: true } },
  { path: '/add-document', component: AddDocumentPage, meta: { requiresAuth: true } },
  { path: "/add-subscription", name: "AddSubscription", component: () => import("../pages/AddSubscriptionPage.vue"), meta: { requiresAuth: true } },
  { path: "/settings", name: "Settings", component: SettingsPage, meta: { requiresAuth: true } },
  { path: "/items", name: "Items", component: ItemsPage, meta: { requiresAuth: true } },
  { path: "/items/:id", name: "ItemDetails", component: () => import("../pages/ItemDetails.vue"), props: true, meta: { requiresAuth: true } },
  {path: "/items/:id/edit", name: "item-edit", component: () => import("../pages/EditItemPage.vue"), props: true, meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Global auth guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token")
  const isLoggedIn = !!token

  if (to.meta.guestOnly && isLoggedIn) {
    return next("/dashboard")
  }

  if (to.meta.requiresAuth && !isLoggedIn) {
    return next("/login")
  }

  next()
})

export default router