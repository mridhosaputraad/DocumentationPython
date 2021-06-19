# if Kalo di python
# if statement:
#     statement:

nilai = 75

if nilai == 75:  # equal eksplisit
    print("nilai anda:", nilai)


# misalkan ( nesting if artinya if didalam if )
nilai1 = 80
nilai2 = 85

if nilai1 == 80:
    print("nilai anda:", nilai1)
    print("step 1")
    if nilai2 == 85:  # ini namanya nesting if
        print("nilai anda:", nilai2)
        print("step 2")


# Kasus lain if variabel is/is not data ( is artinya sama dengan, is not tidak sama dengan (natural language) )
# akan error di 3.8 ke atas. solusinya gunakan "==" & "!="
nilai4 = 55
if nilai4 == 60:  # equal
    print("nilai anda:", nilai4)

if nilai4 != 60:  # not equal
    print("nilai anda:", nilai4)

print(10*"=")

# Topik elif
# Apa yang elif lakukan dia memberi syarat tambahan
nilai5 = 65

if 80 <= nilai5 <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai5 < 80:
    print("nilai anda adalah B")
elif 60 <= nilai5 < 70:
    print("nilai anda adalah C")
elif 50 <= nilai5 < 60:
    print("nilai anda adalah T, lakukan perbaikan!")
else:
    print("maaf anda tidak lulus mata kuliah ini")
# Lebih mudahnya bisa meggunakan switch case

print(50*"=")


# Kasus: operator logika untuk list dan string
gorengan = ["bakwan", "cireng", "bala-bala", "gehu",
            "combro", "pisang goreng", "pukis", "risoles"]
beli = "bandros"

# standarnya akan melakukan loppping variabel satu persatu. tapi cukup dengan:
if beli in gorengan:
    print('Mamang bilang, " ya saya jual', beli, '"')

if not beli in gorengan:
    print('"Saya gak jual', beli, '"')

# FYI: is dan in ini kita bisa gunakan untuk mengecek stringnya
# if 'n' in beli:
#     print("ada n")

karakter = "z"
if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada", karakter, "di", beli)
