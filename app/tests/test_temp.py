import pytest
import app

def test_patch():
    print(app.w)
    print(dir(app.w))
    assert hasattr(app.w,'MSAcpi_ThermalZoneTemperature')

def test_patch_result():
    assert type(app.w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature) == int 

def test_get_temp():
    this_temp = app.get_temp('CurrentTemperature')
    assert this_temp >= 0 and this_temp < 2000

def test_get_trip_point():
    critical_point = app.get_temp('CriticalTripPoint')
    assert critical_point == 1500

def test_get_temp_missing():
    missing = app.get_temp('Missing Property')
    assert missing == None


