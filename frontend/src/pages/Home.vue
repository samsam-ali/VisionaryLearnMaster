<!-- <template>
    <div class="container mt-5">
        <div class="row">
            <img src="../assets/grad.jpg" alt="background">
            <div class="col-md-6 offset-md-3 text-center">
            <h1 v-if="$store.state.token" class="display-4" tabindex="0">Hi {{ first_name }} {{ last_name }}! Welcome to VisionaryLearn. You are a {{ role }}!</h1>
            <h1 v-if="!$store.state.token" class="display-4" tabindex="0">Welcome to VisionaryLearn!<br> You are not logged in</h1>
            <p class="lead" tabindex="0">Empowering learners to achieve their dreams</p>
            <p tabindex="0">At VisionaryLearn, we believe in providing high-quality education and resources to help you succeed.</p>
            <p tabindex="0">Get started on your learning journey today!</p>
            <router-link to="/Dashboard" class="btn btn-primary btn-lg">Get Started</router-link>
            </div>
        </div>
    </div>
</template> -->
<template>
    <div id="background-row">
        <div class="container">
            <div class="row">
                <div class="col-md-6 offset-md-3 text-center">
                    <h1 v-if="$store.state.token" class="display-4" tabindex="0">
                        Hi {{ first_name }} {{ last_name }}! Welcome to VisionaryLearn. You are a {{ role }}!
                    </h1>
                    <h1 v-else class="display-4" tabindex="0">
                        Welcome to VisionaryLearn!<br> You are not logged in
                    </h1>
                    <p class="lead" tabindex="0">Empowering learners to achieve their dreams</p>
                    <p tabindex="0">At VisionaryLearn, we believe in providing high-quality education and resources to help you succeed.</p>
                    <p tabindex="0">Get started on your learning journey today!</p>
                    <router-link to="/Dashboard" class="btn btn-primary btn-lg">Get Started</router-link>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios'

    export default {
        name: 'Home',
        data(){
            return{
                user:null,
                role: '',
                first_name: '',
                last_name: '',
            }
        },
        mounted(){
            

            if(this.$store.state.token){
                this.get_user();
                this.role = localStorage.getItem('role');
                console.log("role:"+this.role)
                console.log("localStorage:"+localStorage.getItem('role'))
                responsiveVoice.speak("You are in the home page");
            }
            else{
                responsiveVoice.speak("Welcome to VisionaryLearn! You are not logged in");
            }
            
        },
        methods: {
            async get_user(){
                const response = await axios.get('get_user');
                this.user = response.data;

                this.first_name = this.user.first_name;
                this.last_name = this.user.last_name;
            }
        }
        
        }
</script>
  
<style scoped>
#background-row {
    /* background-image: url('../assets/grad.jpg'); */
    background-image: linear-gradient(rgba(255, 253, 240, 0.4), rgba(255, 248, 216, 0.4)), url(../assets/grad.jpg);
    background-size: cover;
    background-position: center;
    color: white;
    padding: 100px 0;
}

.text-center {
    text-align: center;
}

#background-row .col-md-6 {
    background-color: rgba(0, 0, 0, 0.8);
    padding: 20px;
    border-radius: 10px;
}

@media (max-width: 768px) {
    #background-row {
        padding: 50px 0;
    }
}
</style>