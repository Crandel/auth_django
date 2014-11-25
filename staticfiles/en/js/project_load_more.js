function load_more(page, url){
    $.get(url, {page: page}, function(data){
        $(".item_list").append(data.items);
        $("#load_more").html(data.more)
    });
}