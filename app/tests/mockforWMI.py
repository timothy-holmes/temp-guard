from random import randint
from typing import List

class MockTempResponse:
    def __init__(self) -> None:
        values = {'ActiveTripPoint': 2732 + 500,
                'PassiveTripPoint': 2732 + 1000,
                'CriticalTripPoint': 2732 + 1500,
                'CurrentTemperature': randint(2732, 2732 + 2000)}
        for property,property_value in values.items():
            setattr(self,property,property_value)

class MockWMI:
    def __init__(self,namespace) -> None: 
        self.namespace = namespace

    def __repr__(self) -> str:
        return f'<MockWMI {self.namespace}>'
    
    @staticmethod
    def MSAcpi_ThermalZoneTemperature() -> List[MockTempResponse]:
        return [MockTempResponse()]