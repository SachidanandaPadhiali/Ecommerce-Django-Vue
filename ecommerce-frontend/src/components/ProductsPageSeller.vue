<template>
  <button class="logout-btn" @click="logout()">LOG OUT</button>
  <div>
    <div class="table-title">
      <h1>Products</h1>
    </div>
    <table class="table-fill">
      <thead>
        <tr>
          <th class="text-center">Product</th>
          <th class="text-center">Price</th>
          <th class="text-center">Stock</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody class="table-hover">
        <tr v-for="product in products" :key="product.id">
          <td class="text-left hoverable">{{ product.name }}</td>
          <td class="text-center hoverable">&#8377;{{ product.price }}</td>
          <td class="text-center hoverable">{{ product.stock }}</td>
          <td class="prod-action">
            <button class="btn action-btn edit-btn" @click="editProduct(product)">
              <span>Edit</span>
            </button>
            <!-- Button triggers the delete method -->
            <button class="btn action-btn delete-btn" @click="deleteProduct(product.id)">
              <span>Delete</span>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="container">
      <button class="btn add-btn" @click="showForm = true">ADD NEW PRODUCT</button>

      <div v-if="showForm" class="popup-overlay">
        <div class="popup-form">
          <form @submit.prevent="addProduct">
            <button class="close-btn" @click="showForm = false">×</button>
            <input v-model="formData.name" placeholder="Product Name" required />
            <input v-model.number="formData.price" placeholder="Price" type="number" required />
            <textarea v-model="formData.description" placeholder="Description"></textarea>
            <input v-model.number="formData.stock" placeholder="Stock" type="number" required />
            <div class="actions">
              <!-- Change button text based on edit vs. add mode -->
              <button type="submit">
                {{ formData.id ? 'Update' : 'Add' }} Product
              </button>
              <!-- Button to clear/reset the form -->
              <button class="cancel" type="button" @click="resetForm">Reset</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProductsPageSeller',
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
      apiUrl: `${process.env.VUE_APP_API_URL}/api/products/`,
      showForm: false,
    };
  },
  // Fetch the products as soon as the component is mounted
  mounted() {
    this.fetchProducts();
  },
  methods: {
    // Retrieve all products from the server
    fetchProducts() {
      axios.get(this.apiUrl, {
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      }).then((response) => {
        this.products = response.data;
      }).catch((error) => {
        console.error('Error fetching products:', error);
      });
    },

    // Handle form submission to create or update product
    addProduct() {
      const config = {
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`, // Replace with your real token
        }
      };

      console.log(config);

      if (this.formData.id) {
        // Update existing product
        axios
          .put(`${this.apiUrl}${this.formData.id}/`, this.formData, config)
          .then(() => {
            this.fetchProducts();
            this.resetForm();
            this.showForm = false;
          })
          .catch((error) => {
            console.error('Error updating product:', error);
          });
      } else {
        // Create new product
        axios
          .post(this.apiUrl, this.formData, config)
          .then(() => {
            this.fetchProducts();
            this.resetForm();
            this.showForm = false;
          })
          .catch((error) => {
            console.error('Error creating product:', error);
          });
      }
    },

    // Populate the form with product data for editing
    editProduct(product) {
      this.showForm = true;
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
    closeForm() {
      this.showForm = false
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
    logout() {
      localStorage.removeItem('token');
      delete axios.defaults.headers.common['Authorization'];
      this.$router.push('/');
    }
  }
};
</script>

<style>
.table-title {
  display: block;
  margin: auto;
  max-width: 900px;
  padding: 5px;
  width: 100%;
}

.table-title h1 {
  color: var(--text-dark);
  font-size: 40px;
  text-align: center;
  font-weight: 1000;
  font-family: "Roboto", helvetica, arial, sans-serif;
  text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
  text-transform: uppercase;
}

.table-fill {
  border-collapse: collapse;
  margin: auto;
  max-width: 900px;
  width: 90%;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

th {
  color: #D5DDE5;
  background: var(--text-dark);
  border-bottom: 4px solid var(--bg-btn);
  font-size: 20px;
  text-transform: uppercase;
  font-weight: var(--font-slim);
  padding: 10px;
}

tr {
  color: var(--box-bg);
  font-weight: normal;
  text-shadow: 0 1px 1px rgba(256, 256, 256, 0.1);
}

tr:hover td.hoverable {
  color: var(--text-light);
  background: var(--hover-bg);
  border-top: 1px solid #22262e;
}

td {
  background: #FFFFFF;
  padding: 10px 0;
  max-height: 50px;
  text-align: left;
  vertical-align: middle;
  font-weight: 300;
  font-size: 18px;
  text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.1);
  border-right: 1px solid #C1C3D1;
}

td:last-child {
  border-right: 0px;
}

th.text-left {
  text-align: left;
}

th.text-center {
  text-align: center;
}

th.text-right {
  text-align: right;
}

td.text-left {
  text-align: left;
}

td.text-center {
  text-align: center;
}

td.text-right {
  text-align: right;
}

.prod-action {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4rem;
  height: 100%;
}

.btn {
  padding: 10px 30px;
  border: none;
  border-radius: 20px;
  font-size: 1rem;
  font-weight: 600;
  color: inherit;
  cursor: pointer;
  transition: all 0.3s ease;
  background: transparent;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
}

.action-btn {
  backdrop-filter: blur(20px);
  transition: all 0.3s ease;
}

.edit-btn:hover {
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-color: cyan;
  color: rgb(0, 127, 127);
}

.delete-btn:hover {
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-color: red;
  color: red;
}

.container {
  text-align: center;
  margin-top: 60px;
}

.add-btn {
  padding: 12px 24px;
  font-size: 16px;
  color: var(--dark-text);
  border: 2px solid black;
  border-radius: 50px;
  cursor: pointer;
}

.add-btn:hover {
  background-color: var(--hover-bg);
  color: var(--white-text);
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(27, 30, 36, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.popup-form {
  background-color: #ffffff;
  padding: 0 10px 10px 10px;
  border-radius: 12px;
  width: 300px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.popup-form h2 {
  margin-bottom: 20px;
  color: #1B1E24;
}

.popup-form input,
.popup-form textarea {
  display: block;
  width: 280px;
  padding: 10px;
  margin-bottom: 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
}

.actions {
  display: flex;
  justify-content: space-between;
}

.actions button {
  padding: 10px 20px;
  border: none;
  background-color: #4E5066;
  color: white;
  border-radius: 6px;
  cursor: pointer;
}

.actions .cancel {
  background-color: #ccc;
  color: #333;
}

.close-btn {
  position: relative;
  float: right;
  padding: 0;
  padding-bottom: 10px;
  background: transparent;
  border: none;
  font-size: 30px;
  cursor: pointer;
  color: #333;
}

.close-btn:hover {
  color: #000;
}

@media only screen and (max-width: 900px) {
  .table-fill {
    width: 90%;
  }

  .table-title {
    width: 90%;
  }
}
</style>
