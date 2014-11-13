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
                if (resp.success) {
                    $(".browse-btn input.input").val("");
                    alert('Thank you for submitting your resume');
                } else {
                    alert('Please attach file');
                }
                return false;

            },
            error: function (resp) {
                alert('error');
            }
        });
        e.preventDefault();
        return false;
    });
    $('body').on('keyup', '#id_nationality_name', function(e){
        var val = $(this).val();
        var url = $(this).data('url');
        $.get(url, {str: val}, function(data){
            $("#drop-box").children().removeAttr("style");
            var list = "";
            if (data.length) {
                var i = 0;
                var len = data.length;
                for (; i<len; i++){
                    list += "<li data-id='"+data[i]['id']+"' class='nat_list'>"+data[i]['name']+"</li>";
                }
                if (data.length < 4) {
                    $("#drop-box").children().attr('style', 'min-height: ' + 40 * data.length + 'px');
                }

                $("#select-nationality").html(list);
            }
            $("#drop-box").show().addClass("open");
        })
    })
    $('body').on('click', "#select-nationality .nat_list", function(){
        var id = $(this).data('id');
        $('#id_nationality_name').val($(this).html())
        $('#id_nationality').val(id);
        $("#drop-box").hide().removeClass("open");
    })
    // $('body').on('submit', '#contact-form', function (e) {
    //     var form = $(this);
    //     form.ajaxSubmit({
    //         success: function (resp) {
    //             if (resp.success){
    //                 $(".browse-btn input.input").val("")
    //                 alert("Thank you for submitting your resume");
    //                 $(".required").each(function(el){
    //                     this.value = "";
    //                 });
    //                 Recaptcha.reload();
    //             }else{
    //                 var errors = resp.messages;
    //                 var i=0;
    //                 var len = errors.length;
    //                 var code = ""
    //                 for(;i<len;i++){
    //                     code = errors[i][0];
    //                     if code ==="nationality"{
    //                         var el =$(".required[name="+ code +"]").next('.error');

    //                     }
    //                     el.show();
    //                     el.html(errors[i][1])
    //                 }
    //             }

    //         },
    //         error: function (resp) {
    //             alert('error');
    //         }
    //     });
    //     e.preventDefault();
    //     return false;
    // });


  });
  function load_more(page, url){
    $.get(url, {page: page}, function(data){
      $("#vacancy").append(data.items);
      $("#load_more").html(data.more)
    });
  }
