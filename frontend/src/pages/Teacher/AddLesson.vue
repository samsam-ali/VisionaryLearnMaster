<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div>
                <h3>Add Lesson</h3>
                <hr/>
            </div>
            <form @submit.prevent="addLesson" class="mt-4">
                <div class="mb-3">
                    <label for="course" class="form-label">Course</label>
                    <select v-model="selectedCourse" id="course" class="form-select">
                        <option value="">Select Course</option>
                        <option v-for="course in courses" :key="course.id" :value="course.id">{{ course.title }}</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="lessonTitle" class="form-label">Lesson Title</label>
                    <input type="text" v-model="lessonTitle" class="form-control" required>
                </div>
                <div v-for="(topic, index) in topics" :key="index">
                    <hr>
                    <h5>Topic {{ index + 1 }}</h5>
                    <div class="mb-3">
                        <label class="form-label">Title</label>
                        <input type="text" v-model="topic.title" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Text</label>
                        <input type="text" v-model="topic.text" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Image</label><br>
                        <input type="file" class="form-control-file" accept="image/*" @change="handleImageUpload($event,index)">
                    </div>
                </div>
                <button @click.prevent="addTopic" class="btn btn-secondary mb-3">Add Topic</button>
                <button type="submit" class="btn btn-primary mb-3">Submit</button>
            </form>

            <!-- Preview Section -->
            <div v-if="lessonTitle && topics.length > 0" class="mt-4">
                <h4>Lesson Preview</h4>
                <main class="lesson-container">
                    <h1 tabindex="0">{{ lessonTitle }} - Lesson Topics</h1>
                    <div v-for="(topic, index) in topics" :key="index" class="topic-card">
                        <h2 tabindex="0">{{ topic.title }}</h2>
                        <div>
                            <img :src="topic.imageUrl" :alt="'Image showing: ' + topic.captionText" class="topic-image" tabindex="0">
                            <p>Image showing: {{ topic.captionText }}</p>
                        </div>
                        <p class="topic-text" tabindex="0">{{ topic.text }}</p>
                    </div>
                </main>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            courses: [],
            selectedCourse: '',
            lessonTitle: '',
            topics: [{ 
                title: '', 
                image: null,
                imagecaptionId: null, 
                captionText: '',
                imageUrl: '',
                text: '',
            }], 
        };
    },
    created(){
        this.get_courses();
    },
    methods: {
        get_courses(){
            axios.get('get_courses')
                .then(response => {
                    this.courses = response.data;
                })
                .catch(error => {
                    console.error('Error fetching courses:', error);
                });
        },
        addTopic() {
            this.topics.push({ title: '' });
        },
        async addLesson() {
            try {
                // First, create the lesson
                const lessonResponse = await axios.post('add_lesson', {
                    course: this.selectedCourse,
                    title: this.lessonTitle,
                });
                const lessonId = lessonResponse.data.id;
                

                // Then, create each topic associated with the lesson
                for (const topic of this.topics) {
                    try {
                        const formData = new FormData();
                        formData.append('image', topic.image);
                        
                        // Get CSRF token from cookie
                        const csrfToken = this.getCookie('csrftoken');

                        const response = await axios.post('/add-image-caption/', formData, {
                            headers: {
                                'Content-Type': 'multipart/form-data',
                                'X-CSRFToken': csrfToken, // Include CSRF token in the request headers
                            },
                        });
                        topic.imagecaptionId = response.data.id;
                        topic.captionText = response.data.caption;
                        topic.imageUrl = topic.image ? URL.createObjectURL(topic.image) : '';

                        await axios.post('add_topic', {
                            lesson: lessonId,
                            title: topic.title,
                            imagecaption: topic.imagecaptionId,
                            text: topic.text,
                        });
                    } catch (error) {
                        console.error('Error uploading image:', error);
                        alert("Error adding lesson")
                    }
                }
                console.log("Lesson and topics added successfully!");
            } catch (error) {
                console.error('Error adding lesson and topics:', error);
                alert("Error adding lesson")
            }
        },
        handleImageUpload(event,index) {
            const selectedFile = event.target.files[0];
            this.topics[index].image = selectedFile;
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
