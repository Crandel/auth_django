$(document).ready(function(e) {
   /* var deviceW = $(window).width();
    if(deviceW<480){
		$("#container").addClass("device-W");
    }*/
	$(".searchbox input").on("keyup", function(){
		$(".searchbox small#end-search").addClass("show");
	});

     $(".searchbox small#end-search a").on("click", function(){
        $(".searchbox input").val('');
        $(".searchbox small#end-search").removeClass("show");
      });
});

function footerPos(){
	var wh = $(window).height();	
	var hh = $("header").outerHeight();
	var fh = $("footer").outerHeight();
	var actualHeight = wh-(hh+fh);
	$(".contents").css("min-height", actualHeight);
}
