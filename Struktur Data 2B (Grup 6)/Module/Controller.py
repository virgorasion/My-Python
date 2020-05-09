import Module.Queue as q

# Constanta Fasilitas
const_fasilitas = {"fasilitas": {"Umum": "Umum",
                                 "Darurat": "Darurat"}, "waktu": {"Umum": 20, "Darurat": 35}}


def insert(iterasi):
    data = {}
    for i in range(iterasi):
        print("Pasien Ke-{0}".format(i+1))
        input_nama = input("Nama Pasien: ").lower()
        # Create child dict
        child = {
            "kategori": input("Kondisi Penyakit: ").lower(),
            "waktu": int(input("Kebutuhan Waktu: ")),
            "fasilitas": ""
        }
        print()
        # Add child dict into data
        data[input_nama] = child
    return data  # return (dict)


def show_data(data_pasien):
    no = 0
    for pasien in data_pasien.keys():
        no += 1
        # Print Pasien
        print("{0} ({1})".format(pasien, no))
        for data in data_pasien[pasien]:
            # Print data pasien
            print("-{0}: {1}".format(data, data_pasien[pasien][data]))
        print()


def listQueue(pasien, data_pasien):
    # Check if kategori pasien is ringan or sedang
    if data_pasien[pasien]['kategori'] == "ringan" or data_pasien[pasien]['kategori'] == "sedang":
        # Update dict fasilitas into Umum
        data_pasien[pasien].update({"fasilitas": "Umum"})
        print(
            "Pasien {0} Tercatat Sebagai Pengguna Fasilitas Umum".format(pasien))
        return "umum"
    # check if kategori pasien is ringan or sedang
    elif data_pasien[pasien]['kategori'] == "berat":
        # Update dict pasien into Darurat
        data_pasien[pasien].update({"fasilitas": "Darurat"})
        print(
            "Pasien {0} Tercatat Sebagai Pengguna Fasilitas Darurat".format(pasien))
        return "darurat"
    else:
        data_pasien[pasien].update({"fasilitas": "Unknown"})
        print(
            "Pasien {0} Terdapat Kesalahan Penginputan Kategori".format(pasien))

def use_fasilitas(antrian, data_pasien, fasilitas):
    # Show First
    print("Antrian: {0}".format(antrian))
    # Loop until size antrian 0
    while q.size(antrian) > 0:
        # Decrease time data pasien then..
        # Check if pasien was having a time
        if decrease_time(data_pasien, q.first(antrian), fasilitas):
            print("Pasien {0} Membutuhkan Waktu {1}".format(
                q.first(antrian), check_time(data_pasien, q.first(antrian))))
            # Reverse Antrian
            q.enqueue(antrian, q.dequeue(antrian))
        else:
            print("Pasien {0} Telah Selesai Menggunakan Fasilitas".format(
                q.first(antrian)))
            # Delete Pasien From Antrian
            q.dequeue(antrian)
        print("Antrian: {0}".format(antrian))


def check_time(data_pasien, pasien):
    return data_pasien[pasien]['waktu']


def decrease_time(data_pasien, pasien, fasilitas):
    # Check fasilitas pasien equiv with const fasilitas
    if data_pasien[pasien]["fasilitas"] == fasilitas:
        # Check waktu pasien more than 0
        if data_pasien[pasien]["waktu"] > 0:
            # Decreasingn waktu pasien
            waktu = data_pasien[pasien]["waktu"] - \
                const_fasilitas["waktu"][fasilitas]
            # Update waktu pasien
            data_pasien[pasien].update({"waktu": waktu})
            # if after decrease waktu pasien under 1 then..
            if data_pasien[pasien]['waktu'] < 1:
                # delete from antrian
                return False
            return True
        else:
            return False
    else:
        print("Kami Tidak Memiliki Fasilitas Tersebut")
        return False
