#Created By M Nur Fauzan W | 190411100064
TA = int(input("Masukkan Nilai Tes Akademik : "))
TK = int(input("Masukkan Nilai Tes Keterampilan : "))
TP = int(input("Masukkan Nilai Tes Psikologi"))
avg = (TA+TK+TP)/3
print(float(avg))

if avg > 75:
	if TA > TK and TA > TP:
		print("Bagian Administrasi")
	elif TK > TA and TK > TP:
		print("Bagian Produksi")
	else:
		print("Bagian Pemasaran")
else:
	print("Anda Tidak LULUS")
	