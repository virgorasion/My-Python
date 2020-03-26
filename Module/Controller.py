import Module.Queue as q

# Constanta Fasilitas
const_fasilitas = {"fasilitas":{"Umum":"Umum","Darurat":"Darurat"},"waktu":{"Umum":20,"Darurat":35}}

def insert(iterasi):
    data = {}
    for i in range(iterasi):
        print("Pasien Ke-{0}".format(i+1))
        input_nama = input("input nama: ").lower()
        # Create child dict
        child = {
            "kategori": input("input Kategori: ").lower(),
            "waktu": int(input("input waktu: ")),
            "fasilitas":""
        }
        print()
        # Add child dict into data
        data[input_nama] = child            
    return data #return (dict)

def show_data(data_pasien):
    no = 0
    for pasien in data_pasien.keys():
        no += 1
        # Print Pasien
        print("{0} ({1})".format(pasien,no))
        for data in data_pasien[pasien]:
            # Print data pasien
            print("-{0}: {1}".format(data,data_pasien[pasien][data]))
        print()

def listQueue(pasien, data_pasien):
    # Check if kategori pasien is ringan or sedang
    if data_pasien[pasien]['kategori'] == "ringan" or data_pasien[pasien]['kategori'] == "sedang":
        # Update dict fasilitas into Umum
        data_pasien[pasien].update({"fasilitas":"Umum"})
        print("Pasien {0} Masuk Kedalam Fasilitas Umum".format(pasien))
        return "umum"
    #check if kategori pasien is ringan or sedang 
    elif data_pasien[pasien]['kategori'] == "berat":
        # Update dict pasien into Darurat
        data_pasien[pasien].update({"fasilitas":"Darurat"})
        print("Pasien {0} Masuk Kedalam Fasilitas Darurat".format(pasien))
        return "darurat"
    else:
        print("Pasien {0} Terdapat Kesalahan Penginputan Kategori".format(pasien))

# def use_fasilitas(antrian,data_pasien,fasilitas):
#     # Loop antrian
#     while q.size(antrian) > 0:
#         # Make antrian reverse 1 by 1
#         for i in range(0,1):
#             # print antrian
#             print("Antrian: {0}".format(antrian))
#             # check if fasilitas in data_pasien equivalent with fasilitas in const_fasilitas
#             if data_pasien[antrian[i]]["fasilitas"] == const_fasilitas["fasilitas"].get(fasilitas):
#                 # check if waktu pasien more than 0
#                 if data_pasien[antrian[i]]["waktu"] > 0:
#                     # decrease waktu pasien
#                     waktu_temp = data_pasien[antrian[i]]["waktu"] - const_fasilitas["waktu"].get(fasilitas)
#                     # update waktu pasien in data_pasien
#                     data_pasien[antrian[i]].update({"waktu":waktu_temp})
#                     # after decrease, check data_pasien if waktu pasien more than 1
#                     if data_pasien[antrian[i]]['waktu'] > 1:
#                         print("Pasien {0} Masih Membutuhkan Waktu {1}".format(antrian[i], waktu_temp))
#                         # reverse antrian
#                         q.enqueue(antrian, q.dequeue(antrian))
#                     else:
#                         # decrease antrian
#                         q.dequeue(antrian)
#                 # if antrian not null
#                 elif not q.isEmpty(antrian):
#                     # decrease antrian
#                     q.dequeue(antrian)
#                     print("Antrian: {0}".format(antrian))

# Another Logic
def use_fasilitas(antrian,data_pasien,fasilitas):
    print("Antrian: {0}".format(antrian))
    while q.size(antrian) > 0:
        for i in range(1):
            if decrease_time(data_pasien, q.first(antrian), fasilitas):
                print("Pasien {0} Membutuhkan Waktu {1}".format(q.first(antrian), check_time(data_pasien, q.first(antrian))))
                # print(True)
                q.enqueue(antrian, q.dequeue(antrian))
            else:
                print("Pasien {0} Membutuhkan Waktu {1}".format(q.first(antrian), check_time(data_pasien, q.first(antrian))))
                q.dequeue(antrian)
            print(antrian)

def check_time(data_pasien,pasien):
    return data_pasien[pasien]['waktu']
                
def decrease_time(data_pasien, pasien, fasilitas):
    if data_pasien[pasien]["fasilitas"] == fasilitas:
        if data_pasien[pasien]["waktu"] > 0:
            waktu = data_pasien[pasien]["waktu"] - const_fasilitas["waktu"][fasilitas]
            data_pasien[pasien].update({"waktu":waktu})
            if data_pasien[pasien]['waktu'] < 1:
                return False
            return True
        else:
            return False