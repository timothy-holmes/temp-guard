from flask import Flask, jsonify, render_template
import wmi

import datetime, os

app = Flask(__name__)
w = wmi.WMI(namespace = r"root\wmi")

def get_temp(property):
    try:
        w_class = w.MSAcpi_ThermalZoneTemperature()[0]
        temp = getattr(w_class,property,None)
    except Exception as e:
        temp = None
        print('get_temp error',e)

    # convert from deci-degrees Kelvin to deci-degrees Celcius
    if not temp is None:
        temp = temp - 2732
    return temp

@app.route('/')
def index():
    return render_template('index.html.j2')

@app.route('/current-temp')
def get_current_temp():
    temp = get_temp('CurrentTemperature')
    dt = datetime.datetime.now()
    current_temp = {'datetime': str(dt), 'temp': temp}    
    return jsonify(current_temp)

@app.route('/trip-points')
def get_trip_point():
    class_properties = ['ActiveTripPoint','PassiveTripPoint','CriticalTripPoint']    
    trip_points = {property: get_temp(property) for property in class_properties}
    return jsonify(trip_points)

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 4999, debug = False)