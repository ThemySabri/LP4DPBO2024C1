class ParkingLot:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__current_count = 0

    def park_vehicle(self):
        if self.__current_count < self.__capacity:
            self.__current_count += 1
            print("Vehicle parked successfully.")
        else:
            print("Parking lot is full.")

    def vacate_spot(self):
        if self.__current_count > 0:
            self.__current_count -= 1
            print("Spot vacated.")
        else:
            print("No vehicles parked.")

    def get_current_count(self):
        return self.__current_count

    def get_capacity(self):
        return self.__capacity
