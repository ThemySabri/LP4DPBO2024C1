class Vehicle:
    def __init__(self, license_plate, brand, year, color):
        self.__license_plate = license_plate
        self.__brand = brand
        self.__year = year
        self.__color = color

    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate

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
