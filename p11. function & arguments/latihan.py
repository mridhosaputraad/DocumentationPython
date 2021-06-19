# fungsi dengan menggunakan argumen sederhana
def siswa(nama):    # input nama ini kita sebut arguments
    print('siswa ini bernama', nama)


siswa('mario')
print(50*'=')


# fungsi dengan menggunakan keywords arguments
def guru(nama, pelajaran):
    print('guru ini bernama:', nama)
    print('mengajar:', pelajaran)


guru(nama='popong', pelajaran='seni rupa')
guru(pelajaran='olah raga', nama='endang')
# guru('olah raga', 'raihan') ini tidak error, tetapi urutannya menjadi tidak sesuai
# ini adalah keywords, artinya akan mengakses variabel nama
print(50*'=')


# fungsi dengan menggunakan default arguments
def penjagaSekolah(nama, shift='siang', galak='tidak'):
    print('penjaga sekolah ini bernama:', nama)
    print('shiftnya:', shift)
    print('galak?', galak)


penjagaSekolah('entis')
penjagaSekolah('maman', shift='malam')
penjagaSekolah('asep', galak='sangat')
# penjagaSekolah(shift='malam', galak='iya') ini akan error, karena arguments nama kosong
