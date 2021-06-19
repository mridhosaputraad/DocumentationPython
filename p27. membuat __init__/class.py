# Class
class mahasiswa():

    def __init__(self, nama_pegawai, NIM):
        self.cnama = nama_pegawai
        self.cNIM = NIM

    def nilai(self, nilai_mahasiswa):
        if nilai_mahasiswa > 50:
            print('Kamu Anak Pintar')
        else:
            print('Kamu Terlihat Bodoh')


cmahasiswa = mahasiswa('Udinese', '1234567')

print(cmahasiswa.cnama, cmahasiswa.cNIM)

cmahasiswa.nilai(100)


# Catatan
# Init berfungsi ketika memasukkan attribut langsung dirubah saat menginstasiasi class
# Init akan di jalankan saat menginisialisasi objek
