    
    // Materialize Code

    document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
    // I'm probably not going to leave this as is, this is a mess
  });


  function sweetAlert_notLogged () {
      swal({title: "Little problem",
            text: "Have to log-in first",
            icon: "warning",
            timer: 1500,
            imageUrl: 'https://lionalert.org/wp-content/uploads/2020/01/Lion-Cubs-1080x675.jpg'

            });
        }

    function changeColor_liked() { 
        document.getElementById("up-arrow-liked-inSession").style.color = "red";
    }

    function changeColor_disliked() { 
        document.getElementById("down-arrow-disliked-inSession").style.color = "blue"; 
    }


    function sweetAlert_notHere () {
      swal({title: "",
            text: "You can only vote in the full story page",
            icon: "warning",
            timer: 1500,
            imageUrl: 'https://lionalert.org/wp-content/uploads/2020/01/Lion-Cubs-1080x675.jpg'
            });
        }