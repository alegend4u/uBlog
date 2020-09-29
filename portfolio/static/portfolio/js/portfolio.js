const scrollButtons = document.querySelectorAll('.scroll_btn')
const scrollUp = scrollButtons[0]
const scrollDown = scrollButtons[1]
const sections = Array.from(document.querySelectorAll('.section'))
const sectionPositions = sections.map(section => section.offsetTop)
const modalCloseButtons = document.querySelectorAll('.modal .close')

music = document.querySelector('#project_music')
uit = document.querySelector('#project_uit')

modalCloseButtons.forEach((closeButton) => {
    closeButton.onclick = function () {
        modal = this.parentElement.parentElement
        // modal.style.display = 'none'
        modal.classList.remove('modal_open')
    }
})

window.onclick = function (event) {
    if (event.target.classList.contains('modal')){
        // event.target.style.display = 'none'
        event.target.classList.remove('modal_open')
    }
}

music.addEventListener('click', function () {
    music_modal = document.querySelector("#modal-music")
    // music_modal.style.display = 'block'
    music_modal.classList.add('modal_open')
})

uit.addEventListener('click', function () {
    uit_modal = document.querySelector('#modal-uit')
    // uit_modal.style.display = 'block'
    uit_modal.classList.add('modal_open')
})


scrollUp.addEventListener('click', scrollToPreviousSection)
scrollDown.addEventListener('click', scrollToNextSection)

function scrollToPreviousSection() {
    const currentPos = window.pageYOffset;
    let nearestSectionIdx = 0;
    let minDistance = Infinity
    for (let i = 0; i < sectionPositions.length; i += 1) {
        let distance = currentPos - sectionPositions[i]
        if (distance > 0 && distance < minDistance) {
            minDistance = distance
            nearestSectionIdx = i
        }
    }
    sections[nearestSectionIdx].scrollIntoView()
}

function scrollToNextSection() {
    const currentPos = window.pageYOffset;
    let nearestSectionIdx = null;
    let minDistance = Infinity;
    for (let i = 0; i < sectionPositions.length; i += 1) {
        const distance = sectionPositions[i] - currentPos;
        if (distance > 0 && distance < minDistance) {
            minDistance = distance
            nearestSectionIdx = i
        }
    }
    if (nearestSectionIdx == null) {
        nearestSectionIdx = sections.length - 1
    }
    sections[nearestSectionIdx].scrollIntoView()
}
