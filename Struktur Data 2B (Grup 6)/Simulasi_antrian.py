import Module.Queue as q
import Module.Controller as cont

# Data Tester
data_pasien = {
    "Helmi Lestari Ning Tyas":
        {
            "NIM": 190411100034,
            "kategori": "sedang",
            "waktu": 50,
            "fasilitas": ""
        },
    "Mas Agung Muhammad I. U.":
        {
            "NIM": 190411100039,
            "kategori": "sedang",
            "waktu": 20,
            "fasilitas": ""
        },
    "Sandi Prayogo":
        {
            "NIM": 190411100053,
            "kategori": "ringan",
            "waktu": 30,
            "fasilitas": ""
        },
    "Abd Muin":
        {
            "NIM": 190411100055,
            "kategori": "ringan",
            "waktu": 40,
            "fasilitas": ""
        },
    "M. Nur Fauzan W.":
        {
            "NIM": 190411100064,
            "kategori": "berat",
            "waktu": 60,
            "fasilitas": ""
        },
    "Prasetyo Adi Pratama N.":
        {
            "NIM": 190411100072,
            "kategori": "berat",
            "waktu": 30,
            "fasilitas": ""
        },
    "Achmad Farid Alfa Waid":
        {
            "NIM": 190411100073,
            "kategori": "berat",
            "waktu": 50,
            "fasilitas": ""
        },
    "Siti Sofiyatul F.":
        {
            "NIM": 190411100074,
            "kategori": "sedang",
            "waktu": 100,
            "fasilitas": ""
        },
    "Maghfirutul Jannah":
        {
            "NIM": 190411100079,
            "kategori": "ringan",
            "waktu": 80,
            "fasilitas": ""
        },
    "Anggi Nor Fauziah":
        {
            "NIM": 190411100093,
            "kategori": "berat",
            "waktu": 120,
            "fasilitas": ""
        },
}

# *Attention*
# To make dinamis data comment the Data Tester in above
# then uncomment data pasien and Insert data pasien in bottom

# Declare Variable
# data_pasien = {}
antrian_umum = q.createQueue()
antrian_darurat = q.createQueue()

# Insert Data Pasien
# jumlah_pasien = int(input("Jumlah pasien yang terdata: "))
# data_pasien = cont.insert(jumlah_pasien)


# List Queue
for namaPasien in data_pasien.keys():
    if cont.listQueue(namaPasien, data_pasien) == "umum":
        q.enqueue(antrian_umum, namaPasien)
    else:
        q.enqueue(antrian_darurat, namaPasien)

# Show Data Pasien
print('=============================================================')
cont.show_data(data_pasien)

# Use Fasilitas
# Fasilitas Umum
if not q.isEmpty(antrian_umum):
    print("Antrian Umum")
    cont.use_fasilitas(antrian_umum, data_pasien, "Umum")
    print()
else:
    print("Antrian Umum Kosong")
# Fasilitas Darurat
if not q.isEmpty(antrian_darurat):
    print("Antrian Darurat")
    cont.use_fasilitas(antrian_darurat, data_pasien, "Darurat")
else:
    print("Antrian Darurat Kosong")
