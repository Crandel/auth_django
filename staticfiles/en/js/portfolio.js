$(document).ready(function(e) {
    $(".header-nav .slider").flexslider({animation: "slide", controlNav: false, slideshow:false, animationSpeed:1500,});
    $("#main-banner").flexslider({
        controlNav:true,
        directionNav:false,
        slideshow: true
    });
});
