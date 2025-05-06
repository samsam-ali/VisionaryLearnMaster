<template>
    <!-- <nav @dblclick="readWebpage" class="navbar navbar-expand-lg navbar-dark bg-info"> -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-info">
        <div class="container">
            <!-- Logo on the far left -->
            <router-link class="navbar-brand" :to="{ name: 'Home' }" aria-label="VisionaryLearn">
            <img src="../assets/VisionaryLearn-logos_transparent.png" alt="VisionaryLearn logo" width="125" height="50">
            </router-link>
    
            <!-- Toggler button for small screens -->
            <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
            >
            <span class="navbar-toggler-icon"></span>
            </button>
    
            <!-- Navbar links on the far right -->
            <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                <router-link v-if="$store.state.token" class="nav-link" :to="{ name: 'Home' }">Home</router-link>
                </li>
                <li class="nav-item">
                <router-link v-if="isStudent()" class="nav-link" :to="{ name: 'Dashboard' }">Dashboard</router-link>
                </li>
                <li class="nav-item">
                <router-link v-if="isTeacher()" class="nav-link" :to="{ name: 'AddCourse' }">Add Course</router-link>
                </li>
                <li class="nav-item">
                <router-link v-if="isTeacher()" class="nav-link" :to="{ name: 'AddLesson' }">Add Lesson</router-link>
                </li>
                <li class="nav-item">
                <router-link v-if="isTeacher()" class="nav-link" :to="{ name: 'AddAssignment' }">Add Assignment</router-link>
                </li>
                <li class="nav-item">
                <router-link v-if="!$store.state.token" class="nav-link" :to="{ name: 'Login' }">Login</router-link>
                </li>
                <li class="nav-item">
                <!-- <button v-if="$store.state.token" class="nav-link" @click="logout">Log out</button> -->
                <Logout />
                </li>
                <li class="nav-item">
                <router-link v-if="!$store.state.token" class="nav-link" :to="{ name: 'Signup' }">Register</router-link>
                </li>
                
            </ul>
            </div>
        </div>
    </nav>
    <RouterView />
</template>
  
<script>
import $store from '../store/index';
import Logout from '../pages/logout.vue'; 

    export default {
        name: 'Navbar',
        components: {
            Logout
        },
        data() {
            return {
                role: localStorage.getItem('role'),
            };
        },
        methods: {
            logout() {
                this.$store.commit('logout');
                this.$store.commit('initialiseStore');
                console.log("logout");
                // this.$router.push('/');
                window.location.reload();
            },
            readWebpage() {
                const webpageContent = document.body.innerText;

                responsiveVoice.speak(webpageContent);
            },
            isTeacher() {
                return this.role === 'teacher';
            },
            isStudent() {
                return this.role === 'student';
            },
        },
        created() {
            this.$store.commit('initialiseStore');
            
        },
        mounted() {
            // this.$store.commit('initialiseStore');
            // const script = document.createElement('script');
            // script.src = 'https://code.responsivevoice.org/responsivevoice.js?key=XXXXXXXX';
            // document.head.appendChild(script);
            
        },
        
    }
</script>


<style scoped>
/* Monochromatic light color scheme */
.navbar {
    background-color: rgb(247, 247, 247) !important;
}

.navbar-nav .nav-link{
    color: #424242 !important;
}

.navbar-nav .nav-link:hover {
    color: #d4d4d4 !important;
}

</style>
  

