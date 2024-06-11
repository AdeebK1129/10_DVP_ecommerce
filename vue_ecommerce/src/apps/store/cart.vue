<template>
    <div class="container">
      <h2>Your Cart</h2>
      <div class="row">
        <div v-for="item in cart" :key="item.id" class="col-md-3">
          <div class="card mb-4 shadow-sm">
            <div class="card-body">
              <h5 class="card-title">{{ cart.product.title }}</h5>
              <p class="card-text">Price: ${{ cart.product.price }}</p>
              <p class="card-text">Category: {{ cart.product.category }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Cart',
    data() {
      return {
        cart: cart,
      };
    },
    methods: {
      removeItem(itemID) {
        fetch(`/remove-item/${itemID}/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken') // Get CSRF token from cookies
          }
        })
        .then(response => {
          if (response.ok) {
            // If removal is successful, update the favorites list
            this.cart = this.cart.filter(item => item.id !== itemID);
          } else {
            console.error('Error removing cart item');
          }
        })
        .catch(error => {
          console.error('Error removing cart item:', error);
        });
      },
      getCookie(name) {
        const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
        return cookieValue ? cookieValue.pop() : '';
      }
    }
  };
  </script>
  