<template>
    <NavBar />
    <div class="productPageContainer" v-if="product">
        <div class="productPageImgContainer">
            <div class="productPageImagesBar">
                <div v-for="(img, index) in images" :key="index" class="image"
                    :class="{ selected: selectedIndex === index }" @click="selectImage(index)">
                    <img :src="img" alt="" />
                </div>
            </div>

            <div class="productPageFullImage" ref="imgZoom" @mousemove="handleMouseMove" @mouseleave="handleMouseLeave">
                <img :src="selectedImage" alt="Product Preview" />
            </div>
        </div>
        <div class="product-info">
            <h1>{{ product.name }}</h1>
            <p class="sku">SKU: {{ product.id }} | </p>
            <h3 v-if="product.stock === 0" class="error">OUT OF STOCK</h3>
            <div class="productPagePrice" v-else>
                <span class="price">₹{{ product.price }}</span>
                <span class="priceAfter">₹{{ product.price }}</span>
            </div>
            <p class="payment-info"> <a href="#"></a></p>

            <div class="purchase_wrraper">
                <!-- Quantity -->
                <div class="quantity-section">
                    <button>-</button>
                    <input type="text" class="quantity-input" value="1">
                    <button>+</button>
                </div>

                <!-- Purchase -->
                <div class="purchase" v-if="product.stock > 0">
                    <button class="addToCart">Add to Cart</button>
                    <button class="buy-now">Buy Now</button>
                </div>
            </div>

            <!-- Additional Info (Free Shipping, Support, Warranty, Delivery) -->
            <div class="additional-info">
                <p><strong>Free Shipping on Orders Over $50</strong></p>
                <p><strong>24/7 Customer Support:</strong> +1-800-123-4567</p>
                <p><strong>1-Year Manufacturer Warranty</strong></p>
                <p><strong>Delivery:</strong> 3 - 5 Business Days</p>
            </div>
            <div class="tab-content">
                <p>{{ product.description }}</p>
            </div>
        </div>
    </div>

    <div v-else-if="loading" class="loading">Loading product...</div>
    <div v-else class="error">Product not found.</div>
</template>

<script>
import axios from "axios";
import NavBar from "./NavBar.vue";

export default {
    name: "ProductPage",
    components: {
        NavBar
    },
    data() {
        return {
            product: null,
            loading: true,
            apiUrl: `${process.env.VUE_APP_API_URL}`,
            images: [],
            selectedIndex: 0,
            selectedImage: "",
            isDesktop: window.innerWidth >= 768
        };
    },
    mounted() {
        this.fetchProduct();
        window.addEventListener("resize", () => {
            this.isDesktop = window.innerWidth >= 768;
        });
        this.setupSwipe();
    },
    methods: {
        async fetchProduct() {
            const id = this.$route.params.id;
            try {
                const response = await axios.get(`${this.apiUrl}/api/products/${id}/`);
                this.product = response.data;
                this.images = [response.data.image, response.data.image, response.data.image];
                console.log(this.images);
                this.selectedImage = response.data.image;
                this.loading = false;

                this.$nextTick(() => {
                    this.selectImage(0);
                });
            } catch (error) {
                console.error("Error fetching product:", error);
                this.loading = false;
            }
        },
        selectImage(index) {
            this.selectedIndex = index;
            this.selectedImage = this.images[index];
            this.setZoomImage(this.selectedImage);
        },
        setZoomImage(imageUrl) {
            const imgZoom = this.$refs.imgZoom;
            if (imgZoom && this.isDesktop) {
                imgZoom.style.setProperty("--img", `url(${imageUrl})`);
            }
        },
        handleMouseMove(e) {
            if (!this.isDesktop) return;
            const imgZoom = this.$refs.imgZoom;
            const rect = imgZoom.getBoundingClientRect();
            const offsetX = e.clientX - rect.left;
            const offsetY = e.clientY - rect.top;
            const x = `${(offsetX / rect.width) * 100}%`;
            const y = `${(offsetY / rect.height) * 100}%`;
            imgZoom.style.setProperty("--display", "block");
            imgZoom.style.setProperty("--zoom-x", x);
            imgZoom.style.setProperty("--zoom-y", y);
        },
        handleMouseLeave() {
            const imgZoom = this.$refs.imgZoom;
            imgZoom.style.setProperty("--display", "none");
        },
        setupSwipe() {
            const el = this.$refs.imgZoom;
            if (!el || this.isDesktop) return;

            let startX = 0;

            el.addEventListener('touchstart', (e) => {
                startX = e.touches[0].clientX;
            });

            el.addEventListener('touchend', (e) => {
                const endX = e.changedTouches[0].clientX;
                const diff = endX - startX;

                if (Math.abs(diff) > 50) {
                    if (diff < 0) this.nextImage();  // swipe left
                    else this.prevImage();           // swipe right
                }
            });
        },

        nextImage() {
            if (this.selectedIndex < this.images.length - 1) {
                this.selectImage(this.selectedIndex + 1);
            }
        },

        prevImage() {
            if (this.selectedIndex > 0) {
                this.selectImage(this.selectedIndex - 1);
            }
        }
    }
};
</script>

<style>
.productPageContainer {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
}

.productPageImgContainer {
    display: flex;
    flex-direction: row;
    gap: 1rem;
    align-items: flex-start;
}

.productPageImagesBar {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    max-height: 400px;
    overflow-y: auto;
    width: 80px;
}

