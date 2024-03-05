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

class Motorcycle : public Vehicle
{
private:
    std::string type_motorcycle;
    int tank_capacity;

public:
    // Constructor
    Motorcycle(std::string license_plate, std::string brand, int year, std::string color, std::string type_motorcycle, int tank_capacity)
        : Vehicle(license_plate, brand, year, color), type_motorcycle(type_motorcycle), tank_capacity(tank_capacity) {}

    // Getter and Setter for type of motorcycle
    std::string get_type_motorcycle()
    {
        return type_motorcycle;
    }

    void set_type_motorcycle(std::string new_type_motorcycle)
    {
        type_motorcycle = new_type_motorcycle;
    }

    // Getter and Setter for tank capacity
    int get_tank_capacity()
    {
        return tank_capacity;
    }

    void set_tank_capacity(int new_tank_capacity)
    {
        tank_capacity = new_tank_capacity;
    }
};