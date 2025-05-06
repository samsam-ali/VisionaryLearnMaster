<template>
    <div class="lesson-list">
        <div class="course-header">
            <h1 tabindex="0">{{ course.title }} Lessons:</h1>
        </div>
        <div class="lessons-container">
            <table class="lessons-table">
                <tbody>
                    <tr v-for="(lesson, index) in lessons" :key="lesson.id">
                        <td class="lesson-item">
                            <div class="lesson-info">
                                <h4 class="lesson-title">
                                    <a :href="'/courses/lessons/' + lesson.id">
                                        Lesson {{ index + 1 }}: {{ lesson.title }}
                                    </a>
                                </h4>
                            </div>
                        </td>
                    </tr>
                    <tr v-if="emptyLesson" tabindex="0">
                        <td colspan="2">
                            You have no lessons.
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div tabindex="0" class="assignments-header">
            <h1>Assignments:</h1>
        </div>
        <div class="assignments-container">
            <table class="assignments-table">
                <tbody>
                    <tr v-for="(assignment, index) in assignments" :key="assignment.id">
                        <td class="assignment-item">
                            <div class="assignment-info">
                                <h4 class="assignment-title">
                                    <a :href="'/courses/assignment/' + assignment.id">
                                        Assignment {{ index + 1 }}: {{ assignment.title }}
                                    </a>
                                </h4>
                            </div>
                        </td>
                    </tr>
                    <tr v-if="emptyAssignment" tabindex="0">
                        <td colspan="2">
                            You have no assignments.
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
  
  	export default {
      	data() {
          	return {
				course: {},
				courseId: null,
              	lessons: [],
				assignments: [],
				emptyLesson: false,
				emptyAssignment: false,
          	};
      	},
    created() {
        this.fetchCourse();
    },
    methods: {
			async fetchCourse() {
				this.courseId = this.$route.params.id;
				
				try {
					const response = await axios.get(`/get_course/${this.courseId}/`);
					this.course = response.data;
                    responsiveVoice.speak("You are in the"+ this.course.title+" course");
				} catch (error) {
					console.error('Error fetching course:', error);
				}
				this.fetchLessons();
				this.fetchAssignments();
			},
			
			async fetchLessons() {
				try {
					
					const response = await axios.get(`/get_course_lessons/${this.courseId}/`);
					this.lessons = response.data;
					this.emptyLesson = this.lessons.length === 0;
				} catch (error) {
					console.error('Error fetching lessons:', error);
				}
			},

			async fetchAssignments() {
				try {
					const response = await axios.get(`/get_lesson_assignments/${this.courseId}/`);
					this.assignments = response.data;
					this.emptyAssignment = this.assignments.length === 0;
				} catch (error) {
					console.error('Error fetching assignments:', error);
				}
			},
    },
  };
</script>



<style scoped>
.lesson-list {
    max-width: 800px;
    margin: 0 auto;
}

a {
    text-decoration: none;
}

.course-header,
.assignments-header {
    background-color: #d6d6d6;
    color: #000000;
    padding: 10px;
    margin-top: 20px;
}

.lessons-container,
.assignments-container {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 5px;
    margin-bottom: 2em;
}

.lesson-title,
.assignment-title {
    margin-bottom: 5px;
}

.btn {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    text-decoration: none;
    cursor: pointer;
}

.btn:hover {
    background-color: #0056b3;
}

.lessons-table,
.assignments-table {
    width: 100%;
    border-collapse: collapse;
}

.lesson-item,
.assignment-item {
    border: 1px solid #ddd;
    padding: 10px;
}

.lesson-item {
    background-color: #ffffff;
}

.assignment-item {
    background-color: #f8f9fa;
}

.lesson-item a,
.assignment-item a {
    color: #000000;
}

.lesson-item a:hover,
.assignment-item a:hover {
    color: #007bff;
}
</style>