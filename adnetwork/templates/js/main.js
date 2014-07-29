var activen="home";
var nextn="";


$(document).ready(function()
{
	
	var x=(($(window).width())-1024)/2;
	//alert(x);
	$('body').css("left",x+"px");
	setTimeout('rotate()',3000);





});
$(document).keydown(function(e) {
    
    if (e.keyCode == 27) {
        closePopup();
    }
});
function select(id)
	{
		nextn=id;
		$("#nav-"+nextn).click(function(){
			$("#nav-"+activen).removeClass("active");
			$("#nav-"+nextn).addClass("active");
			activen=nextn;
			
		});
}
function rotate()
{
	$("#home1").fadeOut(3000);
	$("#home2").fadeIn(3000,"linear",function(){setTimeout('rotatei()',3000);});
}
function rotatei()
{

	$("#home2").fadeOut(3000);
	$("#home1").fadeIn(3000,"linear",function(){setTimeout('rotate()',3000);});
	
}
function showPopup()
{
	$("#popupback").css("opacity",0.1);
	$("#popup").show(50);
}
function closePopup()
{
	$("#popup").hide(50);
	$("#popupback").css("opacity",1);
}
function show_login_err()
{
	document.getElementById("login-err").innerHTML="Invalid Username or Password";
}


		
	