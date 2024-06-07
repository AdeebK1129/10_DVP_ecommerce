<template>
    <div class="checkout">
      <h1>Checkout Page</h1>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="name">Name:</label>
          <input type="text" id="name" v-model="name" required />
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="address">Address:</label>
          <input type="text" id="address" v-model="address" required />
        </div>
        <div>
          <label for="city">City:</label>
          <input type="text" id="city" v-model="city" required />
        </div>
        <div>
          <label for="country">Country:</label>
          <input type="text" id="country" v-model="country" required />
        </div>
        <div>
          <label for="zip">ZIP Code:</label>
          <input type="text" id="zip" v-model="zip" required />
        </div>
        <button type="submit">Submit</button>
      </form>
      <div v-if="submitted">
        <h2>Review Your Order</h2>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
        <p>Address: {{ address }}</p>
        <p>City: {{ city }}</p>
        <p>Country: {{ country }}</p>
        <p>ZIP Code: {{ zip }}</p>
        <vue-paypal-checkout 
          :amount="totalAmount" 
          currency="USD"
          :client="client"
          @payment-authorized="paymentAuthorized">
        </vue-paypal-checkout>
      </div>
    </div>
  </template>
  
  <script>
  import VuePaypalCheckout from 'vue-paypal-checkout';
  
  export default {
    components: {
      VuePaypalCheckout
    },
    data() {
      return {
        name: '',
        email: '',
        address: '',
        city: '',
        country: '',
        zip: '',
        submitted: false,
        totalAmount: 0.01, // Example total amount
        client: {
          sandbox: 'AXaQRBhdOpEM2tZwNo-X_0hrOpdKHRBUvImQcMF4WQDC-s6dsAOUv-ksk8YXGTgp1et10zWsU7Btv1zu',  
        }
      };
    },
    methods: {
      handleSubmit() {
        this.submitted = true;
      },
      paymentAuthorized(data) {
        console.log('Payment Authorized!', data);
        // Handle post-payment processing here
      }
    }
  };
  </script>
  
  <style scoped>
  .checkout {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  form div {
    margin-bottom: 10px;
  }
  </style>
  