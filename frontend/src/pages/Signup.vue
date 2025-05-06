<template>
    <div id="background-row">
        <div class="row justify-content-center " id="background-row">
            <div class="col-md-6">
                <div>
                    <h3>
                        Register here:
                        <hr/>
                    </h3>
                </div>
                <form @submit.prevent="signup" class="mt-4">
                    <div class="mb-3">
                        <label for="first_name" class="form-label">First Name</label>
                        <input type="text" v-model="first_name" class="form-control" aria-label="Enter your first name">
                    </div>
                    <div class="mb-3">
                        <label for="last_name" class="form-label">Last Name</label>
                        <input type="text" v-model="last_name" class="form-control" aria-label="Enter your last name">
                    </div>
                    <div class="mb-3">
                        <label for="username" class="form-label">Username</label>
                        <input type="text" v-model="username" class="form-control" aria-label="Enter your username">
                    </div>
                    <div class="mb-3">
                        <label for="email" class="form-label">Email</label>
                        <input type="email" v-model="email" class="form-control" aria-label="Enter your email address">
                    </div>
                    <div class="mb-3">
                        <label for="password" class="form-label">Password</label>
                        <input type="password" v-model="password" class="form-control" aria-label="Enter your password">
                    </div>
                    <!-- <div class="mb-3">
                        <label for="role" class="form-label" >Role</label>
                        <select v-model="role" class="form-control" aria-label="Select your role">
                            <option value="STUDENT" label="Student">Student</option>
                            <option value="TEACHER" label="Teacher">Teacher</option>
                        </select>
                    </div> -->
                    <div class="mb-3">
                        <label class="form-label">Role</label>
                        <div tabindex="0" aria-label="Select role student" @keypress.enter="selectRole('STUDENT')">
                            <input type="radio" id="student" value="STUDENT" v-model="role" :tabindex="-1">
                            <label for="student">Student</label>
                        </div>
                        <div tabindex="0" aria-label="Select role teacher" @keypress.enter="selectRole('TEACHER')">
                            <input type="radio" id="teacher" value="TEACHER" v-model="role" :tabindex="-1">
                            <label for="teacher">Teacher</label>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <h3 v-if="unsuccessful" tabindex="0">
                        Register unsuccessful! Please register again!
                    </h3>
                </form>
            </div>
        </div>
    </div>
    
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: '',
            password: '',
            first_name: '',
            last_name: '',
            email: '',
            role: '',
            unsuccessful: false,
        };
    },
    mounted() {

        responsiveVoice.speak("You are in the register page");
    },
    methods: {
        get_url(role) {
            if (role === 'STUDENT') {
                return 'http://127.0.0.1:8000/api/signup_student';
            } else if (role === 'TEACHER') {
                return 'http://127.0.0.1:8000/api/signup_teacher';
            }
        },
        selectRole(role) {
            this.role = role;
        },
        async signup() {
            try {
                const url = this.get_url(this.role);
                const response = await axios.post(url, {
                    username: this.username,
                    password: this.password,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    role: this.role,
                })
                if(response.status == 200) {
                    this.$store.commit('login', response.data.token);
                    console.log("Signup successful!");
                    
                    localStorage.setItem('token', response.data.token);
                    
                    if (this.role === 'STUDENT') {
                        localStorage.setItem('role', 'student');
                    } else if (this.role === 'TEACHER') {
                        localStorage.setItem('role', 'teacher');
                    }
                    window.location.reload();

                } else {
                    console.log("Signup unsuccessful, couldn't assign role");
                    // alert("Signup Unsuccessful, couldn't assign role");
                    responsiveVoice.speak("Unsuccessful register, please try again")
                    this.unsuccessful = true;
                }
                
            } catch (error) {
                console.error('Signup unsuccessful', error);
                // alert("Signup Unsuccessful");
                responsiveVoice.speak("Unsuccessful Register, please try again")
                this.unsuccessful = true;
            }

            
        },

        async signupbackup() {
            try {
                const url = this.get_url(this.role);
                const response = await axios.post(url, {
                    username: this.username,
                    password: this.password,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    email: this.email,
                    role: this.role,
                }).then((response) =>{
                    if(response.status == 200) {
                        this.$store.commit('login', response.data.token);
                        console.log("Signup successful!");
                        
                        localStorage.setItem('token', response.data.token);
                        
                        this.$router.push('/');
                    }
                });
                
            } catch (error) {
                console.error('Signup unsuccessful', error);
            }

            // if (this.user.role === 'STUDENT') {
            //     localStorage.setItem('role', 'student');
            // } else if (this.user.role === 'TEACHER') {
            //     localStorage.setItem('role', 'teacher');
            // }
        }
    },
};
</script>

<style scoped>
#background-row {
    background-image: linear-gradient(rgb(247, 247, 247), rgb(255, 253, 206)); /* Gradient from light gray to dark gray */
    color: white;
    padding: 1em 0;
    
}

.col-md-6 {
    background-color: rgba(0, 0, 0, 0.5);
    padding: 2em;
    border-radius: 10px;
}

</style>