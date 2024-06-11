<template>
  <div class="container">
    <h2>Your Favorites</h2>
    <div class="row">
      <div v-for="favorite in favorites" :key="favorite.id" class="col-md-3">
        <div class="card mb-4 shadow-sm">
          <div class="card-body">
            <h5 class="card-title">{{ favorite.product.title }}</h5>
            <p class="card-text">Price: ${{ favorite.product.price }}</p>
            <p class="card-text">Category: {{ favorite.product.category }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Favorites',
  data() {
    return {
      favorites: favorites, 
    };
  },
  methods: {
    removeFavorite(favoriteId) {
      fetch(`/remove-favorite/${favoriteId}/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getCookie('csrftoken') // Get CSRF token from cookies
        }
      })
      .then(response => {
        if (response.ok) {
          // If removal is successful, update the favorites list
          this.favorites = this.favorites.filter(favorite => favorite.id !== favoriteId);
        } else {
          console.error('Error removing favorite item');
        }
      })
      .catch(error => {
        console.error('Error removing favorite item:', error);
      });
    },
    getCookie(name) {
      const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
      return cookieValue ? cookieValue.pop() : '';
    }
  }
};
</script>
