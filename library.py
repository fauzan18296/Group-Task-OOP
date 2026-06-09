import os
class Buku:
          def __init__(self, judul: list[str], penulis: list[str], tahun: list[int]):
                    self.judul = judul
                    self.penulis = penulis
                    self.tahun = tahun

          def opsi_buku(self):
                    while True:
                              print("Pilih jenis buku:")
                              print("1. Buku Pelajaran")
                              print("2. Novel")
                              print("3. Majalah")
                              print("4. Keluar")
                              
                              book_option = input("Masukkan jenis buku yang ingin ditambahkan (1-4): ")
                              
                              if book_option == "1":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        buku_pelajaran.opsi_user_action()
                              elif book_option == "2":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        novel.opsi_user_action()
                              elif book_option == "3":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        majalah.opsi_user_action()
                              elif book_option == "4":
                                        print("Keluar dari program.")
                                        break
                              else:
                                        print("Opsi tidak valid. Silakan coba lagi.")
                                        return self.opsi_buku()
                              

          def tampil_info(self):
                    return f"{self.judul} oleh {self.penulis} ({self.tahun})"


class BukuPelajaran(Buku):
          def __init__(self, judul: list[str], penulis: list[str], tahun: list[int], mata_pelajaran: list[str]):
                    super().__init__(judul, penulis, tahun)
                    self.mata_pelajaran = mata_pelajaran
          
          def opsi_user_action(self):
                    while True:
                              print("\nAnda berada di jenis Buku Pelajaran.")
                              print("Opsi aksi yang tersedia:")
                              print("1. Tambahkan Buku")
                              print("2. Tampilkan Informasi Buku")
                              print("3. Hapus Buku")
                              print("4. Keluar")
                    
                              user_action = input("Masukkan aksi yang ingin dilakukan (1-4): ")
                              if user_action == "1":
                                        judul = input("Masukkan judul buku: ")
                                        penulis = input("Masukkan penulis buku: ")
                                        tahun = int(input("Masukkan tahun terbit buku: "))
                                        mata_pelajaran = input("Masukkan mata pelajaran buku: ")
                                        self.tambah_buku(judul, penulis, tahun, mata_pelajaran)
                                        print("Buku berhasil ditambahkan.")
                              elif user_action == "2":
                                        self.tampil_info()
                              elif user_action == "3":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        self.tampil_info()
                                        try:
                                                  user_delete_book = int(input("Masukkan nomor buku yang ingin dihapus: ")) - 1  # Mengurangi 1 untuk mendapatkan indeks yang benar
                                                  self.hapus_buku(user_delete_book)
                                        except ValueError:
                                                  print("Input tidak valid. Silakan masukkan nomor buku yang benar.")
                              elif user_action == "4":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Kembali ke menu utama.")
                                        break
                              else:
                                        print("Opsi tidak valid. Silakan coba lagi.")
                                        return self.opsi_user_action()
          def tambah_buku(self, judul: str, penulis: str, tahun: int, mata_pelajaran: str):
                    self.judul.append(judul)
                    self.penulis.append(penulis)
                    self.tahun.append(tahun)
                    self.mata_pelajaran.append(mata_pelajaran)
          def hapus_buku(self, index: int):
                    if 0 <= index < len(self.judul):
                              self.judul.pop(index)
                              self.penulis.pop(index)
                              self.tahun.pop(index)
                              self.mata_pelajaran.pop(index)
                              self.tampil_info()
                              print("Buku berhasil dihapus.")
                    else:
                              print("Indeks tidak valid. Tidak ada buku yang dihapus.")
          def tampil_info(self):
                    print("="*20,"Informasi Buku Pelajaran", "="*20)
                    for index, judul in enumerate(self.judul, start=0):
                              print(f"{index + 1}. {judul} oleh {self.penulis[index]} ({self.tahun[index]}) - Mata Pelajaran: {self.mata_pelajaran[index]}")
                    print("="*57)

