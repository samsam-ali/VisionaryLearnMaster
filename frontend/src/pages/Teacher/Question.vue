<template>
    <div class="question-form">
        <h2>Create a Question</h2>
        <form @submit.prevent="submitQuestion">
                <div class="form-group">
                    <label for="questionTitle">Question Title:</label>
                    <input type="text" id="questionTitle" v-model="questionTitle" class="form-control" required>
                </div>
                <div class="form-group" v-for="(choice, index) in choices" :key="index">
                    <label :for="'choice' + index">Choice {{ index + 1 }}:</label>
                    <input type="text" :id="'choice' + index" v-model="choice.title" class="form-control" required>
                    <input type="radio" :id="'correctChoice' + index" v-model="correctChoice" :value="index">
                    <label :for="'correctChoice' + index">Correct Choice</label>
                </div>
                <button type="button" @click="addChoice" class="btn btn-secondary">Add Choice</button>
                <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</template>

<script>
export default {
    data(){
        return {
            questionTitle: '',
            choices: [{ title: '', is_correct:false }],
            correctChoice: null,
        };
    },
    methods: {
        addChoice(){
            this.choices.push({ title:'', is_correct: false });
        },

        async submitQuestion(){
            try{
                const response = await axios.post('add_question', {
                    title: this.questionTitle,
                    choices: this.choices,
                }).then((response) => {
                    if(response.status == 201){
                        console.log('Created question successfully!')
                        console.log(response)
                    }
                })
            }
            catch (error) {
                console.error('Question was not created:', error);
            }
        }
    },
};
</script>

<Style>
</Style>