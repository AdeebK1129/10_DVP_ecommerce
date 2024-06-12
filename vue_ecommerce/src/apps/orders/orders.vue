<template>
    <div class="container">
      <h2>Your Orders</h2>
      <div class="row">
        <div class="col-md-3" v-for="order in orders" :key="order.id">
          <div class="card mb-4 shadow-sm h-100">
            <div class="card-body d-flex flex-column">
              <h5 class="card-title">Order ID: {{ order.id }}</h5>
              <p class="card-text">Order Date: {{ order.order_date }}</p>
              <p class="card-text">Products: {{ order.products }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        orders: [],
      };
    },
    methods: {
      fetchOrders() {
        this.orders = window.ordersData;
      },
    },
    mounted() {
      this.fetchOrders();
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  .card {
    margin-bottom: 20px;
  }
  </style>
  