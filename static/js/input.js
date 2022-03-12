var input_switch = false;
var elms_input = [
	$(".user-input").eq(0),
	$(".user-input").eq(1)
];
$(() => {
	elms_input[Number(input_switch)].focus();
});
$(document).keydown(function(e){
	//console.log("key: " + e.key + "(len:"+(e.key).length+")"); 
	if(e.key == "Tab"){
		input_switch = !input_switch;
		elms_input[Number(input_switch)].focus();
		return false;
	}
	if(e.key == "Escape"){
		console.log("sync!")
	}
});
elms_input[0].click((e)=>{
	input_switch = false;
});
elms_input[1].click((e)=>{
	input_switch = true;
});

////////////////////////////////////////////
elms_input[0].keydown((e) => {
	if(e.key == "Enter"){
		var input = elms_input[0].val();
		elms_input[0].val("");
		//var input = $(this).eq(0).val();
		process_0(input);
	}
});
elms_input[1].keydown((e) => {
	if(e.ctrlKey == true && e.key == "Enter"){
		var input = elms_input[1].val();
		elms_input[1].val("");
		//var input = $(this).eq(0).val();
		process_1(input);
	}
});
elms_input[1].keyup((e) => {
	var input = elms_input[1].val();
	console.log("途中: "+ input);
});