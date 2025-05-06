<template>
    <main class="lesson-container">
        <h1>{{ lesson.title }} Lesson</h1>
      
        <div v-for="(topic, index) in lessonTopics" :key="topic.id" class="topic-card" >
            <h2 tabindex="0">Topic {{index+1}}: {{ topic.title }}</h2>
            <div >
                <img :src="topic.imageUrl" :alt="'Image showing: ' + topic.caption" class="topic-image" tabindex="0">
            </div>
            
            <p class="topic-text" tabindex="0">{{ topic.text }}</p>
        </div>
    </main>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            lesson: {},
            lessonTopics: [],
            lessonId: this.$route.params.id,
            baseUrl: 'http://localhost:8000'
        };
    },
    created() {
        this.fetchLesson();
    },
    methods: {
        async fetchLesson() {
            try {
                const response = await axios.get(`/get_lesson/${this.lessonId}/`);
                this.lesson = response.data;
                responsiveVoice.speak("You are in "+ this.lesson.title+" lesson");
            } catch (error) {
                console.error('Error fetching lesson:', error);
            }
            this.fetchLessonTopics();
        },
        async fetchLessonTopicsBackup() {
            try{
                axios.get(`/get_lesson_topics/${this.lessonId}/`)
                .then(response => {
                    this.lessonTopics = response.data;
                    // console.log(this.lessonTopics);
                    console.log('Lesson Topics:', this.lessonTopics);
                })
                .catch(error => {
                    console.error(error);
                });
            }
            catch (error) {
                console.error('Error fetching lesson topics:', error);
            }
            
        },
        async fetchLessonTopics() {
            try {
                const response = await axios.get(`/get_lesson_topics/${this.lessonId}/`);
                const topicsData = response.data;
                // Preload image URLs for each topic
                const topicsWithImages = await Promise.all(topicsData.map(async topic => {
                    try {
                        const imageResponse = await axios.get(`/get_imagecaption/${topic.imagecaption}/`);
                        const imagecaption = imageResponse.data;
                        const imageUrl = this.baseUrl + imagecaption.image;
                        const caption = imagecaption.caption;
                        
                        return { ...topic, imageUrl, caption };
                    } catch (error) {
                        console.error('Error fetching imagecaption:', error);
                        // If fetching fails, return the topic object with placeholder image URL
                        return { ...topic, imageUrl: this.placeholderImage };
                    }
                }));
                // Set the topics data with preloaded image URLs
                this.lessonTopics = topicsWithImages;
                console.log(topicsWithImages)
            } catch (error) {
                console.error('Error fetching topics:', error);
            }
        },
        getTopicImageUrl(imageFilename) {
            return this.baseUrl + imageFilename;
        }
    }
};
</script>

<style>
.lesson-container {
    max-width: 800px;
    margin: 0 auto;
}

.topic-card {
    margin-bottom: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.topic-card h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.topic-image {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
}

.topic-text {
    font-size: 16px;
}
</style>