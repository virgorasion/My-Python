#Created By M Nur Fauzan W | 190411100064
def paksalim(nama,gaji,menikah,rumah):
	print("Syarat-syarat yang harus dilakukan pak "+str(nama)+" adalah :")
	if gaji >= 3000000:
		print("Wajib Mengikuti Asuransi (Syarat 1)")
	else:
		print("Tidak Wajib Mengikuti Asuransi (Syarat 1)")
	if menikah == "ya":
		print("Anda Sudah Boleh Menabung (Syarat 2)")
	else:
		print("Anda Belum Boleh Menabung (Syarat 2)")
	if rumah == "ya":
		print("Anda Wajib Membayar PBB (Syarat 3)")
	else:
		print("Anda Tidak Perlu Membayar PBB (Syarat 3)")

nama = input("Masukkan Nama Anda :")
gaji = int(input("Masukkan Slip Gaji Anda :"))
menikah = input("Apakah Anda Sudah Menikah ? ya/tidak")
rumah = input("Apakah Anda Sudah Memiliki Rumah ? ya/tidak")

paksalim(nama,gaji,menikah,rumah)
