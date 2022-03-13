$(() => {
	//インスタンス情報初期化
	localStorage.setItem("instance", null);
	localStorage.setItem("ready", false);
});
function process_1(input){
	console.log("process_1:");
	console.log(input);
	if(
		localStorage.getItem("instance") !== null &&
		localStorage.getItem("ready") == false &&
		input == "準備完了"
	){
		localStorage.setItem("ready", true);
	}
	p1_respond("[お題ゾーン]", "[プレイヤー一覧ゾーン]");
}

function shita_start(){
	localStorage.setItem("instance", split_input[1])
	p1_respond(
		"｢準備完了｣とタイプして、Ctrl+Enterを押してください。",
		""
	);
}

function p1_respond(odai_text, disp_text){
	var odai_div = $('<div>'+odai_text+'</div>');
	var input_div = $('<input>', {class: 'user-input input-shita'})
	input_div.keydown((e) => {
		if(e.ctrlKey == true && e.key == "Enter"){
			var input = elms_input[1].last().val();
			elms_input[1].last().val("");
			process_1(input);
		}
	});
	var disp_div = $('<div>'+disp_text+'</div>')

	$("#p3").empty();
	$("#p3").append(odai_div);
	$("#p3").append(input_div);
	$("#p3").append(disp_div);
	input_div.focus();
	input_switch = !input_switch;
}