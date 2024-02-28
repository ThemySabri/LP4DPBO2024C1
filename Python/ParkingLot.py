'''Bismillah
Saya Themy Sabri Syuhada dengan NIM 2203903. 
Demi keberkahan-Nya, saya berjanji mengerjakan 
latihan praktikum 4 DPBO dengan jujur 
dan tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin.'''


class ParkingLot:
    def __init__(self, capacity):
        # Inisialisasi objek tempat parkir dengan kapasitas dan hitungan saat ini
        self.__capacity = capacity      # Kapasitas total tempat parkir
        self.__current_count = 0         # Hitungan saat ini jumlah kendaraan yang terparkir

    # Metode untuk memarkir kendaraan
    def park_vehicle(self):
        if self.__current_count < self.__capacity:  # Jika masih ada tempat kosong
            self.__current_count += 1              # Tambahkan hitungan kendaraan terparkir
            # Tampilkan pesan berhasil parkir
            print("Vehicle parked successfully.")
        else:
            # Jika tempat parkir penuh, tampilkan pesan
            print("Parking lot is full.")

    # Metode untuk mengosongkan tempat parkir
    def vacate_spot(self):
        if self.__current_count > 0:               # Jika ada kendaraan yang terparkir
            self.__current_count -= 1              # Kurangi hitungan kendaraan terparkir
            # Tampilkan pesan tempat parkir kosong
            print("Spot vacated.")
        else:
            # Jika tidak ada kendaraan yang terparkir, tampilkan pesan
            print("No vehicles parked.")

    # Metode getter untuk mendapatkan jumlah kendaraan yang terparkir saat ini
    def get_current_count(self):
        return self.__current_count

    # Metode getter untuk mendapatkan kapasitas total tempat parkir
    def get_capacity(self):
        return self.__capacity
