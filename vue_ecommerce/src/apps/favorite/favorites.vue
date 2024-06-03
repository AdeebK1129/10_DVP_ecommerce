<template>
    <div class="container mt-5">
    <h2 class="mb-4">Your Favorites</h2>
    <div class="row">
    <span v-for="favorite in favorites">
        <div class="col-md-3">
            <div class="card mb-4 shadow-sm">
                <img src="{{ favorite.product.image }}" class="card-img-top" alt="{{ favorite.product_name }}">
                <div class="card-body">
                    <h5 class="card-title">{{ favorite.product_name }}</h5>
                    <p class="card-text">${{ favorite.product.price }}</p>
                    <a href="{% url 'shop:product_show' favorite.product_id %}" class="btn btn-primary btn-block">View Product</a>
                    <button @click="removeFavorite(favorite.product_id)" class="btn btn-danger btn-block">Remove from Favorites</button>
                </div>
            </div>
        </div>
    </span>
    </div>
</div>
</template>

<script>
export default {
    name: 'Favorites',
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
            }
        },
    methods: {
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
    }
}
</script>