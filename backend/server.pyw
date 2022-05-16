from flask import Flask, jsonify
import wmi

import datetime

app = Flask(__name__)

w = wmi.WMI(namespace="root\wmi")

def get_temp(property):
    w_class = w.MSAcpi_ThermalZoneTemperature()[0]
    result = getattr(w_class,property,None)
    if not result is None:
        # conversion from 10x deg K to 10x deg C
        return result - 2732

@app.route('/current-temp')
def get_current_temp():
    temp = get_temp('CurrentTemperature')
    dt = datetime.datetime.now()
    current_temp = {'datetime': str(dt), 'temp': temp - 2732}    
    return jsonify(current_temp)

@app.route('/trip-points')
def get_trip_point():
    class_properties = ['ActiveTripPoint','PassiveTripPoint','CriticalTripPoint']    
    trip_points = {property: get_temp(property) for property in class_properties}
    return jsonify(trip_points)

if __name__ == '__main__':
    app.run(
        'TempWatch backend', 
        host = '127.0.0.1', 
        port = 4999,
        debug = False
    )