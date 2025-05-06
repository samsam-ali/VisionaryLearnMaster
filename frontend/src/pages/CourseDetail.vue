<template>
    <div class="course-detail">
        <h1>{{ course.title }}</h1>
        <p>{{ course.description }}</p>
        <!-- <router-link :to="'/courses/' + course.id + '/lessons'">View Lessons</router-link> -->

        <div class="lesson-list">
            <h1>{{ course.title }} - Lessons</h1>
            <ul>
                <li v-for="lesson in lessons" :key="lesson.id">{{ lesson.title }}</li>
            </ul>
        </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
import LessonList from './LessonList.vue';
  
  export default {
    name: 'Course',
    
    data() {
        return {
            course: {},
            lessons: [],
        };
    },
    created() {
        this.fetchCourse();
        
    },
    methods: {
        async fetchCourse() {
            try {
                const response = await axios.get(`/get_course/${this.$route.params.id}`);
                this.course = response.data;
            }
            catch (error) {
                console.error('Error fetching course:', error);
            }
            this.fetchLessons();
        },
        async fetchLessons() {
            try {
                const response = await axios.get(`/get_lessons/${this.course.id}`);
                this.lessons = response.data;
            } catch (error) {
                console.error('Error fetching lessons:', error);
            }
        },
    },
};
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  