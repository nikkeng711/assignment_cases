class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.diesel_slots = diesel
        self.petrol_slots = petrol
        self.electric_slots = electric

    def fuel_vehicle(self, fuel_type):
        if fuel_type == "diesel":
            if self.diesel_slots > 0:
                self.diesel_slots -= 1
                return True
        elif fuel_type == "petrol":
            if self.petrol_slots > 0:
                self.petrol_slots -= 1
                return True
        elif fuel_type == "electric":
            if self.electric_slots > 0:
                self.electric_slots -= 1
                return True
        return False  

    def open_fuel_slot(self, fuel_type):
        if fuel_type == "diesel":
            self.diesel_slots += 1
            return True
        elif fuel_type == "petrol":
            self.petrol_slots += 1
            return True
        elif fuel_type == "electric":
            if self.electric_slots < 1:  
                return False
            self.electric_slots += 1
            return True
        return False  

fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.fuel_vehicle("petrol"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.fuel_vehicle("electric"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.open_fuel_slot("diesel"))  
print(fuel_station.fuel_vehicle("diesel"))  
print(fuel_station.open_fuel_slot("electric"))  
print(fuel_station.open_fuel_slot("electric"))  