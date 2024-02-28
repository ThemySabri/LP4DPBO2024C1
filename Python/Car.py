from Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, license_plate, brand, year, color, num_seats, num_doors):
        super().__init__(license_plate, brand, year, color)
        self.__num_seats = num_seats
        self.__num_doors = num_doors

    def get_num_seats(self):
        return self.__num_seats

    def set_num_seats(self, num_seats):
        self.__num_seats = num_seats

    def get_num_doors(self):
        return self.__num_doors

    def set_num_doors(self, num_doors):
        self.__num_doors = num_doors
