<template>
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div>
                <h3>Add Assignment</h3>
                <hr/>
            </div>
            <form @submit.prevent="addAssignment" class="mt-4">
                <div class="mb-3">
                    <label for="lesson" class="form-label">Lesson</label>
                    <select v-model="selectedLesson" id="lesson" class="form-select">
                        <option value="">Select Lesson</option>
                        <option v-for="lesson in lessons" :key="lesson.id" :value="lesson.id">{{ lesson.title }}</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="assignmentTitle" class="form-label">Assignment Title</label>
                    <input type="text" v-model="assignmentTitle" class="form-control" required>
                </div>
                <div v-for="(question, index) in questions" :key="index">
                    <hr>
                    <h5>Question {{ index + 1 }}</h5>
                    <div class="mb-3">
                        <label class="form-label">Question Title</label>
                        <input type="text" v-model="question.title" class="form-control" required>
                    </div>
                    <div class="mb-3">
                        <h5><label class="form-label">Choices</label></h5>
                        <div v-for="(choice, choiceIndex) in question.choices" :key="choiceIndex">
                            Choice {{ choiceIndex+1 }}
                            <input type="text" v-model="choice.title" class="form-control" required>
                            <label>
                                <input type="checkbox" v-model="choice.is_correct"> Correct
                            </label>
                        </div>
                        <button @click.prevent="addChoice(index)" class="btn btn-secondary mt-3">Add Choice</button>
                    </div>
                </div>
                <button @click.prevent="addQuestion" class="btn btn-secondary mb-3">Add Question</button>
                <button type="submit" class="btn btn-primary mb-3">Submit</button>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            lessons: [],
            selectedLesson: '',
            assignmentTitle: '',
            questions: [{ 
                title: '', 
                choices: [{ title: '', is_correct: false }] 
            }],
        };
    },
    created(){
        this.get_lessons();
    },
    methods: {
        get_lessons() {
            axios.get('get_lessons')
                .then(response => {
                    this.lessons = response.data;
                })
                .catch(error => {
                    console.error('Error fetching lessons:', error);
                });
        },
        addQuestion() {
            this.questions.push({ title: '', choices: [{ title: '', is_correct: false }] });
        },
        addChoice(questionIndex) {
            this.questions[questionIndex].choices.push({ title: '', is_correct: false });
        },
        async addAssignment() {
            try {
                const assignmentResponse = await axios.post('add_assignment', {
                    lesson: this.selectedLesson,
                    title: this.assignmentTitle,
                });
                const assignmentId = assignmentResponse.data.id;

                for (const question of this.questions) {
                    const questionResponse = await axios.post('add_question', {
                        assignment: assignmentId,
                        title: question.title,
                    });
                    const questionId = questionResponse.data.id;

                    for (const choice of question.choices) {
                        await axios.post('add_choice', {
                            question: questionId,
                            title: choice.title,
                            is_correct: choice.is_correct,
                        });
                    }
                }

                console.log("Assignment and questions added successfully!");
                alert("Added assignment successfully!")
            } catch (error) {
                console.error('Error adding assignment and questions:', error);
            }
        },
    },
};
</script>
