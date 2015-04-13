$('.menu-anchor').on('click touchstart', function(e){
	$('html').toggleClass('menu-active');
  	e.preventDefault();
});

// /bla
$('.user_info').on('click touchstart', function(e){
	$('.user_info li').toggleClass('active');
});
