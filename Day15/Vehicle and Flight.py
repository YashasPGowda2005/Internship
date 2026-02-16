class Vehicle:
    def __init__(self, vehicle_type, speed):
        self.vehicle_type = vehicle_type
        self.speed = speed

class Flight(Vehicle):
    def __init__(self, vehicle_type, speed, flight_number, duration):
        super().__init__(vehicle_type, speed)
        self.flight_number = flight_number
        self.duration = duration

    def flight_summary(self):
        return f"Flight {self.flight_number} ({self.vehicle_type}) travels at {self.speed} km/h for {self.duration} hours"

f = Flight("Airplane", 600, "A1202", 2)
print(f.flight_summary())
