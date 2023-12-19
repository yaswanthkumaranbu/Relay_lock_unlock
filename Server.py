from flask import Flask, render_template
from flask_cors import CORS
# from machine import Pin
# import time

app = Flask(__name__)
CORS(app)

# SENSOR_PIN = 4

# Relay = Pin(15, Pin.OUT)
# Relay1 = Pin(14, Pin.OUT)
# sensor = Pin(SENSOR_PIN, Pin.IN)

# def read_proximity():
#     return sensor.value()

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/start')
def start_relay():
    print("Relay is on")
    # Relay.on()
    # Relay1.on()
    return 'Relay started'

@app.route('/stop')
def stop_relay():
    print("Relay is off")
    # Relay.off()
    # Relay1.off()
    return 'Relay stopped'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
