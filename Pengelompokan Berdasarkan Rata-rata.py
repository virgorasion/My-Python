#Created By M Nur Fauzan W | 190411100064
TA = int(input("Masukkan Nilai Tes Akademik : "))
TK = int(input("Masukkan Nilai Tes Keterampilan : "))
TP = int(input("Masukkan Nilai Tes Psikologi"))
avg = (TA+TK+TP)/3
print(float(avg))

if avg > 75:
	if TP < TA > TK:
		print("Bagian Administrasi")
	elif TA < TK > TP:
		print("Bagian Produksi")
	else:
		print("Bagian Pemasaran")
else:
	print("Anda Tidak LULUS")
	