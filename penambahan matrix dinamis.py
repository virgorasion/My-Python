def getMatrix():
    dataMatrix = []
    for matrix in range(1,3):
        baris = int(input("Masukkan Jumlah Baris Matrix Ke-{0} ".format(matrix)))
        kolom = int(input("Masukkan Jumlah Kolom Matrix Ke-{0} ".format(matrix)))
        dataMatrix.append(isiMatrix(matrix,baris,kolom))
    perkalianMatrix(dataMatrix[0], dataMatrix[1])

def isiMatrix(indexMatrix, barisMatrix, kolomMatrix):
    matrix = []
    for baris in range(barisMatrix):
        dataMatrix = []
        for kolom in range(kolomMatrix):
            dataMatrix.append(int(input("Matrix Ke-{0} [{1},{2}] = ".format(indexMatrix,baris,kolom))))
        matrix.append(dataMatrix)
    return matrix

def tampilkanMatrix(matrix):
    for baris in range(len(matrix)):
        for kolom in range(len(matrix[0])):
            print(matrix[baris][kolom], end=" ")
        print()
    print()

def perkalianMatrix(matrixPertama, matrixKedua):
    hasil = []
    for baris in range(len(matrixPertama)):
        temp = []
        for kolom in range(len(matrixKedua)):
            jumlah = matrixPertama[baris][kolom] + matrixKedua[baris][kolom]
            temp.append(jumlah)
        hasil.append(temp)
    print()
    print("Matrix Pertama")
    tampilkanMatrix(matrixPertama)
    print("Matrix Kedua")
    tampilkanMatrix(matrixKedua)
    print("Hasil Penjumlahan")
    tampilkanMatrix(hasil)

getMatrix()
