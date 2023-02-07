new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        ttsData: null
    },
    methods: {
        speechWriter() {
            axios.post('/api/speech').then(res => this.ttsData = res.data)
        }
    }
})