$(() => {
	size_sync();
});
$(window).resize(() => {
	size_sync();
});

var w_width = 0;
var w_height = 0;
function size_sync(){
	w_width = $(window).width();
	w_height = $(window).height();
	//console.log("width: "+w_width+"height: "+w_height);
	if(w_width < 768){
		resize_tate([10, 30, 50]);
	}else{
		resize_tate([10, 80, 80]);
	}
}
function resize_tate(arr){
	var h_percent = arr;
	$(".pane").each(function(index){
		//console.log(index);
		$(this).height(h_percent[index]/100 * w_height + "px");
		//$(this).css("overflow", "scroll");
	});
}