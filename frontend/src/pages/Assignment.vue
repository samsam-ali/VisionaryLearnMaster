<template>
    <div>
        <div class="container pt-3">
            <h1 tabindex="0">{{ assignment.title }}</h1>
            <div v-for="question in assignmentQuestions" :key="question.id" class="question-card">
                <h4 tabindex="0">Question {{question.id}}: {{ question.title }}</h4>
                <choices :choices="question.choices"></choices>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Choices from './Choices.vue';

export default {
    name: 'Assignment',
    components: {
        'choices': Choices,
    },
    data(){
        return{
            assignment: {},
            assignmentQuestions: [],
            assignmentId: this.$route.params.id,
            selectedChoice: null,
            submitted: false,
        };
    },
    created(){
        this.fetchAssignment();
        
    },
    methods: {
        async fetchAssignment() {
            try {
                const response = await axios.get(`/get_assignment/${this.assignmentId}/`);
                this.assignment = response.data;
                responsiveVoice.speak("You are in "+ this.assignment.title);
            } catch (error) {
                console.error('Error fetching assignment:', error);
            }
            this.fetchAssignmentQuestions();
        },
        async fetchAssignmentQuestions() {
            try{
                axios.get(`/get_assignment_questions/${this.assignmentId}/`)
                .then(response => {
                    this.assignmentQuestions = response.data;
                    console.log('Assignment questions:', this.assignmentQuestions);
                })
                .catch(error => {
                    console.error(error);
                });
            }
            catch (error) {
                console.error('Error fetching assignment questions:', error);
            }
            
        },
        async fetchQuestionChoices(questionId){
            try{
                axios.get(`/get_question_choices/${questionId}/`)
                .then(response => {
                    this.choices = response.data;
                    console.log('Question choices:', this.choices);
                })
                .catch(error => {
                    console.error(error);
                });
            }
            catch (error) {
                console.error('Error fetching question choices:', error);
            }
        }
    }
}


</script>