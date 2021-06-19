# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah', total)
    return total    # berfungsi untuk menngeluarkan nilai dari function


# Cara 1
a = kuadrat(3)
print(a)

# Cara 2
print(kuadrat(4))
print(50*'=')


# fungsi dengan return value dan multiple argument
def tambah(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1, '+', argumen2, '=', total)
    return total


def kali(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, 'x', argumen2, '=', total)
    return total


# Cara 1
a = tambah(3, 4)
b = kali(3, a)

# Cara 2
c = kali(3, tambah(3, 4))
print(c)


# Return value kita bisa gunakan ketika ingin mengakses nilai dari sesuatu misalnya perhitungan dan lainnya
