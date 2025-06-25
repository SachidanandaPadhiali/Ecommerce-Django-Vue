import { createRouter, createWebHistory } from 'vue-router';
import SignIn from './components/SignIn.vue';
import SignUp from './components/SignUp.vue';
import ProductsPage from './components/Products.vue';
import ProductDetail from './components/ProductDetail.vue';
import ProductsPageSeller from './components/ProductsPageSeller.vue';

const routes = [
  { path: '/', component: SignIn },
  { path: '/signin', component: SignIn },
  { path: '/signup', component: SignUp },
  { path: '/products', component: ProductsPage },
  { path: '/seller/products', component: ProductsPageSeller },
  { path: '/products/:id', component: ProductDetail }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth'
      };
    }
    return { top: 0 };
  }
});

// Navigation Guard to check authentication
router.beforeEach((to, from, next) => {
    const isAuthenticated = localStorage.getItem('token'); // Check if token exists

    if (to.meta.requiresAuth && !isAuthenticated) {
        next('/HomePage'); // Redirect to login
    } else {
        next(); // Allow access
    }
});

export default router;
