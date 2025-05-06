<template>
    <div>
        <form @submit.prevent="submitAnswer">
            <ul class="list-group">
                <li v-for="(choice, index) in choices" :key="index" class="list-group-item">
                    <label class="text-dark" :tabindex="0" @keypress.enter="selectChoice(choice)">
                        <input class="form-check-input" type="radio" v-model="selectedChoice" :value="choice" name="choices" :tabindex="-1">
                        <span class="form-check-label">{{ choice.title }}</span>
                    </label>
                </li>
            </ul>
            <button class="btn btn-secondary mt-3" type="submit">Submit</button>
        </form>
        <div v-if="submitted" class="mt-3" tabindex="0">
            You selected: {{ selectedChoice.title }}
        </div>
        <div v-if="submitted" class="mt-3" tabindex="0">
            Your answer is: <strong :class="[{'text-success': selectedChoice.is_correct, 'text-danger': !selectedChoice.is_correct}]">{{ selectedChoice.is_correct ? 'Correct' : 'Incorrect' }}</strong>
        </div>
    </div>
</template>



  
<script>
export default {
    name: 'Choices',
    props: {
        // receive choices as a prop from Assignment
        choices: Array,
    },
    data(){
        return{
            selectedChoice: null,
            submitted: false,
        };
    },
    methods: {
        async submitAnswer(){
            if(this.selectedChoice){
                this.$emit('choice-selected', this.selectedChoice);
                this.submitted = true;
                var corr = "incorrect";
                if(this.selectedChoice.is_correct){
                    corr = "correct";
                }
                responsiveVoice.speak("You selected: " + this.selectedChoice.title + ". Your answer is " + corr);
            }
        },
        selectChoice(choice) {
            this.selectedChoice = choice;
            
        }
    },
}
</script>
