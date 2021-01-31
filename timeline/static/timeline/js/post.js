let post_title = document.querySelector(".post_title");
let max_title_size = unpx(window.getComputedStyle(post_title, null)
    .getPropertyValue('font-size'));
let min_title_size = Math.floor(0.6 * max_title_size);
let scroll_span = 300;

window.onscroll = function () {
    animate_header();
};

function animate_header() {
    let scroll = document.documentElement.scrollTop;
    var scale = 0;
    if (scroll >= scroll_span) {
        scale = 1;
    } else {
        scale = scroll / scroll_span;
    }
    let calculated_font_size = Math.round(max_title_size - (max_title_size - min_title_size) * scale);
    post_title.style.fontSize = calculated_font_size + "px";
}

function unpx(px_value) {
    return parseInt(px_value.slice(0, -2))
}