import { createRouter, createWebHistory } from 'vue-router';
import SignIn from './components/SignIn.vue';
import SignUp from './components/SignUp.vue';
import ProductsPage from './components/ProductsPage.vue';

const routes = [
  { path: '/', component: SignIn },
  { path: '/signin', component: SignIn },
  { path: '/signup', component: SignUp },
  { path: '/products', component: ProductsPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
