from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plate_number, brand, year, color, motor_type, tank_capacity):
        super().__init__(plate_number, brand, year, color)
        self.__motor_type = motor_type
        self.__tank_capacity = tank_capacity

    def get_motor_type(self):
        return self.__motor_type

    def set_motor_type(self, motor_type):
        self.__motor_type = motor_type

    def get_tank_capacity(self):
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity):
        self.__tank_capacity = tank_capacity
