<template>
    <div class="product-container">
        <div class="product-image-gallery">
            <img :src="product.image" alt="Product Image" class="main-image" />
            <div class="thumbnail-container">
                <img v-for="(image, index) in thumbnailImages" :key="index" :src="image" alt="Thumbnail" class="thumbnail-image" />
            </div>
        </div>
        <div class="product-details">
            <h1 class="product-price">${{ product.price }}</h1>
            <h2 class="product-title">{{ product.title }}</h2>
            <p class="product-description">{{ product.description }}</p>
            <div class="action-buttons">
                <button @click="toggleFavorite" :class="['favorite-button', isFavorite ? 'favorited' : '']">
                    {{ isFavorite ? 'Remove from Favorites' : 'Add to Favorites' }}
                </button>
                <button class="order-now-button">Order Now</button>
            </div>
            <div class="quantity-selector">
                <button @click="decreaseQuantity" class="quantity-button">-</button>
                <input type="number" v-model="quantity" min="1" class="quantity-input" />
                <button @click="increaseQuantity" class="quantity-button">+</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductShow',
    data() {
        return {
            product: {},
            quantity: 1,
            isFavorite: false,
            product_show_json_url: ext_product_show_json_url,
            add_to_favorites_url: ext_add_to_favorites_url,
            remove_from_favorites_url: ext_remove_from_favorites_url,
            csrfToken: ext_csrf_token,
            thumbnailImages: [] // Assuming we have multiple images for thumbnails
        };
    },
    methods: {
        fetchProductDetails() {
            fetch(this.product_show_json_url, {
                method: 'get',
                credentials: 'same-origin',
            })
                .then(response => response.json())
                .then(data => {
                    this.product = data.product;
                    this.thumbnailImages = [data.product.image]; // Update with actual thumbnail images
                })
                .catch(error => {
                    console.error('Error fetching product details:', error);
                });
        },
        toggleFavorite() {
            this.isFavorite = !this.isFavorite;
            const url = this.isFavorite ? this.add_to_favorites_url : this.remove_from_favorites_url;
            fetch(url, {
                method: 'post',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrfToken,
                },
                body: JSON.stringify({ product_name: this.product.title }),
            }).then(response => {
                if (!response.ok) {
                    console.error('Error updating favorite status');
                }
            });
        },
        decreaseQuantity() {
            if (this.quantity > 1) this.quantity--;
        },
        increaseQuantity() {
            this.quantity++;
        },
        addToCart() {
            // Implement the logic to add the product to the cart
            console.log(`Adding ${this.quantity} of product ${this.product.id} to cart.`);
        },
    },
    beforeMount() {
        this.fetchProductDetails();
    },
};
</script>

<style scoped>
.product-container {
    display: flex;
    justify-content: space-between;
    padding: 20px;
}

.product-image-gallery {
    flex: 1;
    margin-right: 20px;
}

.main-image {
    width: 100%;
    border: 1px solid #ccc;
    padding: 10px;
}

.thumbnail-container {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}

.thumbnail-image {
    width: 18%;
    border: 1px solid #ccc;
    padding: 5px;
    cursor: pointer;
}

.product-details {
    flex: 1;
    padding: 20px;
}

.product-price {
    font-size: 24px;
    font-weight: bold;
}

.product-title {
    font-size: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.product-description {
    margin-bottom: 20px;
}

.action-buttons {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.favorite-button,
.order-now-button {
    background-color: #000;
    color: #fff;
    padding: 10px 20px;
    margin-right: 10px;
    border: none;
    cursor: pointer;
}

.favorite-button.favorited {
    background-color: red; /* Change color when favorited */
}

.order-now-button {
    background-color: #000;
}

.quantity-selector {
    display: flex;
    align-items: center;
}

.quantity-button {
    background-color: #ccc;
    border: none;
    padding: 10px;
    cursor: pointer;
}

.quantity-input {
    width: 50px;
    text-align: center;
    margin: 0 10px;
}
</style>
