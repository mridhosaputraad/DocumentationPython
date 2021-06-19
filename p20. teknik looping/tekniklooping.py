# Teknik Looping
nama_band = ['Payung Teduh',
             'Fourtwenty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena']

kumpulan_lagu = ['Akad',
                 'Zona Nyaman',
                 'Rumahku',
                 'Sang Filsuf',
                 'Sindori']

# Cara mudahnya
# iterasi = 0
# for band in nama_band:
#     print('no', iterasi, 'namaband', band)
#     iterasi += 1


# enumerate, akan mereturn indeksnya dan nilainya
for i, band in enumerate(nama_band, start=1):
    print(i, ':', band)

# zip, menggabungkan dua list (korespondensinya harus satu-satu dan linier)
for band, lagu in zip(nama_band, kumpulan_lagu):
    print(band, 'menyanyikan lagu yang berjudul:', lagu)


# Kasus pada set
playlist = {'baby baby',
            'ada apa dengan cinta',
            'cenat-cenut',
            'jaran goyang',
            'louder',
            'roki',
            'daydream',
            'shiranai'}

for lagu in sorted(playlist):
    print(lagu)


print(100*'=')
# Dictionary (keyword, value)
playlist2 = {'Roselia': 'Louder',
             'Afterglow': 'Roki',
             'Poppin Party': 'Initial'
             }

for i, v in playlist2.items():
    print(i, 'lagunya:', v)


# Dan masih banyak lagi
for i in reversed(range(1, 10, 1)):
    print(i)
