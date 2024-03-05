/*
Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903.
Demi keberkahan-Nya, saya berjanji mengerjakan
latihan praktikum 4 DPBO dengan jujur
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
*/

#include <string>
#include <vector>
#include <iostream>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"
#include "VehicleTable.cpp"

int main(int argc, char *argv[])
{
    // Membuat objek kendaraan (2 mobil dan 2 sepeda motor)
    Car *car1 = new Car("ABC123", "Toyota", 2020, "Red", 5, 4);
    Car *car2 = new Car("DEF456", "Honda", 2018, "Blue", 4, 4);
    Motorcycle *motorcycle1 = new Motorcycle("GHI789", "Yamaha", 2019, "Black", "Sport", 10);
    Motorcycle *motorcycle2 = new Motorcycle("JKL012", "Suzuki", 2021, "White", "Cruiser", 15);

    // Membuat objek garasi dan menambahkan kendaraan ke dalamnya
    Garage *garage = new Garage("My Garage", 200);
    garage->add_vehicle(car1);
    garage->add_vehicle(car2);
    garage->add_vehicle(motorcycle1);
    garage->add_vehicle(motorcycle2);

    // Menampilkan informasi kendaraan yang ada di dalam garasi
    std::cout << "Vehicles in the garage:" << std::endl;
    for (Vehicle *vehicle : garage->get_vehicles())
    {
        std::cout << "License Plate: " << vehicle->get_license_plate() << ", Brand: " << vehicle->get_brand()
                  << ", Year: " << vehicle->get_year() << ", Color: " << vehicle->get_color() << std::endl;
    }

    // Membuat objek tempat parkir dan mengelola parkir kendaraan
    ParkingLot *parking_lot = new ParkingLot(10);
    std::cout << "\nParking Lot Capacity: " << parking_lot->get_capacity() << std::endl;

    for (int i = 0; i < 12; i++)
    { // Melakukan parkir lebih dari kapasitas tempat parkir
        parking_lot->park_vehicle();
    }

    // Menampilkan jumlah kendaraan yang terparkir
    std::cout << "\nCurrent vehicles parked: " << parking_lot->get_current_count() << std::endl;

    // Mengosongkan tempat parkir
    parking_lot->vacate_spot();
    parking_lot->vacate_spot();

    // Menampilkan jumlah kendaraan yang terparkir
    std::cout << "\nCurrent vehicles parked: " << parking_lot->get_current_count() << std::endl;

    // Membersihkan memori dengan menghapus objek yang dialokasikan secara dinamis
    delete car1;
    delete car2;
    delete motorcycle1;
    delete motorcycle2;
    delete garage;
    delete parking_lot;

    return 0;
}
