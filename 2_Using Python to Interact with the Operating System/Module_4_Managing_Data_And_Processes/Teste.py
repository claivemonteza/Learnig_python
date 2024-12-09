class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass

school_bus = bus("School volvo", 180, 12)
print("Vihicle name:", school_bus.name,school_bus.max_speed,school_bus.mileage)