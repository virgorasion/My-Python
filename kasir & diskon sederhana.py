#Created By M Nur Fauzan W | 190411100064
baju = 100000
celana = 150000
sepatu = 250000

barang = input("Ingin membeli apa (baju/celana/sepatu) ? ")
card = input("Apakah mempunyai kartu member ? (ya/tidak) ")

if barang == "baju":
	if card == "ya":
		disc = baju * 20 / 100
		result = baju - disc
		print("Harga Baju :",result)
	else:
		result = baju
		print("Harga Baju :",result)
elif barang == "celana":
	if card == "ya":
		disc = celana * 20 / 100
		result = celana - disc
		print("Harga Celana :",result)
	else:
		result = celana
		print("Harga Celana :",result)
elif barang == "sepatu":
	if card == "ya":
		disc = sepatu * 20 / 100
		result = sepatu - disc
		print("Harga Sepatu :",result)
	else:
		result = sepatu
		print("Harga Sepatu :",result)
else:
	print("Barang dagangan tidak tersedia")
