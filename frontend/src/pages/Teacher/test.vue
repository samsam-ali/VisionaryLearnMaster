<template>
    <div>
      <input type="file" @change="handleFileUpload" />
      <button @click="uploadImage">Upload</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
        return {
            selectedFile: null,
        };
    },
    methods: {
      handleFileUpload(event) {
        this.selectedFile = event.target.files[0];
      },
      async uploadImageBackup() {
        try {
          const formData = new FormData();
          formData.append('image', this.selectedFile);
          
  
          const response = await axios.post('/add-image-caption', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
  
          console.log(response.data);
          // Do something with the response data
        } catch (error) {
          console.error('Error uploading image:', error);
          // Handle error
        }
      },
      async uploadImage() {
        try {
            const formData = new FormData();
            formData.append('image', this.selectedFile);

            // Get CSRF token from cookie
            const csrfToken = this.getCookie('csrftoken');

            const response = await axios.post('/add-image-caption/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': csrfToken, // Include CSRF token in the request headers
                },
            });

            console.log(response.data);
            // Do something with the response data
        } catch (error) {
            console.error('Error uploading image:', error);
            // Handle error
        }
    },
    
    getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}

    
  };
  </script>
  