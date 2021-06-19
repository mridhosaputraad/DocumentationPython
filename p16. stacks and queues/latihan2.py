# FYI :  Di python, build in-nya tidak ada untuk menggunakan antrian tapi ada yang namanya modul. simplenya kita mengimpor dari source code punya orang lain

# > Mensimulasikan queue (antrian) FIFO
from collections import deque   # ini adalah library pengganti fungsi build in

antrian = deque([1, 2, 3, 4, 5])
# Fungsinya kita bisa menambah dan mengurangi data di depan
print('data sekarang: ', antrian)

# Menambahkan data
antrian.append(6)
print('data masuk: ', 6)
print('data sekarang: ', antrian)

antrian.append(7)
print('data masuk: ', 7)
print('data sekarang: ', antrian)

# Mengurangi antrian
out = antrian.popleft()
print('data keluar: ', out)
print('data sekarang: ', antrian)

out = antrian.popleft()
print('data keluar: ', out)
print('data sekarang: ', antrian)

out = antrian.popleft()
print('data keluar: ', out)
print('data sekarang: ', antrian)

antrian.append(8)
print('data masuk: ', 8)
print('data sekarang: ', antrian)
