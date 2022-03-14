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

function process_0(input){
	split_input = input.split(" ");
	console.log("process_0:" + split_input);
	if(split_input[0] == "助けて"){
		p0_respond(dump_help(0));
	}else if(split_input[0] == "助けてい"){
		p0_respond(dump_help(1));
	}else if(split_input[0] == "名前"){
		console.log(split_input[1]);
		if(split_input[1] !== undefined && split_input[1] !== ""){
			if(split_input[1].length <= 16){
				localStorage.setItem("name", split_input[1]);
				p0_respond("お名前が登録されました。");
			}else{
				p0_respond("お名前は16文字以内でお願いします。");
			}
		}else{
			p0_respond("第2引数にお名前を入力してください。")
		}
	}else if(split_input[0] == "一覧"){
		var ajax_res = myajax({arg1:"view"});
		p0_respond(ajax_res);
	}else if(split_input[0] == "作る"){
		if(split_input[1] !== undefined && split_input[1] !== ""){
			if(split_input[1].length <= 16){
				var ajax_res = myajax({arg1:"create", arg2: split_input[1]});
				p0_respond(ajax_res);
			}else{
				p0_respond("インスタンス名は16文字以内でお願いします。")
			}
		}else{
			p0_respond("第2引数にインスタンス名を入力してください。")
		}
	}else if(split_input[0] == "入る"){
		if(split_input[1] !== undefined && split_input[1] !== ""){
			var ajax_res = myajax({
				arg1:"join", arg2: split_input[1], 
				arg3: localStorage.getItem("name")
			});
			if(ajax_res.includes("[成功]")){
				p0_respond(ajax_res);
				shita_start();
			}else{
				p0_respond(ajax_res);
			}
		}else{
			p0_respond("第2引数にインスタンス名を入力してください。")
		}
	}else if (split_input[0] == "test"){
		p0_respond(myajax({arg1:"test"}));
	}else if (split_input[0] == "clear"){
		p0_respond(myajax({arg1:"clear"}));
	}else if(split_input[0] == "rem"){
		localStorage.removeItem("name");
		p0_respond("removed name");
	}else{
		p0_respond("そのようなコマンドはありません。");
	}
}
const help_text = [
	[
		"名前 `名前`: ユーザーネームを`名前`に設定",
		"一覧: 現在開いている対戦インスタンスを表示",
		"作る `名前`: 対戦インスタンス`名前`を作成",
		"入る `名前`: 対戦インスタンス`名前`に入室する",
		"助けてい: インスタンスの設定に関するコマンドを表示"
	],
	[
		"開発中です……"
	]
];
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