var formLogin = $('.form-login')
var butonUser = $('.button-user')
var buttonPlace = $('.button-place')
var formSiginUser = $('.form-user')
var formSiginPlace = $('.form-place')

formLogin.hide()
formSiginUser.hide()
formSiginPlace.hide()
butonUser.hide()
buttonPlace.hide()

$('button').click(function(){
	if ($(this).hasClass("sigin")) {
		$('form').hide();
		butonUser.toggle();
		buttonPlace.toggle();
	} else if ($(this).hasClass("login")) {
		$('form').hide();
		formLogin.toggle();
	} else if ($(this).hasClass("button-user")) {
		$('form').hide();
		formSiginUser.toggle();
	} else if ($(this).hasClass("button-place")) {
		$('form').hide();
		formSiginPlace.toggle();
	};
});

