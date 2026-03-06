#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 8
#=============================================

#Implementasi algoritma quick sort

# Implementasi algoritma quick sort (ascending)
def quickSort(data):
    quickSortHelper(data, 0, len(data)-1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)

        quickSortHelper(data, first, splitpoint-1)
        quickSortHelper(data, splitpoint+1, last)

def partition(data, first, last):
    pivotvalue = data[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [54,26,93,17,77,31,44,55,20]

quickSort(data)
print("Sebelum modifikasi:", data)

#Ketik kembali kode program di atas. Setelah itu, modifikasilah program yang
#awalnya mengurutkan secara menaik (ascending) menjadi mengurutkan secara
#menurun (descending).

# Modifikasi menjadi descending
def quickSort(data):
    quickSortHelper(data, 0, len(data)-1)

def quickSortHelper(data, first, last):
    if first < last:
        splitpoint = partition(data, first, last)

        quickSortHelper(data, first, splitpoint-1)
        quickSortHelper(data, splitpoint+1, last)

def partition(data, first, last):
    pivotvalue = data[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [54,26,93,17,77,31,44,55,20]

quickSort(data)
print("Hasil modifikasi:", data)