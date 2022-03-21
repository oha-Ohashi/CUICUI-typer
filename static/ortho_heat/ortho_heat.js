$(() => {
	$(".layout-mod textarea").val(layouts[0]);
	$(".text-mod textarea").val(texts[0]);

})

$("#create").click(() => {
	var layout = $(".layout-mod textarea").val().replaceAll("\n", "");
	var text = $(".text-mod textarea").val().replaceAll("\n", "");
	createheatmap(layout, text);
});

const layouts = [
	"QWERTYUIOP\nASDFGHJKL_\nZXCVBNM___",
	"ABCDEFGHIJ\nKLMNOPQRST\nUVWXYZ____",
	"___PYFGCRL\nAOEUIDHTNS\n_QJKXBMWVZ",
	"QWFPBJLUY_\nARSTGMNEIO\nZXCDVKH___",
	"QW___MRDYP\nAOEIUGTKSN\nZXCVFBHJL_",
	"_WBF_MRDYP\nAOEUIGTKNS\nZXCV__HJLQ",
	"ZGMK__CWPQ\nDNHTRIEAOU\nVFLS__YBXJ"
];
$(".layout-mod .btn-group .btn").on('click', function(){
	var index = $(".layout-mod .btn-group .btn").index($(this));
	console.log(index);
	$(".layout-mod textarea").val(layouts[index]);
	$(".layout-mod .btn-group .btn").removeClass('active');
	$(this).addClass('active');
});

const texts = [
	"It was on a dreary night of November that I beheld the accomplishment of my toils. With an anxiety that almost amounted to agony, I collected the instruments of life around me, that I might infuse a spark of being into the lifeless thing that lay at my feet. It was already one in the morning; the rain pattered dismally against the panes, and my candle was nearly burnt out, when, by the glimmer of the half-extinguished light, I saw the dull yellow eye of the creature open; it breathed hard, and a convulsive motion agitated its limbs.How can I describe my emotions at this catastrophe, or how delineate the wretch whom with such infinite pains and care I had endeavoured to form? His limbs were in proportion, and I had selected his features as beautiful. Beautiful! Great God! His yellow skin scarcely covered the work of muscles and arteries beneath; his hair was of a lustrous black, and flowing; his teeth of a pearly whiteness; but these luxuriances only formed a more horrid contrast with h"
	+ "konaida roan roan kun ni a xtu ta toki 、 maruzen no mise de 一 niti ni mannenhitu ga nani honi u reru daro u to tazu ne tara 、 roan kun ha oo i toki ha hyakumoto kurai de ru sou da to kota e ta 。 otto sore de ha 一 hon no mannenhitu ga dono kurai naga ku tuka eru daro u to ki i tara 、 konaida yokohama no mono de 、 pen ha mada ka nari da ga 、 ziku zi kuga he xtu ta kara ziku take dake kae kae te kure kure to i xtu te mo xtu te ki ta no ga aru ga 、 konohito ha 十三 nen mae ni 一 hon ka xtu ta giri de 、 sono 一 hon wo kyou made ta e zu siyou si te i ta no da to iu kara 、 kore kore ga maa itiban naga i rei rasii to hana si ta 。 si te mi ru to hutuu no baai de ha ikura zankoku ni tuka xtu te mo taitei 六七 nen no hosyou ha tu ke rareru no ga 、 ippan no mannenhitu no unmei rasii 。 一 hon de otto hodo sorehodo naga ku tuka eru mono ga hi ni hyakumoto mo de ru to i e ba mannenhitu wo zyuyou suru hito no hani ha hizyou na ikioi wo omonmi moxtu te hiro gari tutu aru to mi te mo manzara manzara kentoutiga",
	"It was on a dreary night of November that I beheld the accomplishment of my toils. With an anxiety that almost amounted to agony, I collected the instruments of life around me, that I might infuse a spark of being into the lifeless thing that lay at my feet. It was already one in the morning; the rain pattered dismally against the panes, and my candle was nearly burnt out, when, by the glimmer of the half-extinguished light, I saw the dull yellow eye of the creature open; it breathed hard, and a convulsive motion agitated its limbs.How can I describe my emotions at this catastrophe, or how delineate the wretch whom with such infinite pains and care I had endeavoured to form? His limbs were in proportion, and I had selected his features as beautiful. Beautiful! Great God! His yellow skin scarcely covered the work of muscles and arteries beneath; his hair was of a lustrous black, and flowing; his teeth of a pearly whiteness; but these luxuriances only formed a more horrid contrast with h",
	"konaida roan roan kun ni a xtu ta toki 、 maruzen no mise de 一 niti ni mannenhitu ga nani honi u reru daro u to tazu ne tara 、 roan kun ha oo i toki ha hyakumoto kurai de ru sou da to kota e ta 。 otto sore de ha 一 hon no mannenhitu ga dono kurai naga ku tuka eru daro u to ki i tara 、 konaida yokohama no mono de 、 pen ha mada ka nari da ga 、 ziku zi kuga he xtu ta kara ziku take dake kae kae te kure kure to i xtu te mo xtu te ki ta no ga aru ga 、 konohito ha 十三 nen mae ni 一 hon ka xtu ta giri de 、 sono 一 hon wo kyou made ta e zu siyou si te i ta no da to iu kara 、 kore kore ga maa itiban naga i rei rasii to hana si ta 。 si te mi ru to hutuu no baai de ha ikura zankoku ni tuka xtu te mo taitei 六七 nen no hosyou ha tu ke rareru no ga 、 ippan no mannenhitu no unmei rasii 。 一 hon de otto hodo sorehodo naga ku tuka eru mono ga hi ni hyakumoto mo de ru to i e ba mannenhitu wo zyuyou suru hito no hani ha hizyou na ikioi wo omonmi moxtu te hiro gari tutu aru to mi te mo manzara manzara kentoutiga"
];
$(".text-mod .btn-group .btn").on('click', function(){
	var index = $(".text-mod .btn-group .btn").index($(this));
	console.log(index);
	$(".text-mod textarea").val(texts[index]);
	$(".text-mod .btn-group .btn").removeClass('active');
	$(this).addClass('active');
});