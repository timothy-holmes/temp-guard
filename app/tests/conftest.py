import pytest

from tests.mockforWMI import MockWMI
import app

@pytest.fixture(autouse=True)
def patch_WMI(monkeypatch):
    monkeypatch.setattr(app,"w",MockWMI(namespace = 'whatever'))
    print('app.w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature')
    print(app.w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature)