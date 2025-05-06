import axios from 'axios'
import $store from './store'

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
// axios.defaults.headers.common['Authorization'] = 'token ' + $store.state.token;
axios.defaults.headers.common['Authorization'] = 'token ' + localStorage.getItem('token');