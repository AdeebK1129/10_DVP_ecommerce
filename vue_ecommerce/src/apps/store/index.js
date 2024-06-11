import {createStore } from 'vuex'
export default createStore({
    state: {
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: '',
        isLoading: false,


    },
    mutations: {
        initializeStore(state){
            if(localStorage.getItem('cart')){
                state.cart = JSON.parse(localStorage.getItem('cart'));
            }
            else{
                localStorage.setItem('cart'), JSON.stringify(state.cart)
            }
        }
    },
    addtoCart(state, item){
        const exists = state.cart.items.filter
    }


})