class Vehicle:
    def __init__(self, number):
        self.number = number
        self.__fuel_level = 100
        self.__mileage = 0

    def refuel(self, manager, amount):
        if isinstance(manager, FleetManager):
            self.__fuel_level = min(100, self.__fuel_level + amount)
        else:
            print("Ruxsat yo‘q!")

    def drive(self, km):
        if self.__fuel_level >= km * 0.1:
            self.__fuel_level -= km * 0.1
            self.__mileage += km
        else:
            print("Yonilg‘i yetarli emas!")

    def get_status(self):
        return f"Yonilg‘i: {self.__fuel_level:.1f}%, Yurgan: {self.__mileage} km"


class FleetManager:
    pass


class Driver:
    pass



v = Vehicle("80A123AA")
mgr = FleetManager()
v.refuel(mgr, 20)
v.drive(200)
print(v.get_status())
