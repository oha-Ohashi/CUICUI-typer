$(() => {
	//インスタンス情報初期化
	localStorage.setItem("instance", null);
});

function shita_start(){
	localStorage.setItem("instance", split_input[1])
	p1_respond(" ", " ");
	setInterval(() => {
		p1_sync();
	}, 0);
}

let sound_enter = new Audio("https://github.com/oha-Ohashi/cuicui/blob/main/media/enter1.mp3?raw=true");

function p1_respond(odai_text, disp_text){
	var odai_div = $('<div id="odai">'+odai_text+'</div>');
	var input_div = $('<input>', {class: 'user-input input-shita'})

	input_div.last().click((e)=>{
		input_switch = true;
	});
	input_div.keydown((e) => {
		console.log("た");
	});
	input_div.keyup((e) => {
		var input = input_div.val();
		myajax({
			arg1:"wip", 
			arg2: input,
			arg3: localStorage.getItem("name"), 
			arg4: localStorage.getItem("instance")
		});
		//console.log("途中: "+ input);
		//console.log("おだい: "+ $("#odai").text());
		if (input == $("#odai").text()){
			console.log("ピコーン");
			sound_enter.play();
		}

		if(e.key === "Enter"){
			console.log("enta--");
			input_div.val("");
		}
	});

	var disp_div = $('<div id=disp>'+disp_text+'</div>')

	$("#p3").empty();
	$("#p3").append(odai_div);
	$("#p3").append(input_div);
	$("#p3").append(disp_div);
	//input_div.focus();
	//input_switch = !input_switch;
}

function p1_sync(){
	res = myajax({
		arg1: "sync",
		arg3: localStorage.getItem("name"),
		arg4: localStorage.getItem("instance")
	});
	//console.log(res);
	var odai_text = res.split('\\')[0];
	var disp_text = res.split('\\')[1];
	//console.log("sync!");
	var odai_div = $('<div id="odai">'+odai_text+'</div>');
	var disp_div = $('<div id=disp>'+disp_text+'</div>')
	$("#odai").html(odai_div);
	$("#disp").html(disp_div);
}