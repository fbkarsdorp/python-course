$(document).ready(function(){

  $("#search input").on("keydown",function(e){
    if(e.keyCode == "13"){
      $("#results").html("");
      $("#results").addClass("loading");
      query = $(this).val();
      $.ajax({
        url:"/searchbox",
        data:{"q":query},
        method:"POST",
        success:function(data){
          $("#results").removeClass("loading");
          $("#results").html(data.html);
        },
        error:function(){
          $("#results").removeClass("loading");
          $("#results").html("oops, something went wrong...");
        }
      })
    }
  })
})
