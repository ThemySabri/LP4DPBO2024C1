from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot


def main():
    car1 = Car("ABC123", "Toyota", 2020, "Red", 5, 4)
    car2 = Car("DEF456", "Honda", 2018, "Blue", 4, 4)
    motorcycle1 = Motorcycle("GHI789", "Yamaha", 2019, "Black", "Sport", 10)
    motorcycle2 = Motorcycle("JKL012", "Suzuki", 2021, "White", "Cruiser", 15)

    garage = Garage("My Garage", 200)
    garage.add_vehicle(car1)
    garage.add_vehicle(car2)
    garage.add_vehicle(motorcycle1)
    garage.add_vehicle(motorcycle2)

    print("Vehicles in the garage:")
    for vehicle in garage.get_vehicles():
        print(f"License Plate: {vehicle.get_license_plate()}, Brand: {vehicle.get_brand()}, "
              f"Year: {vehicle.get_year()}, Color: {vehicle.get_color()}")

    parking_lot = ParkingLot(10)
    print(f"\nParking Lot Capacity: {parking_lot.get_capacity()}")

    for i in range(12):
        parking_lot.park_vehicle()

    print(f"\nCurrent vehicles parked: {parking_lot.get_current_count()}")

    parking_lot.vacate_spot()
    parking_lot.vacate_spot()

    print(f"\nCurrent vehicles parked: {parking_lot.get_current_count()}")


if __name__ == "__main__":
    main()
