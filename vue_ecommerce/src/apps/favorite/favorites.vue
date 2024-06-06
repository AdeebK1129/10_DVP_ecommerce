<template>
    <div class="favorites-container">
      <h2>Your Favorites</h2>
      <div class="favorite-product" v-for="favorite in favorites" :key="favorite.id">
        <div class="product-info">
          <h3>{{ favorite.title }}</h3>
          <p>Price: ${{ favorite.price }}</p>
          <button @click="removeFromFavorites(favorite.id)">Remove from Favorites</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Favorites',
    data() {
      return {
        favorites: [] // Array to store user's favorite products
      };
    },
    created() {
      this.fetchFavoritesFromBackend();
    },
    methods: {
      fetchFavoritesFromBackend() {
        fetch('/fetch-favorites/', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken') // Get CSRF token from cookies
          },
        })
        .then(response => response.json())
        .then(data => {
          this.favorites = data.favorites;
        })
        .catch(error => {
          console.error('Error fetching favorites:', error);
        });
      },
      getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      },
      removeFromFavorites(productId) {
        fetch(`/remove-from-favorites/${productId}/`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken') // Get CSRF token from cookies
          },
        })
        .then(response => {
          if (response.ok) {
            this.favorites = this.favorites.filter(favorite => favorite.id !== productId);
          } else {
            console.error('Failed to remove from favorites');
          }
        })
        .catch(error => {
          console.error('Error removing from favorites:', error);
        });
      },
    }
  };
  </script>
  
  <style scoped>
  </style>
  