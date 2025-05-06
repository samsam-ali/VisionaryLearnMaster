import { createStore } from 'vuex';

const store = createStore({
    state: {
        token: null,
        // role: null,
    },
    mutations: {
        login(state, token) {
            state.token = token;
            // state.role = role;
            localStorage.setItem('token', token);
            // localStorage.setItem('role', role);
        },
        logout(state) {
            state.token = null;
            // state.role = null;
            localStorage.removeItem('token');
            localStorage.removeItem('role');
        },
        initialiseStore(state) {
            if(localStorage.getItem('token')) {
                state.token = localStorage.getItem('token');
                // state.role = localStorage.getItem('role');
            }
        }
    },
    actions: {
        
    },
    getters: {
        
    },
});

export default store;