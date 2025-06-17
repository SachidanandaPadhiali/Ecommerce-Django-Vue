<template>
  <div>
    <h1>Products</h1>
    
    <!-- Display list of products -->
    <ul>
      <!-- Loop through products array -->
      <li v-for="product in products" :key="product.id">
        {{ product.name }} - ${{ product.price }}
        <!-- Button triggers the edit method -->
        <button @click="editProduct(product)">Edit</button>
        <!-- Button triggers the delete method -->
        <button @click="deleteProduct(product.id)">Delete</button>
      </li>
    </ul>

    <!-- Form to create or update a product -->
    <form @submit.prevent="submitForm">
      <input
        v-model="formData.name"
        placeholder="Product Name"
        required
      />
      <input
        v-model.number="formData.price"
        placeholder="Price"
        type="number"
        required
      />
      <textarea
        v-model="formData.description"
        placeholder="Description"
      ></textarea>
      <input
        v-model.number="formData.stock"
        placeholder="Stock"
        type="number"
        required
      />
      <!-- Change button text based on edit vs. add mode -->
      <button type="submit">
        {{ formData.id ? 'Update' : 'Add' }} Product
      </button>
      <!-- Button to clear/reset the form -->
      <button type="button" @click="resetForm">Reset</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductsPage',
  data() {
    return {
      // Holds all products fetched from the API
      products: [],
      // Used for both new and editing product data
      formData: {
        name: '',
        description: '',
        price: 0,
        stock: 0,
        id: null,
      },
      // Base URL for your Django API (adjust if necessary)
      apiUrl: 'http://localhost:8000/api/products/',
    };
  },
  methods: {
    // Retrieve all products from the server
    fetchProducts() {
      axios
        .get(this.apiUrl)
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error('Error fetching products:', error);
        });
    },

    // Handle form submission to create or update product
    submitForm() {
      if (this.formData.id) {
        // If formData has an id, update the existing product
        axios
          .put(`${this.apiUrl}${this.formData.id}/`, this.formData)
          .then(() => {
            this.fetchProducts();
            this.resetForm();
          })
          .catch((error) => {
            console.error('Error updating product:', error);
          });
      } else {
        // Otherwise, create a new product
        axios
          .post(this.apiUrl, this.formData)
          .then(() => {
            this.fetchProducts();
            this.resetForm();
          })
          .catch((error) => {
            console.error('Error creating product:', error);
          });
      }
    },

    // Populate the form with product data for editing
    editProduct(product) {
      // Use the spread operator to copy product data into formData
      this.formData = { ...product };
    },

    // Delete a product via its API endpoint
    deleteProduct(id) {
      axios
        .delete(`${this.apiUrl}${id}/`)
        .then(() => {
          this.fetchProducts();
        })
        .catch((error) => {
          console.error('Error deleting product:', error);
        });
    },

    // Reset the form data to initial values
    resetForm() {
      this.formData = {
        name: '',
        description: '',
        price: 0,
        stock: 0,
        id: null,
      };
    },
  },
  // Fetch the products as soon as the component is mounted
  mounted() {
    this.fetchProducts();
  },
};
</script>

<style scoped>
/* Basic styling, feel free to customize */
ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 0.5rem;
}

input,
textarea {
  display: block;
  margin-bottom: 0.5rem;
  padding: 0.4rem;
  width: 250px;
}

button {
  margin-right: 0.5rem;
}
</style>
