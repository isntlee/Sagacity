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
            timer: 2500
            });
        }

    function sweetAlert_textError () {
      swal({title: "",
            text: "Just add some words, and capitalize the first one.",
            icon: "warning",
            timer: 2500
            });
        }

    function sweetAlert_httpError () {
      swal({title: "",
            text: "Add a proper url .e.g https://...",
            icon: "warning",
            timer: 2500
            });
        }

    function sweetAlert_delete() {
      swal({
            title: "Sure about this?",
            text: "This can't be recovered afterwards",
            icon: "warning",
            buttons: true,
            dangerMode: true,
            timer: 5000,
            })
    .then((willDelete) => {
        if (willDelete) {
            document.getElementById("deleteForm").submit();
            swal("And just like that, it was gone", {
            icon: "success",
            });
        } else {
            swal("Your tale is preserved still");
        }
        });
            }