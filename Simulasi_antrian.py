import Module.Queue as q
import Module.Controller as cont

# Data Tester
# data_pasien = {"fauzan":{"kategori":"sedang","waktu":50, "fasilitas":""},"fatin":{"kategori":"sedang","waktu":20, "fasilitas":""},"agung":{"kategori":"ringan","waktu":30, "fasilitas":""},"aini":{"kategori":"ringan","waktu":20, "fasilitas":""}}
# for namaPasien in data.keys():
#     print(data[namaPasien]['kategori'])

# Declare Variable
data_pasien = {}
antrian_umum = q.createQueue()
antrian_darurat = q.createQueue()

# Insert Data Pasien
jumlah_pasien = int(input("Jumlah pasien yang terdata: "))
data_pasien = cont.insert(jumlah_pasien)


# List Queue
for namaPasien in data_pasien.keys():
    if cont.listQueue(namaPasien, data_pasien) == "umum":
        q.enqueue(antrian_umum,namaPasien)
    else:
        q.enqueue(antrian_darurat,namaPasien)

# Show Data Pasien
cont.show_data(data_pasien)

# Use Fasilitas
# Fasilitas Umum
if not q.isEmpty(antrian_umum):
    cont.use_fasilitas(antrian_umum, data_pasien, "Umum")
else:
    print("Antrian Umum Kosong")
# Fasilitas Darurat
if not q.isEmpty(antrian_darurat):
    cont.use_fasilitas(antrian_darurat, data_pasien, "Darurat")
else:
    print("Antrian Darurat Kosong")