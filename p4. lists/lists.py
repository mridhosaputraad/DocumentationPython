# Lists itu sama seperti array
Data = [1, 4, 9, 16, 25, 36, 49, 64]

# Subdata = Data[0]
# Subdata = Data[-3] maka dia akan menghitung dari belakang

# Mengakses lists
Subdata1 = Data[3]
Subdata2 = Data[-3]

# Memotong lists
Subdata3 = Data[2:4]  # bisa juga
Subdata4 = Data[-2:]
# Subdata4 = Data[:4]

Data2 = [100, 200, 300, 400, 500, 600, 700, 800]

# Menambah lists
Data3 = Data + Data2

# Merubah content dari list
# print(Data)
# Data[4] = 87
# print(Data)

# Misal kasus
# 3. Cara mengatasinya menambahkan ':' artinya akan mengakses semua komponen data. pada saat dipanggil a data baru berubah
a = Data[:]
a[4] = 87
# print(a)  # 1. ini akan merubah, tapi
# print(Data)  # 2. a tadi ditimpa ke data

# merubah content list dengan menggunakan metode slicing
Data[3:5] = [11, 12]

# Lists dalam list
x = [Data, Data2]

# Mengakses list dalam multidimensional list
y = x[0][3]
# print(x)
# print(y)

# Methods untuk list
Data.append(30)
# print(Data) dia akan menambah object baru

# Function yang bisa kita gunakan kepada list
panjang_list = len(Data)
print(panjang_list)
