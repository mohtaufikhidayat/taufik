#Moh Taufik Hidayat
print('Operasi Matematika')
print('1. Penjumlah ')
print('2. Pengurang ' )
print('3. Perkalian ')
print('4. Pembagian ' )


operasi = input('Pilih operasi (1|2|3|4): ')
bilangan_1 = eval(input('Masukkan bilangan pertama: '))
bilangan_2 = eval(input('Masukkan bilangan kedua: '))

if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
  print('Tidak valid')