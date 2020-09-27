const scrollButtons = document.querySelectorAll('.scroll_btn')
const scrollUp = scrollButtons[0]
const scrollDown = scrollButtons[1]
const sections = Array.from(document.querySelectorAll('.section'))
const sectionPositions = sections.map(section => section.offsetTop)

scrollUp.addEventListener('click', scrollToPreviousSection)
scrollDown.addEventListener('click', scrollToNextSection)

function scrollToPreviousSection() {
    const currentPos = window.pageYOffset;
    let nearestSectionIdx = 0;
    let minDistance = Infinity
    for (let i = 0; i < sectionPositions.length; i += 1) {
        let distance = currentPos - sectionPositions[i]
        console.log('prev' + distance)
        if (distance > 0 && distance < minDistance) {
            minDistance = distance
            nearestSectionIdx = i
            // console.log('got prev nearest idx' + nearestSectionIdx)
        }
    }
    console.log('-----')
    sections[nearestSectionIdx].scrollIntoView()
}

function scrollToNextSection() {
    const currentPos = window.pageYOffset;
    let nearestSectionIdx = null;
    let minDistance = Infinity;
    for (let i = 0; i < sectionPositions.length; i += 1) {
        const distance = sectionPositions[i] - currentPos;
        console.log('next' + distance)
        if (distance > 0 && distance < minDistance) {
            minDistance = distance
            nearestSectionIdx = i
            // console.log('got next nearest idx' + nearestSectionIdx)
        }
    }
    if (nearestSectionIdx == null) {
        nearestSectionIdx = sections.length - 1
    }
    console.log('-----')
    sections[nearestSectionIdx].scrollIntoView()
}
