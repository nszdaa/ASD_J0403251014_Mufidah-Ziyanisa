#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 6
#=============================================

#Implementasi algoritma selection sort.
def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] > currentvalue:
            data[position] = data[position-1]
            position = position - 1

        data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print("Sebelum modifikasi:", data)

#Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
#awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara
#menurun (descending).

def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index

        while position > 0 and data[position-1] < currentvalue:
            data[position] = data[position-1]
            position = position - 1

        data[position] = currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print("Hasil modifikasi:", data)