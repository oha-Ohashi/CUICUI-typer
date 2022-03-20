
// minimal heatmap instance configuration
var heatmapInstance = h337.create({
// only container is required, the rest will be defaults
	container: document.querySelector('.heatmap'),
	radius: 70,
	maxOpacity: .4
});


function createheatmap(layout, text){
	console.log(layout);
	console.log(text);
	console.log(text.length)

	for(var i = 0; i < 30; i++){
		$(".key").eq(i).text(layout[i]);
	}

	var max = text.length / 20;
	var points = [];
	var one_u = 70;

	for (var i = 0; i < text.length; i++) {
		chr = text[i];
		elm = $(".key:contains("+chr.toUpperCase()+")")
		//console.log(elm.text());
		index = $(".heat-box .key").index(elm);
		//console.log(index);
		var y = Math.floor(index / 10);
		var x = index % 10;
		var point = {
			x: (x+0.5) * one_u,
			y: (y+0.5) * one_u,
			value: 1
		}
		points.push(point);
	}



	/*
	// now generate some random data
	var points = [];
	var max = 0;
	var width = 700;
	var height = 210;
	var len = 200;

	while (len--) {
	var val = Math.floor(Math.random()*100);
	max = Math.max(max, val);
	var point = {
		x: Math.floor(Math.random()*width),
		y: Math.floor(Math.random()*height),
		value: val
	};
	points.push(point);
	}
	*/
	 
	var data = {
		max: max,
		data: []
	}
	heatmapInstance.setData(data);
	// heatmap data format
	var data = { 
	max: max, 
	data: points 
	};
	// if you have a set of datapoints always use setData instead of addData
	// for data initialization
	// heatmapInstance.setData(data);
	heatmapInstance.setData(data);


};
