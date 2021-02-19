$(document).ready(function () {
	"use strict";
	$(window).scroll(function(){
		'use strict';
		if ($(this).scrollTop() > 1){  
			$('.navbar').addClass("scrolled");
		}
		else{
			$('.navbar').removeClass("scrolled");
		}
	});	
});