.productPageImagesBar .image {
    width: 100%;
    height: 80px;
    cursor: pointer;
    opacity: 0.5;
    border-radius: 4px;
    overflow: hidden;
}

.productPageImagesBar .image.selected {
    opacity: 1;
    outline: 2px solid #000;
}

.productPageImagesBar .image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.productPageFullImage {
    position: relative;
    width: 100%;
    max-width: 500px;
    --img: none;
    --zoom-x: 50%;
    --zoom-y: 50%;
    --display: none;
}

.productPageFullImage img {
    width: 100%;
    height: auto;
    display: block;
    z-index: 2;
    position: relative;
}

.productPageFullImage::before {
    content: '';
    display: var(--display);
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-image: var(--img);
    background-size: 200%;
    background-repeat: no-repeat;
    background-position: var(--zoom-x) var(--zoom-y);
    pointer-events: none;
    z-index: 1;
}

.productPageFullImage::after {
    content: "";
    display: var(--display);
    background-image: var(--img);
    background-size: 150%;
    background-position: var(--zoom-x) var(--zoom-y);
    position: absolute;
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    z-index: 2;
    pointer-events: none;
}

.productPageInfoContainer {
    padding: 1rem;
    background: #f9f9f9;
    border-radius: 8px;
}

.productPagePrice {
    display: flex;
    gap: 10px;
    font-weight: bold;
    margin: 1rem 0;
}

.priceAfter {
    text-decoration: line-through;
    padding-top: 11px;
}

.product-info {
    flex: 1.5;
    border-bottom: 1px solid #ddd;
    padding-bottom: 20px;
}

.product-info h1 {
    font-size: 28px;
    margin-bottom: 15px;
    color: #000;
}

.sku {
    font-size: 14px;
    color: #999;
}

.price {
    font-size: 30px;
    color: #333;
    margin-bottom: 10px;
}

.payment-info {
    font-size: 14px;
    color: #555;
}

.payment-info a {
    text-decoration: none;
    color: #000;
}

.options {
    margin-bottom: 20px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 20px;
}

.option-label {
    font-weight: bold;
    margin-bottom: 5px;
}

.option-buttons {
    display: flex;
    gap: 10px;
}

.option-buttons button {
    padding: 10px 20px;
    border: 1px solid #e6e6e6;
    background: #fff;
    cursor: pointer;
    border-radius: 5px;
    font-size: 14px;
}

.option-buttons button.active {
    border-color: #f4b400;
    background: #f4b400;
    color: #fff;
    font-weight: bold;
}

/* Quantity section */
.quantity-section {
    display: flex;
    align-items: center;
    margin-right: 10px;

}

.quantity-section button {
    padding: 10px 15px;
    border: 1px solid #e6e6e6;
    background: #fff;
    cursor: pointer;
    border-radius: 5px;

}

.quantity-input {
    width: 50px;
    text-align: center;
    margin: 0 10px;
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 10px 15px;
}

/* Purchase */
.purchase_wrraper {
    display: flex;
    border-bottom: 1px solid #ddd;
    padding-bottom: 20px;
}

.purchase {
    display: flex;
}

.purchase button {
    padding: 10px 15px;
    margin: 0px 20px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-weight: bold;
}

.addToCart {
    background-color: var(--bg-btn);
    color: #fff;
}

.buy-now {
    background: #b12704;
    color: #fff;
}

.tabs {
    margin-top: 20px;
    border-bottom: 1px solid var(--border);
}

.tab-content {
    margin-top: 20px;
    font-size: 14px;
    color: #555;
    line-height: 1.8;
}

.additional-info {
    font-size: 14px;
    margin-top: 20px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    text-align: left;
}

.additional-info p {
    padding-bottom: 10px;
}

/* Responsive Styles */
@media (max-width: 768px) {
    footer {
        margin-top: 0px;

    }

    .reviews {
        text-align: center;
        margin-top: 0;
    }

    .related-products {
        margin-top: 0px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .product-detail {
        flex-direction: column;
        align-items: center;
    }

    .product-images,
    .product-info {
        flex: none;
        width: 100%;
    }

    .product-info h1 {
        font-size: 22px;

    }

    .price {
        font-size: 24px;

    }

    .purchase_wrraper {
        display: flex;
        flex-direction: column;
        padding-bottom: 0px;
    }

    .purchase {
        margin: 20px 0px;
    }

    .purchase button {
        margin-left: 0px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .quantity-section {
        padding-bottom: 20px;
        border-bottom: 1px solid #ddd;
    }

    .wishlist {
        justify-content: center;
    }

    .tabs {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .thumbnail-images img {
        width: 50px;
        height: 50px;
    }


}

.loading,
.error {
    text-align: center;
    font-size: 1.2rem;
    margin-top: 2rem;
}

@media (max-width: 500px) {
    .productPageImagesBar {
        display: none;
    }

    .productPageFullImage {
        position: relative;
        max-width: 500px;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .productPageImgContainer {
        align-items: flex-start;
        flex-direction: column-reverse;
    }
}

@media (min-width: 768px) {
    .productPageContainer {
        flex-direction: row;
    }

    .productPageImgContainer {
        flex-direction: column;
        flex: 1;
    }

    .productPageInfoContainer {
        flex: 1;
    }

    .productPageImagesBar {
        align-items: center;
    }
}
</style>
