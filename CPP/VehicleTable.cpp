/*
Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903.
Demi keberkahan-Nya, saya berjanji mengerjakan
latihan praktikum 4 DPBO dengan jujur
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.
*/

#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"

using namespace std;

// Kelas untuk menampilkan data kendaraan dalam bentuk tabel yang dinamis
class VehicleTable
{
private:
    std::vector<Vehicle *> vehicles;

public:
    // Constructor
    VehicleTable(std::vector<Vehicle *> vehicles)
        : vehicles(vehicles) {}

    // Metode untuk menampilkan tabel kendaraan
    void display()
    {
        // Jika tidak ada kendaraan, tampilkan pesan
        if (vehicles.empty())
        {
            std::cout << "No vehicles to display." << std::endl;
            return;
        }

        // Menghitung lebar setiap kolom
        int license_plate_width = 13; // Minimum lebar untuk nomor plat
        int brand_width = 5;          // Minimum lebar untuk merek
        int year_width = 4;           // Minimum lebar untuk tahun
        int color_width = 5;          // Minimum lebar untuk warna

        for (Vehicle *vehicle : vehicles)
        {
            license_plate_width = std::max(license_plate_width, (int)vehicle->get_license_plate().length());
            brand_width = std::max(brand_width, (int)vehicle->get_brand().length());
            year_width = std::max(year_width, (int)std::to_string(vehicle->get_year()).length());
            color_width = std::max(color_width, (int)vehicle->get_color().length());
        }

        // Menampilkan header tabel
        std::cout << std::left << std::setw(license_plate_width) << "License Plate |"
                  << std::left << std::setw(brand_width) << "Brand |"
                  << std::left << std::setw(year_width) << "Year |"
                  << std::left << std::setw(color_width) << "Color" << std::endl;

        // Menampilkan garis pembatas antara header dan data
        std::cout << std::setfill('-') << std::setw(license_plate_width + 15) << "-"
                  << std::setw(brand_width + 3) << "-"
                  << std::setw(year_width + 3) << "-"
                  << std::setw(color_width + 3) << "-" << std::endl;

        // Menampilkan data kendaraan
        std::cout << std::setfill(' ');
        for (Vehicle *vehicle : vehicles)
        {
            std::cout << std::left << std::setw(license_plate_width) << vehicle->get_license_plate() + " |"
                      << std::left << std::setw(brand_width) << vehicle->get_brand() + " |"
                      << std::left << std::setw(year_width) << std::to_string(vehicle->get_year()) + " |"
                      << std::left << std::setw(color_width) << vehicle->get_color() << std::endl;
        }
    }
};