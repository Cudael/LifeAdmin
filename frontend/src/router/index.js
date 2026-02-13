import { createRouter, createWebHistory } from 'vue-router'
import { accessToken } from '../utils/auth'
import LandingPage from '../pages/LandingPage.vue'
import LoginPage from '../pages/LoginPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'
import ForgotPasswordPage from '../pages/ForgotPasswordPage.vue'
import ResetPasswordPage from '../pages/ResetPasswordPage.vue'
import AuthCallback from '../pages/AuthCallback.vue'
import DashboardPage from '../pages/DashboardPage.vue'
import AddDocumentPage from '../pages/AddDocumentPage.vue'
import EditItemPage from '../pages/EditItemPage.vue'
import SettingsPage from '../pages/SettingsPage.vue'
import ItemsPage from '../pages/ItemsPage.vue'
import ItemDetails from '../pages/ItemDetails.vue'
import ProfilePage from '../pages/ProfilePage.vue'
import CalendarPage from '../pages/CalendarPage.vue'
import VerifyEmailPage from '../pages/VerifyEmailPage.vue'
import PrivacyPolicyPage from '../pages/PrivacyPolicyPage.vue'
import TermsOfServicePage from '../pages/TermsOfServicePage.vue'
import CookiePolicyPage from '../pages/CookiePolicyPage.vue'

const routes = [
  // Public routes
  { 
    path: '/', 
    name: 'Landing',
    component: LandingPage 
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: PrivacyPolicyPage
  },
  {
    path: '/terms',
    name: 'Terms',
    component: TermsOfServicePage
  },
  {
    path: '/cookies',
    name: 'Cookies',
    component: CookiePolicyPage
  },

  // Guest-only routes (redirect to dashboard if logged in)
  { 
    path: '/login', 
    name: 'Login',
    component: LoginPage, 
    meta: { guestOnly: true } 
  },
  { 
    path: '/register', 
    name: 'Register',
    component: RegisterPage, 
    meta: { guestOnly: true } 
  },
  { 
    path: '/forgot-password', 
    name: 'ForgotPassword',
    component: ForgotPasswordPage, 
    meta: { guestOnly: true } 
  },
  { 
    path: '/reset-password', // ✅ Fixed: removed :token parameter
    name: 'ResetPassword',
    component: ResetPasswordPage, 
    meta: { guestOnly: true } 
  },
  {
    path: '/verify-email',
    name: 'VerifyEmail',
    component: VerifyEmailPage
  },

  // OAuth callback (no auth required during callback)
  { 
    path: '/auth/callback', 
    name: 'AuthCallback',
    component: AuthCallback 
  },

  // Protected routes (require authentication)
  { 
    path: '/dashboard', 
    name: 'Dashboard',
    component: DashboardPage, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/add-document', 
    name: 'AddDocument',
    component: AddDocumentPage, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/add-subscription', 
    name: 'AddSubscription', 
    component: () => import('../pages/AddSubscriptionPage.vue'), 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/items', 
    name: 'Items', 
    component: ItemsPage, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/items/:id', 
    name: 'ItemDetails', 
    component: ItemDetails, 
    props: true, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/items/:id/edit', 
    name: 'ItemEdit', 
    component: EditItemPage, 
    props: true, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/calendar', 
    name: 'Calendar', 
    component: CalendarPage, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/profile', 
    name: 'Profile', 
    component: ProfilePage, 
    meta: { requiresAuth: true } 
  },
  { 
    path: '/settings', 
    name: 'Settings', 
    component: SettingsPage, 
    meta: { requiresAuth: true } 
  },

  // 404 catch-all - redirect to landing or dashboard
  {
    path: '/:pathMatch(.*)*',
    redirect: (to) => {
      // If logged in, go to dashboard, otherwise landing
      return accessToken.value ? '/dashboard' : '/'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Global auth guard
router.beforeEach(async (to, from, next) => {
  const isLoggedIn = !!accessToken.value

  // Redirect authenticated users away from guest-only pages
  if (to.meta.guestOnly && isLoggedIn) {
    return next('/dashboard')
  }

  // Redirect unauthenticated users to login
  if (to.meta.requiresAuth && !isLoggedIn) {
    return next('/login')
  }

  next()
})

export default router