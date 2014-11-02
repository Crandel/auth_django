$(document).ready(function(e){
	langOption();
	
	var dh = $(document).height();
	var hh = $("#header").outerHeight();
	var wh = $(window).height();
	var fh = $("#footer").outerHeight();
	var actualHeight;
	
	if($("body").find("section").hasClass("inner-banner")==false){
		actualHeight = wh-(hh+fh);
	}else{
		var bannerHeight = $(".inner-banner").outerHeight();	
		actualHeight = wh-(hh+fh+bannerHeight+30);
	}
	$("#contents").css("min-height", actualHeight);
});
function langOption(){
	$(".header-search-area .language").click(function(e){
		$("ul.lang-list").slideToggle();
	});
	$("ul.lang-list li").click(function(e){
		var txt = $(this).text();
		$(".header-search-area .language").text(txt);
		$("ul.lang-list").slideToggle();
	});
	$("#navigation ul li .dd-menu ul.title li").hover(function(e){
		var curr = $(this).attr("data-ref");
		$("#navigation ul li .dd-menu").find(".submenu").css("display", "none");
		$("#navigation ul li .dd-menu").find(curr).css("display", "block");
	});
}


