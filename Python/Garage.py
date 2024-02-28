class Garage:
    def __init__(self, name, area):
        self.__name = name
        self.__area = area
        self.__vehicles = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def display_vehicles(self):
        print(f"Vehicles in {self.__name} Garage:")
        print("Plate Number\tBrand\tYear\tColor")
        for vehicle in self.__vehicles:
            print("vehicle.get_plate_number()}\t{vehicle.get_brand()}\t{vehicle.get_year()}\t{vehicle.get_color()}")
