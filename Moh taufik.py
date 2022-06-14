print('=====================')
print('Operasi Matematika')
print('jumlah  [+]')
print('kurang  [-]')
print('kali    [*]')
print('Bagi    [/]')
print('=====================')


operasi = input('pilih (1|2|3|4|)')
bilangan_1= eval(input('masukkan Bilangan Pertama:'))
bilangan_2= eval(input('masukkan bilangan Kedua:'))


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
  
class jawaban:
        def __init__(self, jawaban):
             self. jawaban = jawaban
             
class jawaban:
       pass
       ('jawaban Ini Benar')
 
print('jawaban Ini Benar')