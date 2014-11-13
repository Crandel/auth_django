$(document).ready(function(e) {
    $("input.upload").click(function(){
       $("input[type=file]").trigger("click");
    });
    $(".browse-btn input.input").click(function(){
       $("input[type=file]").trigger("click");
    });
    $('body').on('change', '#id_cv', function(){
        $(".browse-btn input.input").val(this.value)
    })
    $('body').on('submit', '#cv-form', function (e) {
        var form = $(this);
        form.ajaxSubmit({
            success: function (resp) {
                $(".browse-btn input.input").val("")
                alert('Send success')
                return false;

            },
            error: function (resp) {
                alert('error');
            }
        });
        e.preventDefault();
        return false;
    });

    $('body').on('submit', '#contact-form', function (e) {
        var form = $(this);
        form.ajaxSubmit({
            success: function (resp) {
                $(".browse-btn input.input").val("")
                alert('Send success')
                return false;

            },
            error: function (resp) {
                alert('error');
            }
        });
        e.preventDefault();
        return false;
    });


  });
  function load_more(page, url){
    $.get(url, {page: page}, function(data){
      $("#vacancy").append(data.items);
      $("#load_more").html(data.more)
    });
  }
