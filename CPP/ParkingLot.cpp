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

using namespace std;

class ParkingLot
{
private:
    int capacity;
    int current_count;

public:
    // Constructor
    ParkingLot(int capacity)
        : capacity(capacity), current_count(0) {}

    // Method to park a vehicle
    void park_vehicle()
    {
        if (current_count < capacity)
        {                    // If there is still space available
            current_count++; // Increment the count of parked vehicles
            // Print a message indicating successful parking
            std::cout << "Vehicle parked successfully." << std::endl;
        }
        else
        {
            // If the parking lot is full, print a message
            std::cout << "Parking lot is full." << std::endl;
        }
    }

    // Method to vacate a parking spot
    void vacate_spot()
    {
        if (current_count > 0)
        {                    // If there are vehicles parked
            current_count--; // Decrement the count of parked vehicles
            // Print a message indicating spot vacated
            std::cout << "Spot vacated." << std::endl;
        }
        else
        {
            // If there are no vehicles parked, print a message
            std::cout << "No vehicles parked." << std::endl;
        }
    }

    // Getter for the current count of parked vehicles
    int get_current_count()
    {
        return current_count;
    }

    // Getter for the total capacity of the parking lot
    int get_capacity()
    {
        return capacity;
    }
};