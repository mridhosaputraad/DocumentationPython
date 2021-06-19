# Rekap
list = [1, 2, 3, 4]
tuple = (1, 2, 3, 4)
set = {1, 2, 3, 4}

print(type(list))
print(type(tuple))
print(type(set))
print(50*'=')


# Dictionary adalah sebuah struktur data assosiatif atau menggunakan mapping
# Cara membuat dictionary
# member1 = {key: value, key: value}

member1 = {"ID": 101, "Nama": "Ridho",
           "Pekerjaan": "Mahasiswa", "Status member": "Gold"}

member2 = {"ID": 101, "Nama": "Dendu",
           "Pekerjaan": "Mahasiswa", "Status member": "Master"}

memberlist = {101: member1, 102: member2}

print(memberlist[101])

# Cara mengakses data di dictionary
# print(member1["Pekerjaan"])
# print(member1.keys())  # jika ingin melihat key -nya saja
# print(member1.values())  # jika ingin melihat value -nya saja
# print(member1.items())


# Kesimpulannya jadi kita bisa memasukkan dictionary ini di dalam sebuah list. Jadi kita bisa membuat sebuah data ini menjadi database yang bisa kita akses di selanjutnya
