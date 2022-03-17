$(() => {
	if(localStorage.getItem("name") == null){
		p0_respond("`助けて` をタイプしてコマンドを表示");
	}else{
		p0_respond(
			"ようこそ、" + localStorage.getItem("name") +
			"<br>`助けて` をタイプしてコマンドを表示"
		);
	}
});

function process_0_new(input){
	split_input = input.replaceAll("　", " ").split(" ");
	console.log("command array:" + split_input);
	var ajax_res = myajax({
		arg1: split_input[0],
		arg2: split_input[1],
		arg3: localStorage.getItem("name"),
		arg4: localStorage.getItem("instance")
	});
	if(ajax_res.includes("お名前設定")){
		var name = ajax_res.split(":")[1];
		localStorage.setItem("name", name);
	}else if(ajax_res.includes("[成功]")){
		var instance = ajax_res.split(":")[1];
		localStorage.setItem("instance", instance);
		shita_start();
	}
	p0_respond(ajax_res);
}


function myajax(paras){
	var res = $.ajax(
		{
			url: "./cuicui_command",
			type: "GET",
			data: paras,
			async: false
		}
	).responseText
	return res;
}

function speedtest(bool){
	var mae = new Date().getTime();
	for (var i=0; i<100; i++){
		if (bool){
			myajax({
				arg1: "sync",
				arg3: "Ohashi",
				arg4: "a"
			});
		}else{
			myajax({arg1: "test"});
		}
	}
	var ato = new Date().getTime();
	console.log((ato - mae)/1000);
	console.log(100/(ato - mae)*1000);
}

function p0_respond(arg_text){
	var response_div = $('<div>'+arg_text+'</div>');
	var input_div = $('<div>');
	var stored_name = localStorage.getItem("name");
	if(stored_name == null){stored_name = "Unknown";}
	var input_div_name = $('<span>', {class:'green-name', text: stored_name});
	var input_div_input = $('<input>', {class: 'user-input input-ue'})

	input_div_input.click((e)=>{
		input_switch = false;
	});
	input_div_input.keydown((e) => {
		if(e.key == "Enter"){
			var input = input_div_input.val();
			process_0_new(input);
		}
	});

	input_div.append(input_div_name);
	input_div.append(": ");
	input_div.append(input_div_input);

	$("#p2").append(response_div);
	$("#p2").append(input_div);
	input_div_input.focus();
}
