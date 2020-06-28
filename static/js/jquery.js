
$(document).ready(function () {
      $('select').formSelect();
      $('.materialboxed').materialbox();
      });
 
      
$(document).ready(function () {
var selectorvar = $('#selectordiv').html();
if (selectorvar != 'true'){
        $(".navbar-icons").css("color","#FF9F00");
        $(".nav-wrapper").removeClass("transparent").addClass("white");
    }
});

// Lets adapt this over now
$(document).ready(function () {
    var scroll_pos = 0;

    $(document).scroll(function () {
        scroll_pos = $(this).scrollTop();
        var width = $(window).width();



        if (width >= 310) {
            
            if (scroll_pos > 1000) {
                $(".nav-wrapper").removeClass("visible").addClass("hidden");
                $(".navbar-icons").removeClass("visible").addClass("hidden");
            }
            
            if (scroll_pos > 1200) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("transparent").addClass("white");
                $(".navbar-icons").css('color', '#FF9F00');
            }

            if (scroll_pos < 250) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("white").addClass("transparent");
                $(".navbar-icons").css('color', 'white');
            }
        }
    
    });
});