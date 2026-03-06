#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Implementasi Algoritma Binary Search
#=============================================

def binarySearch(data, item):
    first = 0
    last = len(data)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if data[midpoint] == item:
            found = True
        else:
            if item < data[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found
data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]
print(binarySearch(data, 3))
print(binarySearch(data, 13))


"""
Modifikasi Program 4 di atas hingga program tersebut:
1. Mengembalikan posisi (indeks) pertama dari nilai yang dicari pada list.
Apabila nilai tidak ditemukan, kembalikan -1.
2. Mengembalikan seluruh posisi dari nilai yang dicari pada list (Contoh: pada
saat mencari 2, nilai yang dikembalikan adalah [1, 9].
"""

# 1. Mengembalikan indeks pertama dengan Binary Search
def binarySearchIndex(data, item):
    data.sort()   # data harus terurut
    
    first = 0
    last = len(data) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        
        if data[midpoint] == item:
            return midpoint
        elif item < data[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    
    return -1


# 2. Mengembalikan semua posisi nilai
def binarySearchAll(data, item):
    posisi = []
    
    for i in range(len(data)):
        if data[i] == item:
            posisi.append(i)
    
    return posisi


data = [1, 2, 32, 8, 17, 19, 42, 13, 0, 2]

print(binarySearchIndex(data, 3))   # jika tidak ditemukan
print(binarySearchIndex(data, 13))  # indeks nilai 13

print(binarySearchAll(data, 2))     # semua posisi nilai 2