<template>
    <div class="dashboard">
        <h1 tabindex="0" class="mb-4">My courses:</h1>
        <div class="row">
            <div v-for="course in courses" :key="course.id" class="col-md-4 mb-4">
                <div class="card h-100">
                    <img :src="course.imageUrl" :alt="course.caption" class="card-img-top" style="height: 200px; object-fit: cover;">
                    <div class="card-body">
                        <h5 class="card-title">{{ course.title }}</h5>
                        <a :href="'/courses/' + course.id + '/lessons'" class="btn btn-primary" :aria-label="'View Course: ' + course.title">View Course</a>
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
            courses: [],
            baseUrl: 'http://localhost:8000',
            imagecaption: null,
            speakDelayed: false,
        };
    },
    mounted() {
        this.getCourses();
        setTimeout(() => {
            if (!this.speakDelayed) {
                responsiveVoice.speak("You are in dashboard");
                this.speakDelayed = true;
            }
        }, 500);
        
    },
    methods: {
        async getCourses() {
            try {
                const response = await axios.get('get_courses');
                const coursesData = response.data;
                // Preload image URLs for each course
                const coursesWithImages = await Promise.all(coursesData.map(async course => {
                    try {
                        const imageResponse = await axios.get(`/get_imagecaption/${course.imagecaption}/`);
                        const imagecaption = imageResponse.data;
                        const imageUrl = this.baseUrl + imagecaption.image;
                        const caption = imagecaption.caption;
                        // Add imageUrl property to course object
                        return { ...course, imageUrl, caption };
                    } catch (error) {
                        console.error('Error fetching imagecaption:', error);
                        // If fetching fails, return the course object with placeholder image URL
                        return { ...course, imageUrl: this.placeholderImage };
                    }
                }));
                // Set the courses data with preloaded image URLs
                this.courses = coursesWithImages;
                console.log(coursesWithImages)
            } catch (error) {
                console.error('Error fetching courses:', error);
            }
        },
        async getCoursesBackup() {
            try {
                const response = await axios.get('get_courses');
                this.courses = response.data;
            } catch (error) {
                console.error('Error fetching courses:', error);
            }
        },
        async getCourseImageUrlBackup(course) {
            try{
                const response = await axios.get(`/get_imagecaption/${course.imagecaption}/`);
                this.imagecaption = response.data;
            } catch (error) {
                console.error('Error fetching imagecaption:', error);
            }
            
            return this.baseUrl + this.imagecaption.image;
        },
        async getCourseImageUrl(imageUrl) {
            return this.baseUrl + imageUrl;
        }

    }
};
</script>
  
<style>
.dashboard {
    max-width: 800px;
    margin: 0 auto;
}

.course-list {
    margin-top: 20px;
}

.course {
    margin-bottom: 20px;
}

.course-image {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
}

.course-container {
    display: flex;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    background-color: #f9f9f9;
}

.course-details {
    padding: 20px;
}

.course-details h2 {
    margin-top: 0;
    margin-bottom: 10px;
}

.course-details p {
    margin-bottom: 10px;
}

.btn {
    display: inline-block;
    padding: 8px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-decoration: none;
}

.btn:hover {
    background-color: #0056b3;
}
</style>