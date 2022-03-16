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
	split_input = input.replaceAll("　", "").split(" ");
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

function process_0(input){
	split_input = input.replaceAll("　", " ").split(" ");
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
	}else if(split_input[0] == "bot"){
		const arr_10lv = [1,2,3,4,5,6,7,8,9,10];
		//const arr_3blends = ["強","中","弱"];
		console.log(localStorage.getItem("instance"));
		if(localStorage.getItem("instance") !== 'null'){
			if(split_input[1] !== undefined && 
				arr_10lv.indexOf(Number(split_input[1])) !== -1 ){
					res = add_bot(Number(split_input[1]));
					p0_respond(res);
			}/*else if(split_input[1] !== undefined && 
				arr_3blends.indexOf(split_input[1]) !== -1 ){
					res = ""
					var omakase_map = {
						"弱": [1,2,3,4],
						"中": [4,5,6,7],
						"強": [7,8,9,10]
					}
					omakase_map[split_input[1]].forEach((e, i) => {
						res += add_bot(e);
						await wait(1000);
					});
					p0_respond(res);
			}*/else{
				p0_respond("コマンドが不正です。");
			}
		}else{
			p0_respond("インスタンスにまだ参加していません。");
		}

	}else if (split_input[0] == "test"){
		p0_respond(myajax({arg1:"test"}));
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
		"入る `名前`: 対戦インスタンス`名前`に入室する"
	],
	[
		"Tabキー: コマンドエリアとタイピングエリアを往復",
		/*"`bot 強`: おまかせbotブレンド4個体(強)",
		"`bot 中`: おまかせbotブレンド4個体(中)",
		"`bot 弱`: おまかせbotブレンド4個体(弱)",*/
		"`bot [1-10]`: botを1個体だけ追加。レベルは10段階"
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
 
function add_bot(level){
	return myajax({
		arg1:"bot", 
		arg2: localStorage.getItem("instance"), 
		arg3: level
	});
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

const wait = async (ms) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(); // setTimeoutの第一引数の関数として簡略化できる
    }, ms)
  });
}