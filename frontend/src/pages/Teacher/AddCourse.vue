<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div>
                <h3 tabindex="0" class="mt-4">
                    Add Course here:
                    <hr/>
                </h3>
            </div>
            <form @submit.prevent="add_course" class="mt-4 mb-5">
                <div class="mb-3">
                    <label for="title" class="form-label">Title</label>
                    <input type="text" v-model="title" class="form-control" aria-label="Enter course title:">
                </div>
                <div class="mb-3">
                    <label for="teacher" class="form-label">Teacher</label>
                    <select v-model="selectedTeacher" id="teacher" class="form-select">
                        <option value="">Select Teacher</option>
                        <option v-for="teacher in teachers" :key="teacher.id" :value="teacher.id">{{ teacher.first_name }} {{ teacher.last_name }}</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="image" class="form-label">Image</label><br>
                    <input type="file" id="image" class="form-control-file" accept="image/*" @change="handleImageUpload">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>

            <!-- Preview Section -->
            <div v-if="previewCourse" class="mt-4">
                <h4>Preview</h4>
                <div class="card">
                    <img :src="previewCourse.imageUrl" :alt="'Image showing:' + previewCourse.caption" class="card-img-top" style="height: 200px; object-fit: cover;" tabindex="0">
                    <div class="card-body">
                        <h5 class="card-title">{{ previewCourse.title }}</h5>
                        <p>Image showing: {{ previewCourse.caption }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            selectedTeacher: '',
            teachers: [],
            title: '',
            selectedFile: null,
            imageCaption: null,
            captionText: '',
            previewCourse: null,
        };
    },
    created(){
        this.fetchTeachers();
    },
    methods: {
        updatePreview() {
            this.previewCourse = {
                title: this.title,
                imageUrl: this.selectedFile ? URL.createObjectURL(this.selectedFile) : '',
                caption: this.captionText, 
            };
        },
        fetchTeachers(){
            axios.get('get_teachers')
                .then(response => {
                    this.teachers = response.data;
                })
                .catch(error => {
                    console.error('Error fetching teachers:', error);
                });
        },
        async image_caption(){
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
                this.imageCaption = response.data.id;
                console.log(response.data);
            } catch (error) {
                console.error('Error uploading image:', error);
            }
        },
        
        async add_course(){
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
                this.imageCaption = response.data.id;
                this.captionText = response.data.caption;
                console.log(response.data);

                try{
                    const response = await axios.post('add_course', {
                        title: this.title,
                        teacher: this.selectedTeacher,
                        imagecaption: this.imageCaption,
                    }).then((response) => {
                        if(response.status == 201){
                            console.log("Created course successfully!")
                            // console.log(response)
                        }
                    })
                    this.updatePreview();
                }
                catch (error) {
                    console.error('Course was not created:', error);
                    alert("Error adding course")
                }

            } catch (error) {
                console.error('Error uploading image:', error);
                alert("Error uploading image")
            }
            
        },
        handleImageUpload(event) {
            this.selectedFile = event.target.files[0] 
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
        
    },
};
</script>