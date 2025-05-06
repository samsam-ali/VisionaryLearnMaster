<template>
    <div class="row justify-content-center" id="background-row">
        <div class="col-md-6">
            <div >
                <h3>
                    Login here:
                    <hr/>
                </h3>
            </div>
            <form @submit.prevent="login" class="mt-4">
                <div class="mb-3">
                    <label for="username" class="form-label">Username</label>
                    <input type="text" v-model="username" class="form-control" aria-label="Enter your username">
                </div>
                <div class="mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" aria-label="Enter your password">
                </div>
                <button type="submit" class="btn btn-primary mt-2">Submit</button>
                <h3 v-if="unsuccessful" tabindex="0">
                    Login unsuccessful! Please login again!
                </h3>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import router from '../router';

export default {
    data() {
        return {
            username: '',
            password: '',
            role: '',
            user: null,
            unsuccessful: false,
        };
    },
    mounted() {

        responsiveVoice.speak("Enter your username and password to login");
    },
    methods: {

        async get_role(){
            if (this.user.role === 'STUDENT') {
                this.role = 'student';
            } else if (this.user.role === 'TEACHER') {
                this.role = 'teacher';
            }
        },
        async login() {
            try {
                const response = await axios.post('login', {
                    username: this.username,
                    password: this.password
                });

                if (response.status === 200) {
                    this.$store.commit('login', response.data.token);
                    console.log("Login successful!");
                    localStorage.setItem('token', response.data.token);
                    console.log("Local Storage Token: " + localStorage.getItem('token'));

                    
                    // Retrieve user only after successful login
                    // const responseUser = await axios.get('get_user');
                    const responseUser = await axios.get('get_user', {
                        headers: {
                            'Authorization': `token ${localStorage.getItem('token')}`
                        }
                    });
                    this.user = responseUser.data;
                    // responsiveVoice.speak("Login successful");
                    
                    await this.get_role(); // Wait for get_role() to finish
                    
                    localStorage.setItem('role', this.role);
                    
                    window.location.reload();
                    
                } else {
                    console.log("Login unsuccessful, couldn't get user");
                    responsiveVoice.speak("Unsuccessful Login, please try again")
                    // alert("Login Unsuccessful, couldn't get user");
                    this.unsuccessful = true;

                }
            } catch (error) {
                console.error('Login unsuccessful', error);
                responsiveVoice.speak("Unsuccessful Login, please try again")
                // alert("Login Unsuccessful");
                this.unsuccessful = true;
            }
        },

        async loginbackup() {
            try {
                const response = await axios.post('login', {
                    username: this.username,
                    password: this.password
                    
                }).then((response) =>{
                    if(response.status == 200) {

                        this.$store.commit('login', response.data.token);
                        console.log("login successful!");

                        localStorage.setItem('token', response.data.token);
                        console.log("localstorage:"+localStorage.getItem('token'));

                        
                    }

                });
                
            } catch (error) {
                console.log("User: "+this.username + this.password)
                console.error('Login unsuccessful', error);
                alert("Login Unsuccessful")
            }

            const responseUser = await axios.get('get_user');
            this.user = responseUser.data;
            this.get_role();
            

            localStorage.setItem('role', this.role);
            this.$router.push('/');
            // window.location.reload();
        },
        

        resetForm() {
            // Reset form data
            this.username = '';
            this.password = '';
        },

        
    },
};
</script>

<style scoped>
#background-row {
    background-image: linear-gradient(rgb(247, 247, 247), rgb(255, 253, 206)); /* Gradient from light gray to dark gray */
    color: white;
    padding: 50px 0;
    height: auto;
}

.col-md-6 {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 10px;

}

@media (max-width: 768px) {
    #background-row {
        padding: 50px 0;
    }
}
</style>