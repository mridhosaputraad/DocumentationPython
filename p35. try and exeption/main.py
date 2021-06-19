# Error Handling : Try and Exeption
# Ada 2 tipe error, yang pertama error yang bisa di deteksi oleh compiler. Yang kedua runtime error.

print("ini adalah program pembagian")

while True:
    try:
        penyebut = int(input("masukkan angka penyebut: "))
        pembilang = int(input("masukkan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    # Cara paling umum (Bagus untuk debugging)
    # except Exception as err:
    #     print(err)
    except ValueError:
        print("yang anda masukan buka angka")
    except ZeroDivisionError:
        print("angka pembilang yang anda masukkan adalah nol, pilih yang lain")

"""
    type of exception errors:
    1. IOError                  -> untuk input output bila ada corrupted file
    2. ImportError              -> untuk mengecek apakah ada modul
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. EOFError


"""

print("berhasil, hasil pembagian adalah: ", hasil)
