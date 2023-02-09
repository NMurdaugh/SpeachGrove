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
            axios.post('/api/speech/', this.postData(), {
                headers: { 'X-CSRFToken': this.csrfToken }
            }).then(res => this.ttsData = res.data)
        },
        postData() {
            return {
                'speakerName': this.speakerName,
                'userRequestText': this.userRequestText,
         }
         },
    },
    mounted() {
        this.csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value
    },
})