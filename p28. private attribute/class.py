class mahasiswa():

    jurusan = "Pendidikan Ekonomi"
    __nilai = 0  # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama  # public
        self.nim = input_nim

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama, 'lulus')


otong = mahasiswa("otong surotong", 12345567)

otong.uts(10)
otong.uas(50)

otong.check_status()
