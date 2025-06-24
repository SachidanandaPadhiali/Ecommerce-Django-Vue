<template>
    <div :class="['product-list', { loading: isLoading }]">
        <div v-if="loading" class="loader-wrapper">
            <div class="loading"></div>
        </div>
        <div v-else class="grid">
            <div class="product" v-for="product in products" :key="product.id">
                <div class="badge" v-if="product.isOnSale === true">HOT SALE</div>
                <img :src="`${this.apiUrl}/${product.id}.png`" alt="Product Image" />
                <div class="prod_detail">
                    <h3>{{ truncateName(product.name) }}</h3>
                    <div class="star-rating" v-if="product.rating > 0.5">
                        <svg v-for="n in max" :key="n" class="star" viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient :id="'grad-' + n" x1="0" x2="100%" y1="0" y2="0">
                                    <stop offset="0%" stop-color="gold" />
                                    <stop :offset="getFill(n, product.rating)" stop-color="gold" />
                                    <stop :offset="getFill(n, product.rating)" stop-color="#ccc" />
                                    <stop offset="100%" stop-color="#ccc" />
                                </linearGradient>
                            </defs>
                            <path :fill="'url(#grad-' + n + ')'"
                                d="M12 2l2.9 6.9L22 9.3l-5 5 1.2 7.7L12 18l-6.2 4 1.2-7.7-5-5 7.1-0.4L12 2z" />
                        </svg>
                    </div>
                    <h6>₹{{ product.price }}</h6>
                    <button class="myBtn" @click="viewProduct(product.id)">View</button>
                </div>
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
            max: 5,
            apiUrl: `${process.env.VUE_APP_API_URL}/media/images`
        };
    },
    methods: {
        async fetchProducts() {
            try {
                setTimeout(() => {
                    // Code to be executed after the delay
                    this.message = 'Delayed message!';
                }, 4000);
                const response = await axios.get(`${process.env.VUE_APP_API_URL}/api/products/`, {
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                    }
                });
                this.products = response.data;
                console.log(this.products);

            } catch (err) {
                this.error = 'Failed to load products. Please try again.';
                console.error(err);
            } finally {
                this.loading = false;
            }
        },
        truncateName(name) {
            return name.length > 30 ? name.slice(0, 27) + '...' : name;
        },
        getFill(index, rating) {
            const fill = Math.min(Math.max(rating - (index - 1), 0), 1);
            return (fill * 100) + '%';
        },
        viewProduct(id) {
            this.$router.push(`/products/${id}`);
        }
    },
    mounted() {
        setTimeout(() => {
            this.fetchProducts()
        }, 2000)
    }
};
</script>

<style>
.prod_detail h3 {
    text-align: center;
    font-size: var(--normal-font-size);
    margin: 0;
    padding: 12px 0;
}

.prod_detail p {
    text-align: center;
    color: var(--text-dark);
    padding: 0 8px;
}

.prod_detail h6 {
    font-size: 18px;
    text-align: center;
    color: #222f25;
    margin: 5px 0;
}

.myBtn {
    text-align: center;
    width: 100%;
    border: none;
    padding: 10px;
    background-color: var(--bg-btn);
    color: #fff;
    cursor: pointer;
    outline: none;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
</style>
