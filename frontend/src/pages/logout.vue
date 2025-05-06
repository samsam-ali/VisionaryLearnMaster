<template>
    <div>
        <!-- <button @click="logout">Logout</button> -->
        <button v-if="$store.state.token" class="nav-link" @click="logout">Log out</button>
    </div>
</template>
  
<script>
export default {
    methods: {
        async logout() {
            this.$store.commit('logout');
            this.$store.commit('initialiseStore');
            console.log("logout");
            await responsiveVoice.speak("Logout Successful");
            window.location.reload();
        }
    }
}
</script>  

<style>
.nav-link{
    color: #424242 !important;
}

.nav-link:hover {
    color: #d4d4d4 !important;
}
</style>