$(document).ready(function(){

    $("form").submit(function(e) {
        e.preventDefault();
        
        var number; 
        number= $("input").val();

        $.get(
            '/is_circular/', 
            { number: number }, 
            function(data){
                    if (data["result"] == "success"){
                        swal(data["number"]+" tiene primos circulares", "los cuales son: "+data["data"], "success")
                    }
                    else{
                        swal("¡Mala suerte!", data["message"], "error")        
                    }
            }
        );
        return false;
    });
    /*
    swal({
      title: "Error!",
        text: "Here's my error message!",
          type: "error",
            confirmButtonText: "Cool"
            });
        var number;
        $.get( 
            "is_circular",
            function(data) {
                if (data["HTTPRESPONSE"] == 1)
                      {
                                alert("success")
                                      }
            }
        );
    
    
    
    
    
    });
    */


});
