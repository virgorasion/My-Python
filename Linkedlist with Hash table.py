# Function untuk menampilkan Hash 
def display_hash(hashTable): 
	
	for i in range(len(hashTable)): 
		print(i, end = " ") 
		
		for j in hashTable[i]: 
			print("-->", end = " ") 
			print(j, end = " ") 
			
		print() 

# Creating Hashtable
HashTable = [[] for _ in range(10)] # ganti range untuk menambah jumlah table

# Hashing Function to get a key 
def Hashing(keyvalue): 
	return keyvalue % len(HashTable)

def dataPoli():
	getJumlah = 1 #int(input("Masukkan Banyak Poli Pasien"))
	data = []
	for i in range(getJumlah):
		temp = []
		temp.append(input("Nama Poli: "))
		temp.append(input("Riwayat Kundingan: "))
		data.append(temp)
	return data

def dataPasien(key,nama,bpjs):
    data = {}
    data["nama"] = nama
    data["bpjs"] = bpjs
    data["poli"] = dataPoli()
    return data

# Insert Function to add 
# values to the hash table 
def insert(Hashtable, keyvalue): 
	# nama = input("Masukkan Nama Pasien : ")
	# bpjs = bool(input("Kepemilikan BPJS : "))
	hash_key = Hashing(keyvalue) 
	Hashtable[hash_key].append(dataPasien(keyvalue,"Fauzan","yes"))

# def serach(Hashtable, keyvalue):


# Driver Code 
insert(HashTable, 10) 
insert(HashTable, 25) 
insert(HashTable, 25) 
# insert(HashTable, 20, 'Mathura') 
# insert(HashTable, 9, 'Delhi') 
# insert(HashTable, 21, 'Punjab') 
# insert(HashTable, 21, 'Noida') 
print(HashTable[Hashing(10)])
# print(HashTable)
display_hash (HashTable)
