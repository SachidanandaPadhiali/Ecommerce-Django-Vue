<template>
    <div class="product-detail" v-if="product">
        <img :src="`${this.apiUrl}/${product.id}.png`" alt="Product Image" />
        <div class="info">
            <h2>{{ product.name }}</h2>
            <h3 v-if="product.stock === 0">OUT OF STOCK</h3>
            <p class="price" v-else>₹{{ product.price }}</p>
            <p class="description">{{ product.description }}</p>
        </div>
    </div>

    <div v-else-if="loading" class="loading">Loading product...</div>
    <div v-else class="error">Product not found.</div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            product: null,
            loading: true,
            apiUrl: `${process.env.VUE_APP_API_URL}/media/images`
        };
    },
    methods: {
        async fetchProduct() {
            const id = this.$route.params.id;
            try {
                const response = await axios.get(`${process.env.VUE_APP_API_URL}/api/products/${id}/`, {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                    }
                });
                this.product = response.data;
            } catch (error) {
                console.error('Failed to fetch product:', error);
            } finally {
                this.loading = false;
            }
        }
    },
    mounted() {
        this.fetchProduct();
    }
};
</script>

<style scoped>
.product-detail {
    display: flex;
    flex-wrap: wrap;
    padding: 2rem;
    gap: 2rem;
    background: #fff;
    border-radius: 8px;
}

.product-detail img {
    width: 300px;
    object-fit: cover;
    border-radius: 8px;
}

.info {
    flex: 1;
}

.price {
    font-weight: bold;
    font-size: 1.3rem;
    margin: 1rem 0;
}

.description {
    line-height: 1.5;
    margin-bottom: 2rem;
}

.loading,
.error {
    text-align: center;
    margin-top: 2rem;
    font-size: 1.2rem;
}
</style>
