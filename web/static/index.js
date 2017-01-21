console.log('static script working...')

$(document).ready(function(){

	$('button[color]').click(function(event) {
		var color = event.target.getAttribute('color')
		$.post('/led_light/' + color, function(result) {
			if (result.ledState === 'on') {
				event.target.classList.add('led-on')
			} else {
				event.target.classList.remove('led-on')
			}
		})
	})
	
	$('button[rgbcolor]').click(function(event) {
		var color = event.target.getAttribute('rgbcolor')
		$.post('/rgb_light/' + color, function(result) {
			if (result.ledState === 'on') {
				event.target.classList.add('led-on')
			} else {
				event.target.classList.remove('led-on')
			}
		})
	})

	$('#beep').click(function() {
		$.post('/beep/35')
	})

});
