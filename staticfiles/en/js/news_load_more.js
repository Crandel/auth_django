function load_more(month, year, url){
    $.get(url, {month: month, year: year}, function(data){
        $(".accordion-wrapper").append(data.news);
        $("#load_more").hide();
    });
}