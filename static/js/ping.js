$(function(){
	console.log("mimi abema");
	setInterval(function(){
		//console.log("mi");
		prev_time = $.now();
		//res = ajaj({url:"./ping", type:"GET", async:false, data:{mi:"mi"}});
		//res = "hoge"
		var ping = calc_ping($.now() - prev_time);
		$(".p1").eq(1).html(ping);
		
		//res = ajaj({url:"./data", type:"GET", data:{mi:"mi"}});
	}, 10);
});

function ajaj(req){
	$.ajax(req)
	// Ajax通信が成功したら発動
	.done( (data) => {
		//$('.result').html(data);
		return data
	})
	// Ajax通信が失敗したら発動
	.fail( (jqXHR, textStatus, errorThrown) => {
		console.log('Ajax通信に失敗しました。');
		console.log("jqXHR          : " + jqXHR.status); // HTTPステータスを表示
		console.log("textStatus     : " + textStatus);    // タイムアウト、パースエラーなどのエラー情報を表示
		console.log("errorThrown    : " + errorThrown.message); // 例外情報を表示
		return "commmunication failed."
	})
	// Ajax通信が成功・失敗のどちらでも発動
	.always( (data) => {
		//console.log("ajax attempted");
	});
}

function disp_it(paras){
	json_text = $.ajax(
		{
			url:"./data",
			type:"GET",
			data:paras,
			async:false
		}
	).responseText
	console.log("data: ");
	console.log(json_text);
	var json = JSON.parse(json_text);
	console.log(json);
	console.log(json.waku4);
	for(var i = 1; i <= 6; i++){
		var tag = "waku" + i;
		console.log(json[tag]);
		$("#"+tag).html(json[tag]);
	}
}

function ajah(req){
    return $.ajax(req);
}







var n_pings = 1000;
var pings = Array(n_pings);
for (var i = 0; i < n_pings; i++){
	pings[i] = 0;
}
function calc_ping(n){
	//console.log(n);
	pings.shift();
	pings.unshift(n);
	res = "ping: " + average(pings).toFixed(2) + "ms";
	return res;
}
var sum  = function(arr) {
    return arr.reduce(function(prev, current, i, arr) {
        return prev+current;
    });
};
var average = function(arr, fn) {
    return sum(arr, fn)/arr.length;
};

$(function(){
	// 「Ajax通信」ボタンをクリックしたら発動
	$('#ajax').on('click',function(){
		$.ajax({
			url:'./ping',
			type:'GET',
			data:{
				mi: "mi"
			}
		})
		// Ajax通信が成功したら発動
		.done( (data) => {
			$('.result').html(data);
		})
		// Ajax通信が失敗したら発動
		.fail( (jqXHR, textStatus, errorThrown) => {
			console.log('Ajax通信に失敗しました。');
			console.log("jqXHR          : " + jqXHR.status); // HTTPステータスを表示
			console.log("textStatus     : " + textStatus);    // タイムアウト、パースエラーなどのエラー情報を表示
			console.log("errorThrown    : " + errorThrown.message); // 例外情報を表示
		})
		// Ajax通信が成功・失敗のどちらでも発動
		.always( (data) => {
			//console.log("ajax attempted");
		});
	});
});