from typing import Optional
from flask import Flask, jsonify, render_template, Response
import wmi

import datetime, os
import ctypes
import pythoncom

app = Flask(__name__)

def am_i_admin():
    try:
         is_admin = os.getuid() == 0
    except AttributeError:
         is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin == True

def get_temp(attr: str = 'CurrentTemperature') -> Optional[int]:
    # try:
    w0 = wmi.WMI(namespace=r'root\wmi').MSAcpi_ThermalZoneTemperature()[0]
    temp = getattr(w0,attr,None)

    # except Exception as e: # this is bad practice, TODO: isolate exception types
        # temp = None
        # print('get_temp error',e)
        # for p in dir(e):
        #     if not p.startswith('_'):
        #         print(property,getattr(e,p))
    
    # convert from deci-degrees Kelvin to deci-degrees Celcius
    return temp  - 2732

@app.route('/')
def index() -> str:
    return render_template('index.html.j2')

@app.route('/current-temp')
def get_current_temp() -> Response:
    temp = get_temp('CurrentTemperature')
    dt = datetime.datetime.now()
    current_temp = {'datetime': str(dt), 'temp': temp}    
    return jsonify(current_temp)

@app.route('/trip-points')
def get_trip_point() -> Response:
    class_attrs = ['ActiveTripPoint','PassiveTripPoint','CriticalTripPoint']    
    trip_points = {a: get_temp(a) for a in class_attrs}
    return jsonify(trip_points)

if __name__ == '__main__':
    debug = False # use True for integration testing, TODO: move to a .env
    if debug:
        from tests.mockforWMI import MockWMI
        w = MockWMI(namespace = 'test WMI')
    if am_i_admin():
        app.run(host = '127.0.0.1', port = 4999, debug = debug)