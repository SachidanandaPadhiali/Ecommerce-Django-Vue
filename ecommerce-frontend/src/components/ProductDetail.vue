<template>
    <div class="productPageContainer" v-if="product">
        <div class="productPageImgContainer">
            <div class="productPageImagesBar">
                <div v-for="(img, index) in images" :key="index" class="image"
                    :class="{ selected: selectedIndex === index }" @click="selectImage(index)">
                    <img :src="img" alt="" />
                </div>
            </div>

            <div class="productPageFullImage zoom" ref="imgZoom" :class="{ zoom: isDesktop }">
                <img :src="selectedImage" alt="Product Preview" />
            </div>
        </div>
        <div class="productPageInfoContainer">
            <div class="productPageInfo">
                <h3>{{ product.name }}</h3>
                <h3 v-if="product.stock === 0">OUT OF STOCK</h3>
                <div class="productPagePrice" v-else>
                    <span class="priceBefore">₹{{ product.price }}</span>
                    <span class="priceAfter">₹{{ product.price }}</span>
                </div>
                <div class="productPageDescription">
                    <p>{{ product.description }}</p>
                </div>
                <div class="productPageButton">
                    <button class="button"> buy now</button>
                </div>
            </div>
        </div>
    </div>

    <div v-else-if="loading" class="loading">Loading product...</div>
    <div v-else class="error">Product not found.</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ProductPage',
    data() {
        return {
            product: null,
            loading: true,
            apiUrl: `${process.env.VUE_APP_API_URL}`,
            images: [],
            selectedIndex: 0,
            selectedImage: '',
            isDesktop: window.innerWidth >= 768
        };
    },
    mounted() {
        this.selectedImage = this.images[0];
        this.selectImage(0);
        this.fetchProduct();

        const imgZoom = this.$refs.imgZoom;

        if (imgZoom) {
            imgZoom.addEventListener('mousemove', (e) => {
                const rect = imgZoom.getBoundingClientRect();
                const offsetX = e.clientX - rect.left;
                const offsetY = e.clientY - rect.top;

                imgZoom.style.setProperty('--display', 'block');
                imgZoom.style.setProperty('--zoom-x', `${(offsetX / rect.width) * 100}%`);
                imgZoom.style.setProperty('--zoom-y', `${(offsetY / rect.height) * 100}%`);
            });

            imgZoom.addEventListener('mouseleave', () => {
                imgZoom.style.setProperty('--display', 'none');
            });
        }
    },
    methods: {
        async fetchProduct() {
            const id = this.$route.params.id;
            console.log('product ID :', id);
            try {
                const response = await axios.get(`${process.env.VUE_APP_API_URL}/api/products/${id}/`);
                this.product = response.data;
                console.log('product :', response.data);
                this.images = [response.data.image];
                this.selectedImage = response.data.image;
                this.selectImage(0);
                this.loading = false;

                this.$nextTick(() => {
                    if (this.isDesktop && this.$refs.imgZoom) {
                        const imgZoom = this.$refs.imgZoom;
                        imgZoom.addEventListener('mousemove', (e) => {
                            imgZoom.style.setProperty('--display', 'block');
                            imgZoom.style.setProperty('--zoom-x', `${(e.offsetX / imgZoom.offsetWidth) * 100}%`);
                            imgZoom.style.setProperty('--zoom-y', `${(e.offsetY / imgZoom.offsetHeight) * 100}%`);
                        });
                        imgZoom.addEventListener('mouseleave', () => {
                            imgZoom.style.setProperty('--display', 'none');
                        });
                    }
                });
            } catch (error) {
                console.error('Error fetching product:', error);
                this.loading = false;
            }
        },
        selectImage(index) {
            this.selectedIndex = index;
            this.selectedImage = this.images[index];
            const imgZoom = this.$refs.imgZoom;
            if (imgZoom) {
                imgZoom.style.setProperty('--img', `url(${this.selectedImage})`);
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
    /* Adjust this to your preferred width */
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

.productPageFullImage.zoom::before {
    content: '';
    display: var(--display);
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: var(--img);
    background-size: 200%;
    background-position: var(--zoom-x) var(--zoom-y);
    pointer-events: none;
    z-index: 1;
}


.background-size .imgDots {
    display: flex;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.imgDots i {
    font-size: 12px;
    color: gray;
    cursor: pointer;
    transition: 0.3s;
}

.imgDots i.selected,
.imgDots i:hover {
    color: black;
}

.productPageInfoContainer {
    padding: 1rem;
    background: #f9f9f9;
    border-radius: 8px;
}

.productPagePrice {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    margin: 1rem 0;
}

.productPageButton {
    display: flex;
    justify-content: center;
    margin-top: 1rem;
}

.button {
    padding: 0.5rem 1.5rem;
    border: none;
    background: black;
    color: white;
    border-radius: 4px;
    cursor: pointer;
}

.loading,
.error {
    text-align: center;
    font-size: 1.2rem;
    margin-top: 2rem;
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
        flex-direction: column;
        align-items: center;
    }
}
</style>