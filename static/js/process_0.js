$(() => {
	if(localStorage.getItem("name_CUICUI") == null){
		p0_respond("\"助けて\" をタイプしてコマンドを表示");
	}else{
		p0_respond("ようこそ、" + localStorage.getItem("name_CUICUI"));
	}
});
const help_text = [
	[
		"名前 `名前`: ユーザーネームを`名前`に設定",
		"一覧: 現在開いている対戦インスタンスを表示",
		"作る `名前`: 対戦インスタンス`名前`を作成",
		"入る `名前`: 対戦インスタンス`名前`に入室する"
	]
];
function process_0(input){
	split_input = input.split(" ");
	console.log("process_0:" + split_input);
	if(split_input[0] == "助けて"){
		var help_text = dump_help(0);
		p0_respond(help_text);
	}else if(split_input[0] == "名前"){
		console.log(split_input[1]);
		if(split_input[1] !== undefined && split_input[1] !== ""){
			localStorage.setItem("name_CUICUI", split_input[1]);
			p0_respond("お名前が登録されました。");
		}else{
			p0_respond("第2引数にお名前を入力してください。")
		}
	}else if(split_input[0] == "一覧"){
		var ajax_res = myajax({arg1:"view"});
		p0_respond(ajax_res);
	}else if(split_input[0] == "作る"){
		if(split_input[1] !== undefined && split_input[1] !== ""){
			var ajax_res = myajax({arg1:"create", arg2: split_input[1]});
			p0_respond(ajax_res);
		}else{
			p0_respond("第2引数にインスタンス名を入力してください。")
		}
	}else if(split_input[0] == "入る"){
		if(split_input[1] !== undefined && split_input[1] !== ""){
			var ajax_res = myajax({arg1:"join", arg2: split_input[1]});
			p0_respond(ajax_res);
		}else{
			p0_respond("第2引数にインスタンス名を入力してください。")
		}
	}else if(split_input[0] == "rem"){
		localStorage.removeItem("name_CUICUI");
		p0_respond("removed name");
	}else{
		p0_respond("そのようなコマンドはありません。");
	}
}
function dump_help(which){
	var help = help_text[which];
	var res = "<ul>";
	help.forEach((x) => {
		res += "<li>" + x + "</li>";
	});
	res += "</ul>";
	return res;
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

function p0_respond(arg_text){
	var response_div = $('<div>'+arg_text+'</div>');
	var input_div = $('<div>');
	var stored_name = localStorage.getItem("name_CUICUI");
	if(stored_name == null){stored_name = "Unknown";}
	var input_div_name = $('<span>', {class:'green-name', text: stored_name});
	var input_div_input = $('<input>', {class: 'user-input input-ue'})
	input_div_input.keydown((e) => {
		if(e.key == "Enter"){
			var input = elms_input[0].last().val();
			process_0(input);
		}
	});
	input_div.append(input_div_name);
	input_div.append(": ");
	input_div.append(input_div_input);

	$("#p2").append(response_div);
	$("#p2").append(input_div);
	input_div_input.focus();
}