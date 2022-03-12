var stored_name = localStorage.getItem("name_CUICUI");
var user_name = "Unknown";

function process_0(input){
	console.log("process_0:");
	console.log(input);

	append_input_div();
}
 
function append_input_div(){
	var input_div = $('<div>');
	var input_div_name = $('<span>', {class:'green-name', text:user_name });
	var input_div_input = $('<input>', {class: 'user-input'})
	input_div.append(input_div_name);
	input_div.append(": ");
	input_div.append(input_div_input);

	$("#p2").append(input_div);
	input_div_input.focus();
}