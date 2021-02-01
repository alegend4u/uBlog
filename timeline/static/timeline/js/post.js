let page_header = document.querySelector(".page_header");
let post_title = document.querySelector(".post_title");
let max_title_size = unpx(window.getComputedStyle(post_title, null)
    .getPropertyValue("font-size"));
let min_title_size = Math.floor(0.6 * max_title_size);

let datebox = document.querySelector(".datebox");
let max_datebox_width = unpx(window.getComputedStyle(datebox, null)
    .getPropertyValue("width"));
let min_datebox_width = Math.floor(0.75 * max_datebox_width);

let scroll_span = 300;

window.onscroll = function () {
    animate_header();
};

function animate_header() {
    let scroll = document.documentElement.scrollTop;
    var scale_down = 0;
    if (scroll >= scroll_span) {
        scale_down = 1;
    } else {
        scale_down = scroll / scroll_span;
        if (scroll > 0){
            page_header.classList.add("scrolled");
        } else {
            page_header.classList.remove("scrolled");
        }
    }

    let calculated_font_size = Math.round(max_title_size - (max_title_size - min_title_size) * scale_down);
    post_title.style.fontSize = calculated_font_size + "px";

    let calculated_datebox_width = Math.round(max_datebox_width - (max_datebox_width - min_datebox_width) * scale_down);
    datebox.style.width = calculated_datebox_width + "px";
}

function unpx(px_value) {
    return parseInt(px_value.slice(0, -2))
}
