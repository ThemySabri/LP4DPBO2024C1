from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot


def main():
    if __name__ == "__main__":
        car1 = Car("ABC123", "Toyota", 2020, "Red", 5, 4)
        motorcycle1 = Motorcycle("DEF456", "Honda", 2019, "Black", "Sport", 10)
        car2 = Car("GHI789", "Ford", 2021, "Blue", 4, 2)

        garage = Garage("My Garage", 200)
        garage.add_vehicle(car1)
        garage.add_vehicle(motorcycle1)
        garage.add_vehicle(car2)

        print(f"Vehicles in {garage.get_name()} Garage:")
        print("Plate Number\tBrand\tYear\tColor")
        for vehicle in garage._Garage__vehicles:
            print(
                f"{vehicle.get_plate_number()}\t{vehicle.get_brand()}\t{vehicle.get_year()}\t{vehicle.get_color()}")

        parking_lot = ParkingLot(5)
        parking_lot.park_vehicle()
        parking_lot.park_vehicle()
        parking_lot.park_vehicle()
        parking_lot.park_vehicle()
        parking_lot.park_vehicle()
        parking_lot.park_vehicle()