class Novel(Buku):
          def __init__(self, judul: list[str], penulis: list[str], tahun: list[int], genre: list[str]):
                    super().__init__(judul, penulis, tahun)
                    self.genre = genre
                    
          def opsi_user_action(self):
                    while True:
                              print("\nAnda berada di jenis Buku Novel.")
                              print("Opsi aksi yang tersedia:")
                              print("1. Tambahkan Novel")
                              print("2. Tampilkan Informasi Novel")
                              print("3. Hapus Novel")
                              print("4. Keluar")
                    
                              user_action = input("Masukkan aksi yang ingin dilakukan (1-4): ")
                              if user_action == "1":
                                        judul = input("Masukkan judul novel: ")
                                        penulis = input("Masukkan penulis novel: ")
                                        tahun = int(input("Masukkan tahun terbit novel: "))
                                        genre = input("Masukkan genre novel: ")
                                        self.tambah_novel(judul, penulis, tahun, genre)
                                        print("Novel berhasil ditambahkan.")
                              elif user_action == "2":
                                        self.tampil_info()
                              elif user_action == "3":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        try:
                                                  user_delete_book = int(input("Masukkan nomor novel yang ingin dihapus: ")) - 1  # Mengurangi 1 untuk mendapatkan indeks yang benar
                                                  self.hapus_buku(user_delete_book)
                                        except ValueError:
                                                  print("Input tidak valid. Silakan masukkan nomor novel yang benar.")
                              elif user_action == "4":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Kembali ke menu utama.")
                                        break
                              else:
                                        print("Opsi tidak valid. Silakan coba lagi.")
                                        return self.opsi_user_action()
          def tambah_novel(self, judul: str, penulis: str, tahun: int, genre: str):
                    self.judul.append(judul)
                    self.penulis.append(penulis)
                    self.tahun.append(tahun)
                    self.genre.append(genre)
                    
          def hapus_buku(self, index: int):
                    if 0 <= index < len(self.judul):
                              self.judul.pop(index)
                              self.penulis.pop(index)
                              self.tahun.pop(index)
                              self.genre.pop(index)
                              self.tampil_info()
                              print("Buku berhasil dihapus.")
                    else:
                              print("Indeks tidak valid. Tidak ada buku yang dihapus.")
          
          def tampil_info(self):
                    print("="*20,"Informasi Novel", "="*20)
                    for index, judul in enumerate(self.judul, start=0):
                              print(f"{index + 1}. {judul} oleh {self.penulis[index]} ({self.tahun[index]}) - Genre: {self.genre[index]}")
                    print("="*57)

class Majalah(Buku):
          def __init__(self, judul: list[str], penulis: list[str], tahun: list[int], edisi: list[str]):
                    super().__init__(judul, penulis, tahun)
                    self.edisi = edisi
                    
          def opsi_user_action(self):
                    while True:
                              print("\nAnda berada di jenis Buku Majalah.")
                              print("Opsi aksi yang tersedia:")
                              print("1. Tambahkan Majalah")
                              print("2. Tampilkan Informasi Majalah")
                              print("3. Hapus Majalah")
                              print("4. Keluar")
                    
                              user_action = input("Masukkan aksi yang ingin dilakukan (1-4): ")
                              if user_action == "1":
                                        judul = input("Masukkan judul majalah: ")
                                        penulis = input("Masukkan penulis majalah: ")
                                        tahun = int(input("Masukkan tahun terbit majalah: "))
                                        edisi = input("Masukkan edisi majalah: ")
                                        self.tambah_majalah(judul, penulis, tahun, edisi)
                                        print("Majalah berhasil ditambahkan.")
                              elif user_action == "2":
                                        self.tampil_info()
                              elif user_action == "3":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        try:
                                                  user_delete_magazine = int(input("Masukkan nomor majalah yang ingin dihapus: ")) - 1
                                                  self.hapus_buku(user_delete_magazine)
                                        except ValueError:
                                                  print("Input tidak valid. Silakan masukkan nomor majalah yang benar.")
                              elif user_action == "4":
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        print("Kembali ke menu utama.")
                                        break
                              else:
                                        print("Opsi tidak valid. Silakan coba lagi.")
                                        return self.opsi_user_action()
          def tambah_majalah(self, judul: str, penulis: str, tahun: int, edisi: str):
                    self.judul.append(judul)
                    self.penulis.append(penulis)
                    self.tahun.append(tahun)
                    self.edisi.append(edisi)
          
          def hapus_buku(self, index: int):
                    if 0 <= index < len(self.judul):
                              self.judul.pop(index)
                              self.penulis.pop(index)
                              self.tahun.pop(index)
                              self.edisi.pop(index)
                              self.tampil_info()
                              print("Buku berhasil dihapus.")
                    else:
                              print("Indeks tidak valid. Tidak ada buku yang dihapus.")
          
          def tampil_info(self):
                    print("="*20,"Informasi Majalah", "="*20)
                    for index, judul in enumerate(self.judul, start=0):
                              print(f"{index + 1}. {judul} oleh {self.penulis[index]} ({self.tahun[index]}) - Edisi: {self.edisi[index]}")
                    print("="*57)


buku_pelajaran = BukuPelajaran(judul=[], penulis=[], tahun=[], mata_pelajaran=[])
novel = Novel(judul=[], penulis=[], tahun=[], genre=[])
majalah = Majalah(judul=[], penulis=[], tahun=[], edisi=[])

buku = Buku(judul=[], penulis=[], tahun=[])
buku.opsi_buku()

buku_pelajaran.tampil_info()
novel.tampil_info()
majalah.tampil_info()