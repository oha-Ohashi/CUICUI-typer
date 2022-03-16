var input_switch = false;
var elms_input = [
	$(".input-ue"),
	$(".input-shita")
];
$(() => {
	elms_input[Number(input_switch)].last().focus();
});
////////////////////////////////////////
$(document).keydown(function(e){
	//console.log("key: " + e.key + "(len:"+(e.key).length+")"); 
	if(e.key == "Tab"){
		input_switch = !input_switch;
		elms_input[Number(input_switch)].last().focus();
		return false;
	}
	if(e.key == "Escape"){
		console.log("sync!")
	}
});
$(document).keyup(function(e){
	elms_input = [
		$(".input-ue"),
		$(".input-shita")
	];
});

$("#p2").click((e) => {
	input_switch = false;
	$(".input-ue").last().focus();
});
$("#p3").click((e) => {
	input_switch = true;
	$(".input-shita").last().focus();
});

elms_input[0].last().click((e)=>{
	input_switch = false;
});
elms_input[1].last().click((e)=>{
	input_switch = true;
});


////////////////////////////////////////////
elms_input[0].keydown((e) => {
	if(e.key == "Enter"){
		var input = elms_input[0].last().val();
		process_0_new(input);
	}
});
elms_input[1].keydown((e) => {
	if(e.ctrlKey == true && e.key == "Enter"){
		var input = elms_input[1].last().val();
		elms_input[1].last().val("");
		process_1(input);
	}
});
elms_input[1].keyup((e) => {
	var input = elms_input[1].last().val();
	console.log("途中: "+ input);
});