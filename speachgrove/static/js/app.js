new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        speakerName: null,
        userRequestText: null,
        finalRequestText: null,
        ttsData: null
    },
    methods: {
        speechWriter() {
            axios.post('/api/speech').then(res => this.ttsData = res.data)
        }
    },
    mounted() {
        this.csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    }
})