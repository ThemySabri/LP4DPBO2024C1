#pragma once

#include <iostream>
#include <string>
#include <vector>
#include "Vehicle.cpp"

using namespace std;

class Garage
{
private:
    std::string name;
    double area;
    std::vector<Vehicle *> vehicles;

public:
    // Constructor
    Garage(std::string name, double area)
        : name(name), area(area) {}

    // Method to add a vehicle to the garage
    void add_vehicle(Vehicle *vehicle)
    {
        vehicles.push_back(vehicle);
    }

    // Method to get the list of vehicles in the garage
    std::vector<Vehicle *> get_vehicles()
    {
        return vehicles;
    }

    // Getter for garage name
    std::string get_name()
    {
        return name;
    }

    // Setter for garage name
    void set_name(std::string new_name)
    {
        name = new_name;
    }

    // Getter for garage area
    double get_area()
    {
        return area;
    }

    // Setter for garage area
    void set_area(double new_area)
    {
        area = new_area;
    }
};