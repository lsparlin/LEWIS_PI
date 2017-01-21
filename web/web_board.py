from flask import Flask, render_template,  make_response
import gpio, led, rgb, buzzer

gpio.bcmMode()
colors = led.myColorsByName()
rgb_colors = rgb.myColorsByName()
color_states = {k: False for k in list(colors.keys())}
rgb_states = {k: False for k in list(rgb_colors.keys())}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', colorStates=color_states, rgbStates=rgb_states)

@app.route('/led_light/<string:color>', methods=['POST'])
def change_led_light(color):
    colorInt = colors.get(color, led.white)
    state = 'on' if color_states.get(color) == False else 'off'
    set(colorInt, state)
    color_states[color] = not color_states[color]
    return make_response('{"status": "Success", "ledState": "' + state + '"}', 200, {'Content-Type': 'application/json'})

@app.route('/rgb_light/<string:color>', methods=['POST'])
def change_rgb_light(color):
    colorInt = rgb_colors.get(color, led.white)
    state = 'on' if rgb_states.get(color) == False else 'off'
    set(colorInt, state)
    rgb_states[color] = not rgb_states[color]
    return make_response('{"status": "Success", "ledState": "' + state + '"}', 200, {'Content-Type': 'application/json'})

def set(colorInt, state):
    if state != None and state == 'off':
        gpio.pinOff(colorInt)
    else:
        gpio.pinOn(colorInt)

@app.route('/beep', methods=['POST'])
@app.route('/beep/<int:millis>', methods=['POST'])
def beep_for(millis=None):
    if millis == None:
        millis = 100
    buzzer.beep(25, millis/1000)
    return make_response('{"status": "Success"}', 200)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

gpio.pinOff(list(colors.values()))
gpio.pinOff(list(rgb_colors.values()))
gpio.cleanup()
