var input_switch = false;
var user_inputs = ["",""];
$(function(){
	$(".user-input").eq(Number(input_switch)).focus();
	//startTimer(pane_switch);
	setInterval(() => {
		
	}, 0);
});


/////////////////////////////////////////////////////
$(".user-input").keyup((e)=>{
	user_inputs[Number(input_switch)] = $(".user-input").eq(Number(input_switch)).val();
	//console.log($(".user-input").eq(Number(input_switch)).val());
	console.log(user_inputs);

	if(!input_switch){
		if(e.key == "Enter"){
			console.log("post: " + user_inputs[Number(input_switch)]);
			$(".user-input").eq(Number(input_switch)).val("");
			//user_inputs[Number(input_switch)] = "";
		}
	}else{
		if(e.ctrlKey == true && e.key == "Enter"){
			console.log("post: " + user_inputs[Number(input_switch)]);
			$(".user-input").eq(Number(input_switch)).val("");
			//user_inputs[Number(input_switch)] = "";
		}
	}
});
$(document).keydown(function(e){
	//console.log("key: " + e.key + "(len:"+(e.key).length+")"); 
	if(e.key == "Tab"){
		input_switch = !input_switch;
		$(".user-input").eq(Number(input_switch)).focus();
		return false;
	}
	if(e.key == "Escape"){
		disp_it();
	}
	/*
	if((e.key).length == 1){
		user_inputs[Number(pane_switch)] += e.key;
		//console.log("user_input["+Number(pane_switch)+"]: "+ user_inputs[Number(pane_switch)]);
		syncUserInput(Number(pane_switch));
	}
	if(e.key == "Enter"){
		user_inputs[Number(pane_switch)] = "";
		console.log("user_input["+Number(pane_switch)+"]: "+ user_inputs[Number(pane_switch)]);
		syncUserInput(Number(pane_switch));
	}*/

});
$(".user-input").eq(0).click((e)=>{
	input_switch = false;
});
$(".user-input").eq(1).click((e)=>{
	input_switch = true;
});

/*
function syncUserInput(n){
	if(n == 0){
		$(".p2").eq(1).html(user_inputs[n]);
	}else{
		$(".p3").eq(0).html(user_inputs[n]);
	}
}
*/
