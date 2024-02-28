'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''


class Vehicle:
    def __init__(self, license_plate, brand, year, color):
        # Inisialisasi objek kendaraan dengan atribut yang diberikan
        self.__license_plate = license_plate  # Nomor plat kendaraan
        self.__brand = brand                  # Merek kendaraan
        self.__year = year                    # Tahun pembuatan kendaraan
        self.__color = color                  # Warna kendaraan

    # Metode getter dan setter untuk nomor plat kendaraan
    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate

    # Metode getter dan setter untuk merek kendaraan
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    # Metode getter dan setter untuk tahun pembuatan kendaraan
    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    # Metode getter dan setter untuk warna kendaraan
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
