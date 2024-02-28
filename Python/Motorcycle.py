from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, license_plate, brand, year, color, type_motorcycle, tank_capacity):
        super().__init__(license_plate, brand, year, color)
        self.__type_motorcycle = type_motorcycle
        self.__tank_capacity = tank_capacity

    def get_type_motorcycle(self):
        return self.__type_motorcycle

    def set_type_motorcycle(self, type_motorcycle):
        self.__type_motorcycle = type_motorcycle

    def get_tank_capacity(self):
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity):
        self.__tank_capacity = tank_capacity