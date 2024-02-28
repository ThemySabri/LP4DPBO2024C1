'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''


class Garage:
    def __init__(self, name, area):
        # Inisialisasi objek garasi dengan nama dan luas area yang diberikan
        self.__name = name    # Nama garasi
        self.__area = area    # Luas area garasi
        self.__vehicles = []  # Daftar kendaraan yang tersimpan di garasi

    # Metode untuk menambahkan kendaraan ke dalam garasi
    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    # Metode untuk mendapatkan daftar kendaraan yang tersimpan di garasi
    def get_vehicles(self):
        return self.__vehicles

    # Metode getter untuk nama garasi
    def get_name(self):
        return self.__name

    # Metode setter untuk nama garasi
    def set_name(self, name):
        self.__name = name

    # Metode getter untuk luas area garasi
    def get_area(self):
        return self.__area

    # Metode setter untuk luas area garasi
    def set_area(self, area):
        self.__area = area
