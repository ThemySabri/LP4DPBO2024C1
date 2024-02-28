'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''

from Vehicle import Vehicle  # Mengimpor kelas Vehicle untuk dijadikan superclass


class Motorcycle(Vehicle):  # Mendefinisikan kelas Motorcycle yang merupakan subkelas dari Vehicle
    def __init__(self, license_plate, brand, year, color, type_motorcycle, tank_capacity):
        # Memanggil konstruktor kelas induk (Vehicle) dengan menggunakan super()
        super().__init__(license_plate, brand, year, color)
        # Inisialisasi atribut kelas Motorcycle
        # Tipe sepeda motor (misalnya, sport, cruiser, dll.)
        self.__type_motorcycle = type_motorcycle
        # Kapasitas tangki bahan bakar sepeda motor
        self.__tank_capacity = tank_capacity

    # Metode getter dan setter untuk tipe sepeda motor
    def get_type_motorcycle(self):
        return self.__type_motorcycle

    def set_type_motorcycle(self, type_motorcycle):
        self.__type_motorcycle = type_motorcycle

    # Metode getter dan setter untuk kapasitas tangki bahan bakar sepeda motor
    def get_tank_capacity(self):
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity):
        self.__tank_capacity = tank_capacity
