# Set atau himpunan merupakan salah satu tipe data selain list dan tuple yang ada di python
# Karakteristik himpunan, yakni tidak punya urutan, misalnya ada satu himpunan memiliki dua nama yang sama dianggap satu data
# Ada dua cara membuat himpunan

# Cara Pertama
superhero = {"iron man", "captain amerika", "spiderman", "thor", "hulk"}

superhero.add("falcon")  # datanya tidak memilki urutan
superhero.add("thor")  # data yang memiliki nama yang sama di anggap satu

print(superhero)

# Cara Kedua
makanan = set()

makanan.add("Nasi Goreng")
makanan.add("Pecel Lele")
makanan.add("Gurame Bakar")
makanan.add(212)

# print(sorted(makanan))  # sorted untuk mengurutkan
# print(superhero[2]) ini akan error karena set tidak support indexing karena tidak ada urutan pastinya
print(makanan)

# Kesimpulan set dia tipe datanya tidak tergantung pada urutannya dan tidak tergantung pada frekuensi data
# Misalkan kita punya buku. Terus mau kita masukin ke python. Tapi dengan judul yang sama dia akan dianggap sama datanya jadinya tidak bergantung. Misalkan di satu array ada dua buku, kalo pake set ini akan memudahkan bila terdapat data yang sama


# Karena ini himpunan, ada beberapa yang bisa kita gunakan.
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7}

# Mencari gabungan antara ganjil dan genap
print(ganjil.union(genap))

# Mencari irisan antara ganjil dan genap
print(ganjil.intersection(genap))
print(ganjil.intersection(prima))
