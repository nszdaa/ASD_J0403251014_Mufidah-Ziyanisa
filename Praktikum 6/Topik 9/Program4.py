#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Implementasi Algoritma Sequential Search
#=============================================

def sequentialSearch (data, value):
    pos = 0
    found = False
    while pos <len (data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
    return found

data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print (sequentialSearch (data, 3))
print (sequentialSearch (data, 13))

"""
Modifikasi Program 4 di atas hingga program tersebut:
1. Mengembalikan posisi (indeks) pertama dari nilai yang dicari pada list.
Apabila nilai tidak ditemukan, kembalikan -1.
2. Mengembalikan seluruh posisi dari nilai yang dicari pada list (Contoh: pada
saat mencari 2, nilai yang dikembalikan adalah [1, 9].
"""

# 1. Mengembalikan indeks pertama
def sequentialSearchIndex(data, value):
    pos = 0
    found = False
    
    while pos < len(data) and not found:
        if data[pos] == value:
            found = True
        else:
            pos = pos + 1
    
    if found:
        return pos
    else:
        return -1


# 2. Mengembalikan semua posisi
def sequentialSearchAll(data, value):
    posisi = []
    
    for i in range(len(data)):
        if data[i] == value:
            posisi.append(i)
    
    return posisi


data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]

print(sequentialSearchIndex(data, 3))   # jika tidak ada → -1
print(sequentialSearchIndex(data, 13))  # posisi pertama

print(sequentialSearchAll(data, 2))     # semua posisi nilai 2