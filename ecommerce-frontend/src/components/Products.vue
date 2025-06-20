<template>
    <div class="product-list">
        <div v-if="loading" class="loading">Loading...</div>
        <div v-else class="grid">
            <div class="product" v-for="product in products" :key="product.id">
                <img :src="`${this.apiUrl}/${product.id}.png`" alt="Product Image" />
                <h3>{{ product.name }}</h3>
                <p>₹{{ product.price }}</p>
                <button @click="viewProduct(product.id)">View</button>
            </div>
            <div class="product" v-for="product in products" :key="product.id">
                <img :src="`${this.apiUrl}/${product.id}.png`" alt="Product Image" />
                <h3>{{ product.name }}</h3>
                <p>₹{{ product.price }}</p>
                <button @click="viewProduct(product.id)">View</button>
            </div>
            <div class="product" v-for="product in products" :key="product.id">
                <img :src="`${this.apiUrl}/${product.id}.png`" alt="Product Image" />
                <h3>{{ product.name }}</h3>
                <p>₹{{ product.price }}</p>
                <button @click="viewProduct(product.id)">View</button>
            </div>
        </div>
        <div v-if="error" class="error">{{ error }}</div>
        <router-link to="/seller/products" class="nav-link">Seller</router-link>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ProductsPage',
    data() {
        return {
            products: [],
            loading: true,
            error: '',
            apiUrl: `${process.env.VUE_APP_API_URL}/media/images`
        };
    },
    methods: {
        async fetchProducts() {
            try {
                const response = await axios.get(`${process.env.VUE_APP_API_URL}/api/products/`, {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                    }
                });
                this.products = response.data;
            } catch (err) {
                this.error = 'Failed to load products. Please try again.';
                console.error(err);
            } finally {
                this.loading = false;
            }
        },
        viewProduct(id) {
            this.$router.push(`/products/${id}`);
        }
    },
    mounted() {
        this.fetchProducts();
    }
};
</script>

<style scoped>
.product-list {
    padding: 2rem;
}

h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
}

.product {
    border: 1px solid #ddd;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    background-color: #fff;
}

.product img {
    width: auto;
    height: 100%;
    max-height: 160px;
    object-fit: cover;
}

.loading {
    text-align: center;
}

.error {
    color: red;
    text-align: center;
    margin-top: 1rem;
}
</style>
