# Bismillah
# Saya Themy Sabri Syuhada dengan NIM 2203903. Demi keberkahan-Nya, saya berjanji mengerjakan latihan praktikum 4 DPBO dengan jujur dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
# Aamiin.

class Garage:
    def __init__(self, name, area):
        self.__name = name
        self.__area = area
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def get_vehicles(self):
        return self.__vehicles

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area