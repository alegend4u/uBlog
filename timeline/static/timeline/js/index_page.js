function resizeGridItem(item){
   grid = document.getElementsByClassName("blog_grid")[0];
   rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
   rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-gap'));
   rowSpan = Math.ceil(
       (item.querySelector('.content').offsetHeight+rowGap)/(rowHeight+rowGap)
   );
   item.style.gridRowEnd = "span "+rowSpan;
}

function resizeAllGridItems(){
   allItems = document.getElementsByClassName("blog");
   for(x=0;x<allItems.length;x++){
      resizeGridItem(allItems[x]);
   }
}

window.onload = resizeAllGridItems();
window.addEventListener("resize", resizeAllGridItems);
