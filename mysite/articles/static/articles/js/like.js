const likeButton = document.querySelectorAll('.like-button')
likeButton.forEach(button => {
    button.addEventListener('click', function(event) {
        const articleId = event.target.dataset.id
        const likeCount = document.querySelector(`#like-count-${articleId}`)
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        axios.post(`/articles/${articleId}/like/`)
        .then(response => {
            likeCount.innerText = `좋아요 수 : ${response.data.count}`
            if (response.data.liked) {
                event.target.className = 'fas fa-heart fa-lg like-button'
                event.target.style.color = 'crimson'
            } else {
                event.target.className = 'far fa-heart fa-lg like-button'
                event.target.style.color = 'black'
            }
        })
    })
})