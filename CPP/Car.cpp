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
#include "Vehicle.cpp"

using namespace std;

class Car : public Vehicle
{
private:
    int num_seats;
    int num_doors;

public:
    // Constructor
    Car(std::string license_plate, std::string brand, int year, std::string color, int num_seats, int num_doors)
        : Vehicle(license_plate, brand, year, color), num_seats(num_seats), num_doors(num_doors) {}

    // Getter and Setter for number of seats
    int get_num_seats()
    {
        return num_seats;
    }

    void set_num_seats(int new_num_seats)
    {
        num_seats = new_num_seats;
    }

    // Getter and Setter for number of doors
    int get_num_doors()
    {
        return num_doors;
    }

    void set_num_doors(int new_num_doors)
    {
        num_doors = new_num_doors;
    }
};