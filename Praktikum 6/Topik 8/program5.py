#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 5
#=============================================

#Implementasi algoritma selection sort.
def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMin = 0
        for location in range(1, fillslot+1):
            if data[location] < data[positionOfMin]:  # diubah untuk descending
                positionOfMin = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print("Sebelum modifikasi (ascending):", data)

#Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
#awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara
#menurun (descending).

#yang awalnya if data[location]>data[positionOfMax]: menjadi if data[location] < data[positionOfMin]: 

def selectionSort(data):
    for fillslot in range(len(data)-1,0,-1):
        positionOfMin = 0
        for location in range(1, fillslot+1):
            if data[location] > data[positionOfMin]:  # diubah untuk descending
                positionOfMin = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMin]
        data[positionOfMin] = temp

data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print("Setelah modifikasi (descending):", data)