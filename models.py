class Vehicle:
    def __init__(self, make, model, year, vin):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin

class Maintenance:
    def __init__(self, vehicle_id, description, date, mileage, reminder):
        self.vehicle_id = vehicle_id
        self.description = description
        self.date = date
        self.mileage = mileage
        self.reminder = reminder
