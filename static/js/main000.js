// Materialize Code
    document.addEventListener("DOMContentLoaded", function() {
    var elems = document.querySelectorAll("select");
    var instances = M.FormSelect.init(elems, {});
    // I'm probably not going to leave this as is, this is a mess
  });

/* hide when expanded*/
    document.querySelector(".search-field")
        .addEventListener("focus", function() {
    var hidden = document.querySelectorAll(".search-hide");
    for(let i = 0; i < hidden.length; i += 1) {
        hidden[i].style.display = "none";
  }
});

/* show when expanded*/
    document.querySelector(".search-field")
        .addEventListener("focusout", function() {
    var hidden = document.querySelectorAll(".search-hide");
    for(let i = 0; i < hidden.length; i += 1) {
        hidden[i].style.display = "block";
    }
  });

    function changeColor_liked() {
        document.getElementById("up-arrow-liked-inSession")
            .style.color = "red";
    }

    function changeColor_disliked() {
        document.getElementById("down-arrow-disliked-inSession")
            .style.color = "blue";
    }


  function sweetAlert_notLogged () {
      swal({title: "Little problem",
            text: "Have to log-in first",
            icon: "warning",
            timer: 2000
            });
        }

    function sweetAlert_notHere () {
      swal({title: "",
            text: "You can only vote in the full story page",
            icon: "warning",
            timer: 2000
            });
        }


    function sweetAlert_delete() {
      swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover this imaginary file!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
        })
        
        .then((confirm) => {
        if (confirm) {
            swal("Poof! Your imaginary file has been deleted!", {
            icon: "success",
            });
        } else {
            swal("Your imaginary file is safe!");
        }
        });
        }