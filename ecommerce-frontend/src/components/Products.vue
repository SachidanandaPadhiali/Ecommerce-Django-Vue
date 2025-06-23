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
.product-list {
    padding: 2rem;
}

.product-list.loading {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.loader-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100%;
}

.loading {
    position: relative;
    background: currentcolor;
    width: 0.25em;
    height: 0.5em;
    margin: 0 0.5em;
    animation: loading 1s ease-in-out infinite;
    animation-delay: 0.4s;
}

.loading:after,
.loading:before {
    content: "";
    position: absolute;
    width: inherit;
    height: inherit;
    background: inherit;
    -webkit-animation: inherit;
    animation: inherit;
}

.loading:before {
    right: 0.5em;
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
}

.loading:after {
    left: 0.5em;
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
}

@-webkit-keyframes loading {

    0%,
    100% {
        box-shadow: 0 0 0 currentcolor, 0 0 0 currentcolor;
    }

    50% {
        box-shadow: 0 -0.25em 0 currentcolor, 0 0.25em 0 currentcolor;
    }
}

@keyframes loading {

    0%,
    100% {
        box-shadow: 0 0 0 currentcolor, 0 0 0 currentcolor;
    }

    50% {
        box-shadow: 0 -0.25em 0 currentcolor, 0 0.25em 0 currentcolor;
    }
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

.product img {
    width: auto;
    max-width: 220px;
    height: auto;
    max-height: 140px;
    object-fit: cover;
}

.prod_detail {
    margin-top: 10px;
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.star-rating {
    display: flex;
    gap: 4px;
}

.star {
    width: 24px;
    height: 24px;
}

.error {
    color: var(--error);
    text-align: center;
    margin-top: 1rem;
}

.badge {
    position: absolute;
    top: 10px;
    right: 10px;
    background: linear-gradient(to right,
            rgba(169, 3, 41, 1) 0%,
            rgba(196, 72, 72, 1) 44%,
            rgba(170, 34, 56, 1) 100%);
    color: #fff;
    padding: 5px 10px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 10px;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
    z-index: 10;
}

.product {
    position: relative;
    height: 300px;
    text-align: center;
    background-color: var(--bg);
    min-width: 250px;
    margin: 15px;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    cursor: pointer;
    padding-top: 10px;
}

.product:hover {
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15), 0 3px 6px rgba(0, 0, 0, 0.24);
    transform: translateY(-3px);

    img {
        transform: scale(1.05);
    }

    .myBtn {
        background-color: var(--hover);
    }
}

h3 {
    text-align: center;
    font-size: var(--normal-font-size);
    margin: 0;
    padding: 12px 0;
}

p {
    text-align: center;
    color: var(--text-dark);
    padding: 0 8px;
}

h6 {
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
