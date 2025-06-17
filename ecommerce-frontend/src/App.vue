<template>
  <div id="app">
    <!-- Include our Product management component -->
    <ProductsPage />
  </div>
</template>

<script>
// Import the Products component
import ProductsPage from './components/ProductsPage.vue';

export default {
  name: 'App',
  components: {
    ProductsPage,
  },
};
</script>
