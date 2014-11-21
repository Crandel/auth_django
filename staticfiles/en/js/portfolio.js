$(document).ready(function(e) {
    $(".header-nav .slider").flexslider({animation: "slide", controlNav: false, slideshow:false, animationSpeed:1500,});
    $("#main-banner").flexslider({
        controlNav:true,
        directionNav:false,
        slideshow: true
    });
});
function load_more_cat(page, url){
    $.get(url, {page: page}, function(data){
        $(".item_list").append(data.items);
        $("#load_more_cat").html(data.more)
    });
}