class Vehicle:
    def __init__(self, license_plate, brand, year, color):
        self.license_plate = license_plate
        self._brand = brand
        self._year = year
        self._color = color

    def get_license_plate(self):
        return self.license_plate

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def __str__(self):
        return f"{self.license_plate}\t{self._brand}\t{self._year}\t{self._color}"


class Car(Vehicle):
    def __init__(self, license_plate, brand, year, color, doors, fuel_type):
        super().__init__(license_plate, brand, year, color)
        self._doors = doors
        self._fuel_type = fuel_type

    def get_doors(self):
        return self._doors

    def set_doors(self, doors):
        self._doors = doors

    def get_fuel_type(self):
        return self._fuel_type

    def set_fuel_type(self, fuel_type):
        self._fuel_type = fuel_type

    def __str__(self):
        return super().__str__() + f"\t{self._doors}\t{self._fuel_type}"


class Motorcycle(Vehicle):
    def __init__(self, license_plate, brand, year, color, type):
        super().__init__(license_plate, brand, year, color)
        self._type = type

    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type

    def __str__(self):
        return super().__str__() + f"\t{self._type}"


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
            print(
                f"{vehicle.get_plate_number()}\t{vehicle.get_brand()}\t{vehicle.get_year()}\t{vehicle.get_color()}")


garage = Garage("My Garage", 50.5)
car1 = Car("AB 1234 CD", "Toyota", 2022, "Black", 5, "Gasoline")
motorcycle1 = Motorcycle("B 5678 EF", "Honda", 2023, "Red", "Sport")

garage.add_vehicle(car1)
garage.add_vehicle(motorcycle1)

garage.display_vehicles()
