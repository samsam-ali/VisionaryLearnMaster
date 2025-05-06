<template>

    <div>
        <Navbar></Navbar>
        <Footer></Footer>
    </div>
    
</template>

<script>
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';

export default{
    name:'App',
    components: {
        Navbar,
        Footer
    },
    mounted() {
        // Event listener for focus change on the document
        document.addEventListener('focusin', this.handleFocusIn);

    },

    methods: {
        handleKeyDown(event) {
            if (event.key === 'Tab') {
                // event.preventDefault(); // Prevent default tab behavior
                this.handleTabPress();
            }
        },
        handleTabPress() {
            const focusedElement = document.activeElement;
            if (focusedElement) {
                const content = focusedElement.innerText || focusedElement.textContent;
                if (content) {
                    responsiveVoice.speak(content);
                }
            }
        },
        handleFocusIn(event) {
            const focusedElement = event.target;
            if (focusedElement) {
                let content = focusedElement.innerText || focusedElement.textContent;

                // Check if the element has aria-label attribute
                const ariaLabel = focusedElement.getAttribute('aria-label');
                if (ariaLabel) {
                    content = ariaLabel;
                }

                // Check if the element is an image with alt text
                if (focusedElement.tagName.toLowerCase() === 'img') {
                    const altText = focusedElement.getAttribute('alt');
                    if (altText) {
                        content = altText;
                    }
                }

                // Read the content using ResponsiveVoice
                if (content) {
                    responsiveVoice.speak(content);
                }
            }
        }
    }
    
}

</script>

<style >

</style>
