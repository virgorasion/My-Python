#Created By M Nur Fauzan W | 190411100064
def pembulatan(nilai):
	if nilai >= 40:
		if nilai % 5 >= 3:
			plus = 5 - nilai % 5
			hasil = nilai + plus
			print("Hasil Pembulatan :",hasil)
		else:
			minus = nilai % 5
			hasil = nilai - minus
			print("Hasil Pembulatan :",hasil)
	else:
		print("Hasil Pembulatan :",nilai)
		

angka = int(input("Masukkan Angka : "))
pembulatan(angka)