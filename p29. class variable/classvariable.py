class mahasiswa():

    jumlah_mahasiswa = 0
    jurusan = "pendidikan ekonomi"

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1


otong = mahasiswa("otong surotong", 12345671)
ucup = mahasiswa("michael ucup", 12345670)

otong.jurusan = "ekonomi makro"
otong.kegemaran = "menari"

print(otong.jurusan)
print(otong.kegemaran)
print(mahasiswa.jumlah_mahasiswa)

# FYI
# Sesuatu yang ada 'self' itu milik instansiasi, dan sebaliknya bila tidak ada itu milik class
