$(document).ready(function(){

        $("#search input").on("keydown",function(e){
                if(e.keyCode == "13"){
                        $("#results").html("");
                        $("#results").addClass("loading");
                        query = $(this).val();
                        console.log(query);
                        $.ajax({
                                url:"/api",
                                data:{"q":query},
                                method:"POST",
                                success:function(data){
                                        console.log(data);
                                        $("#results").removeClass("loading");
                                        $("#counts").html(data.categories);
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