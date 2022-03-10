//localStorage.setItem('myCat', 'Tom');
//var cat = localStorage.getItem("myCat");
//localStorage.removeItem("myCat");
var user_name = "Unknown";

$(() => {
	var stored_name = localStorage.getItem("name_CUICUI");
	if(stored_name == null){
		alert("kara");
		disp_it({
			name:user_name,
			switch: input_switch
		});
	}
});