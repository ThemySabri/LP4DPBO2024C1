'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''

from Vehicle import Vehicle           # Mengimpor kelas Vehicle
from Car import Car                   # Mengimpor kelas Car
from Motorcycle import Motorcycle     # Mengimpor kelas Motorcycle
from Garage import Garage             # Mengimpor kelas Garage
from ParkingLot import ParkingLot     # Mengimpor kelas ParkingLot


def main():
    # Membuat objek kendaraan (2 mobil dan 2 sepeda motor)
    car1 = Car("ABC123", "Toyota", 2020, "Red", 5, 4)
    car2 = Car("DEF456", "Honda", 2018, "Blue", 4, 4)
    motorcycle1 = Motorcycle("GHI789", "Yamaha", 2019, "Black", "Sport", 10)
    motorcycle2 = Motorcycle("JKL012", "Suzuki", 2021, "White", "Cruiser", 15)

    # Membuat objek garasi dan menambahkan kendaraan ke dalamnya
    garage = Garage("My Garage", 200)
    garage.add_vehicle(car1)
    garage.add_vehicle(car2)
    garage.add_vehicle(motorcycle1)
    garage.add_vehicle(motorcycle2)

    # Menampilkan informasi kendaraan yang ada di dalam garasi
    print("Vehicles in the garage:")
    for vehicle in garage.get_vehicles():
        print(f"License Plate: {vehicle.get_license_plate()}, Brand: {vehicle.get_brand()}, "
              f"Year: {vehicle.get_year()}, Color: {vehicle.get_color()}")

    # Membuat objek tempat parkir dan mengelola parkir kendaraan
    parking_lot = ParkingLot(10)
    print(f"\nParking Lot Capacity: {parking_lot.get_capacity()}")

    for i in range(12):  # Melakukan parkir lebih dari kapasitas tempat parkir
        parking_lot.park_vehicle()

    # Menampilkan jumlah kendaraan yang terparkir
    print(f"\nCurrent vehicles parked: {parking_lot.get_current_count()}")

    # Mengosongkan tempat parkir
    parking_lot.vacate_spot()
    parking_lot.vacate_spot()

    # Menampilkan jumlah kendaraan yang terparkir
    print(f"\nCurrent vehicles parked: {parking_lot.get_current_count()}")


if __name__ == "__main__":
    main()
