import { createRouter, createWebHistory } from 'vue-router'
import { accessToken } from '../utils/auth'

const routes = [
  // Public routes
  { 
    path: '/', 
    name: 'Landing',
    component: () => import('../pages/LandingPage.vue'),
    meta: { title: 'Remindes – Document & Subscription Management' }
  },
  {
    path: '/privacy',
    name: 'Privacy',
    component: () => import('../pages/PrivacyPolicyPage.vue'),
    meta: { title: 'Privacy Policy – Remindes' }
  },
  {
    path: '/terms',
    name: 'Terms',
    component: () => import('../pages/TermsOfServicePage.vue'),
    meta: { title: 'Terms of Service – Remindes' }
  },
  {
    path: '/cookies',
    name: 'Cookies',
    component: () => import('../pages/CookiePolicyPage.vue'),
    meta: { title: 'Cookie Policy – Remindes' }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('../pages/ContactPage.vue'),
    meta: { title: 'Contact – Remindes' }
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../pages/AboutPage.vue'),
    meta: { title: 'About – Remindes' }
  },

  // Guest-only routes (redirect to dashboard if logged in)
  { 
    path: '/login', 
    name: 'Login',
    component: () => import('../pages/LoginPage.vue'),
    meta: { guestOnly: true, title: 'Login – Remindes' } 
  },
  { 
    path: '/register', 
    name: 'Register',
    component: () => import('../pages/RegisterPage.vue'),
    meta: { guestOnly: true, title: 'Register – Remindes' } 
  },
  { 
    path: '/forgot-password', 
    name: 'ForgotPassword',
    component: () => import('../pages/ForgotPasswordPage.vue'),
    meta: { guestOnly: true, title: 'Forgot Password – Remindes' } 
  },
  { 
    path: '/reset-password', // ✅ Fixed: removed :token parameter
    name: 'ResetPassword',
    component: () => import('../pages/ResetPasswordPage.vue'),
    meta: { guestOnly: true, title: 'Reset Password – Remindes' } 
  },
  {
    path: '/verify-email',
    name: 'VerifyEmail',
    component: () => import('../pages/VerifyEmailPage.vue'),
    meta: { title: 'Verify Email – Remindes' }
  },

  // OAuth callback (no auth required during callback)
  { 
    path: '/auth/callback', 
    name: 'AuthCallback',
    component: () => import('../pages/AuthCallback.vue'),
    meta: { title: 'Authenticating – Remindes' }
  },

  // Protected routes (require authentication)
  { 
    path: '/dashboard', 
    name: 'Dashboard',
    component: () => import('../pages/DashboardPage.vue'),
    meta: { requiresAuth: true, title: 'Dashboard – Remindes' } 
  },
  { 
    path: '/add-item', 
    name: 'AddItem',
    component: () => import('../pages/AddItemWizard.vue'), 
    meta: { requiresAuth: true, title: 'Add Item – Remindes' } 
  },
  { 
    path: '/items', 
    name: 'Items', 
    component: () => import('../pages/ItemsPage.vue'),
    meta: { requiresAuth: true, title: 'My Items – Remindes' } 
  },
  { 
    path: '/items/:id', 
    name: 'ItemDetails', 
    component: () => import('../pages/ItemDetails.vue'),
    props: true, 
    meta: { requiresAuth: true, title: 'Item Details – Remindes' } 
  },
  { 
    path: '/items/:id/edit', 
    name: 'ItemEdit', 
    component: () => import('../pages/EditItemPage.vue'),
    props: true, 
    meta: { requiresAuth: true, title: 'Edit Item – Remindes' } 
  },
  { 
    path: '/calendar', 
    name: 'Calendar', 
    component: () => import('../pages/CalendarPage.vue'),
    meta: { requiresAuth: true, title: 'Calendar – Remindes' } 
  },
  { 
    path: '/profile', 
    name: 'Profile', 
    component: () => import('../pages/ProfilePage.vue'),
    meta: { requiresAuth: true, title: 'Profile – Remindes' } 
  },
  { 
    path: '/settings', 
    name: 'Settings', 
    component: () => import('../pages/SettingsPage.vue'),
    meta: { requiresAuth: true, title: 'Settings – Remindes' } 
  },
  { 
    path: '/subscription', 
    name: 'Subscription', 
    component: () => import('../pages/SubscriptionPage.vue'),
    meta: { requiresAuth: true, title: 'Subscription – Remindes' } 
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
  scrollBehavior(to, from, savedPosition) {
    // If there's a saved position (browser back/forward), use it
    if (savedPosition) {
      return savedPosition
    }
    // If navigating to a hash (anchor), scroll to that element with offset for fixed header
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 80, // Offset for fixed header
      }
    }
    // Otherwise scroll to top of the page
    return { top: 0, behavior: 'smooth' }
  },
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

// Update page title on route change
router.afterEach((to) => {
  document.title = to.meta.title || 'Remindes'
})

export default router