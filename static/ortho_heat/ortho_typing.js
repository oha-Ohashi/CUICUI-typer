$(() => {
});
var n_times = 30;
var timers = Array(n_times);
var level = 3;
var score = 0;
var intervals = [2000,1500,1000,500,300]
var speeds = [6000, 4000, 2500, 2000, 2000]


let sound_click = new Audio("https://github.com/oha-Ohashi/cuicui/blob/main/media/ortho_typing/click.mp3?raw=true");
let sound_wrong = new Audio("https://github.com/oha-Ohashi/cuicui/blob/main/media/ortho_typing/wrong.mp3?raw=true");
let sound_failure = new Audio("https://github.com/oha-Ohashi/cuicui/blob/main/media/ortho_typing/failure.mp3?raw=true");

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
function getRandomChar(){
	var abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	var index = getRandomInt(26);
	return abc[index];
}
function randomize(n){
	ran = (Math.random() - 0.5) * (n * 0.7);
	return n + ran;
}
class Target {
	constructor() {
		this.dom = $("<div></div>", {
			text: getRandomChar(),
			css: {left: getRandomInt(10) * 70 + "px"}
		});
		$(".playground").append(this.dom);

		this.fall(speeds[level-1]);
	}	
	fall(ms_to_fall){
		$(this.dom).animate(
			{top:"430px"},
			ms_to_fall,
			"linear"
		);
		setTimeout(() => {
			$(this.dom).remove();
		}, ms_to_fall);

	}
}


function synckeymap(){
	var layout = $(".layout-mod textarea").val().replaceAll("\n", "");
	console.log("keymap:" + layout);
	for(var i = 0; i < 30; i++){
		$(".key").eq(i).text(layout[i]);
	}
}

function doit(){
	score = 0;
	synckeymap();
	$("#progress").text(score + "/" + n_times);
	for(var i = 0; i < n_times; i++){
		timers[i] = setTimeout(function(){
			new Target();
		}, i*intervals[level-1] + randomize(intervals[level-1]));
	}
}

$("#formRange1").change(function(){
	var value = $(this).val();
	console.log(value);
	level = value;
	$(".range-label span").text(value);
});

$("#play").click(function(){
	doit();
});
$("#quit").click(function(){
	timers.forEach(function(t){
		clearInterval(t);
	});
	$(".playground").empty();
	$("#progress").text("");
});


$("body").keydown(function(e){
	if(e.key == "Enter"){
		doit();
	}
	if(e.keyCode >= 65 && e.keyCode <= 90){
		var wrong_flag = true;
		$(".playground div").each(function(){
			var low = $(this).text().toLowerCase();
			//console.log(low);
			if(e.key == low){
				$(this).remove();
				score++;
				wrong_flag = false;
				$("#progress").text(score + "/" + n_times);
			}
		});
		if(wrong_flag){
			sound_wrong.play();
		}else{
			sound_click.play();
		}
	}
});