
$(document).ready(function () {
      $("select").formSelect();
      $(".sidenav").sidenav({
          edge: "right"});
      $(".materialboxed").materialbox();
      $("textarea#intro").characterCounter();
});

$(document).ready(function () {
var selectorvar = $("#selectordiv").html();
var scroll_pos = 0;

if (selectorvar !== "true"){
        $(".navbar-icons").css("color","#FF9F00");
        $(".sidenav-trigger").css("color", "#FF9F00");
        $(".nav-wrapper").removeClass("transparent").addClass("white");
}

if (selectorvar === "true"){

    $(document).scroll(function () {
        scroll_pos = $(this).scrollTop();
        var height = $(window).height();

        if (height >= 800) {

            if (scroll_pos > 700) {
                $(".nav-wrapper").removeClass("visible").addClass("hidden");
                $(".navbar-icons").removeClass("visible").addClass("hidden");
                $(".sidenav-trigger").removeClass("visible").addClass("hidden");
            }

            if (scroll_pos > 900) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".sidenav-trigger").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("transparent").addClass("white");
                $(".navbar-icons").css("color", "#FF9F00");
                $(".sidenav-trigger").css("color", "#FF9F00");
            }

            if (scroll_pos < 300) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".sidenav-trigger").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("white").addClass("transparent");
                $(".navbar-icons").css("color", "white");
                $(".sidenav-trigger").css("color", "white");
            }
        }

        else if (height >= 500) {

            if (scroll_pos > 250) {
                $(".nav-wrapper").removeClass("visible").addClass("hidden");
                $(".navbar-icons").removeClass("visible").addClass("hidden");
                $(".sidenav-trigger").removeClass("visible").addClass("hidden");
        }

            if (scroll_pos > 550) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".sidenav-trigger").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("transparent").addClass("white");
                $(".navbar-icons").css("color", "#FF9F00");
                $(".sidenav-trigger").css("color", "#FF9F00");
            }

            if (scroll_pos < 200) {
                $(".nav-wrapper").removeClass("hidden").addClass("visible");
                $(".navbar-icons").removeClass("hidden").addClass("visible");
                $(".sidenav-trigger").removeClass("hidden").addClass("visible");
                $(".nav-wrapper").removeClass("white").addClass("transparent");
                $(".navbar-icons").css("color", "white");
                $(".sidenav-trigger").css("color", "white");
            }
        }

    });
  }
});

// https://stackoverflow.com/questions/36290110/open-card-reveal-content-by-hover-the-activator-in-materializecss

$(document).ready(function() {
    $(".card").hover(
        function() {
            $(this).find("> .card-image > img.activator").click();
        }, function() {
            $(this).find("> .card-reveal > .card-title").click();
        }
    );
});