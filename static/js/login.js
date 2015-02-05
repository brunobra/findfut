var formLogin = $('.form-login')
var formSigin = $('.form-sigin')

formLogin.hide()
formSigin.hide()

$('button').click(function(){
	if ($(this).hasClass("sigin")) {
		formLogin.hide();
		formSigin.toggle();
	} else if ($(this).hasClass("login")) {
		formSigin.hide();
		formLogin.toggle();
	}
});

