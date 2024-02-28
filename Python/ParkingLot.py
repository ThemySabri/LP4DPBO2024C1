class ParkingLot:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__current_count = 0

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_current_count(self):
        return self.__current_count

    def park_vehicle(self):
        if self.__current_count < self.__capacity:
            self.__current_count += 1
            print("Vehicle parked successfully.")
        else:
            print("Parking lot is full.")
