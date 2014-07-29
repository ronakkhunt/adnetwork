var activen="home";
var nextn="";

$(document).ready(function()
{
	



});
function select(id)
	{
		nextn=id;
		$("#nav-"+nextn).click(function(){
			$("#nav-"+activen).removeClass("active");
			$("#nav-"+nextn).addClass("active");
	//		$("#"+activen).hide();
		//	$("#"+nextn).show();
			activen=nextn;
			
		});
}



		
	