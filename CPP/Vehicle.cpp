#pragma once

#include <iostream>
#include <string>

using namespace std;

class Vehicle
{
private:
    std::string license_plate;
    std::string brand;
    int year;
    std::string color;

public:
    // Constructor
    Vehicle(std::string license_plate, std::string brand, int year, std::string color)
        : license_plate(license_plate), brand(brand), year(year), color(color) {}

    // Getter and Setter for license plate
    std::string get_license_plate()
    {
        return license_plate;
    }

    void set_license_plate(std::string new_license_plate)
    {
        license_plate = new_license_plate;
    }

    // Getter and Setter for brand
    std::string get_brand()
    {
        return brand;
    }

    void set_brand(std::string new_brand)
    {
        brand = new_brand;
    }

    // Getter and Setter for year
    int get_year()
    {
        return year;
    }

    void set_year(int new_year)
    {
        year = new_year;
    }

    // Getter and Setter for color
    std::string get_color()
    {
        return color;
    }

    void set_color(std::string new_color)
    {
        color = new_color;
    }
};