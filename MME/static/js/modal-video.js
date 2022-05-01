document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#btnCloseModal').addEventListener('click', () => {
        document.querySelector('#videoModal').classList.add('hide')
    })

    let player = videojs('videoPlayer');

    player.on('ended', function () {
        document.querySelector('#videoModal').classList.add('hide')
    });
})