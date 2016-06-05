/**
 * Created by Feelemon on 30.05.16.
 */
$(document).ready(function(){
          $.ajaxSetup({
            data: {csrfmiddlewaretoken: '{{ csrf_token }}' }
          });
          $( "button.add" ).click(function(){
            var current_button = $(this);
            $.ajax({
                url: "/add-to-cart/",
                type: "POST",
                data: {"item": $(this).attr('id')},
                success: function(data){
                  current_button.replaceWith( data );
                }
            });
           });
        });