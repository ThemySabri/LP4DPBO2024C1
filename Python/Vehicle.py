class Vehicle:
    def __init__(self, plate_number, brand, year, color):
        self.__plate_number = plate_number
        self.__brand = brand
        self.__year = year
        self.__color = color

    def get_plate_number(self):
        return self.__plate_number

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
