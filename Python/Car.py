'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''

from Vehicle import Vehicle  # Mengimpor kelas Vehicle untuk dijadikan superclass


class Car(Vehicle):  # Mendefinisikan kelas Car yang merupakan subkelas dari Vehicle
    def __init__(self, license_plate, brand, year, color, num_seats, num_doors):
        # Memanggil konstruktor kelas induk (Vehicle) dengan menggunakan super()
        super().__init__(license_plate, brand, year, color)
        # Inisialisasi atribut kelas Car
        self.__num_seats = num_seats  # Jumlah kursi dalam mobil
        self.__num_doors = num_doors  # Jumlah pintu mobil

    # Metode getter dan setter untuk jumlah kursi dalam mobil
    def get_num_seats(self):
        return self.__num_seats

    def set_num_seats(self, num_seats):
        self.__num_seats = num_seats

    # Metode getter dan setter untuk jumlah pintu mobil
    def get_num_doors(self):
        return self.__num_doors

    def set_num_doors(self, num_doors):
        self.__num_doors = num_doors
