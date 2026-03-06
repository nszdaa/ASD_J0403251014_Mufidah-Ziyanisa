#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 7
#=============================================

# Implementasi algoritma shell sort (ascending)
def shellSort(data):
    sublistcount = len(data)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2


def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):

        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]
shellSort(data)
print("Sebelum modifikasi:", data)

# Modifikasi menjadi descending
def shellSort(data):
    sublistcount = len(data)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2


def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):

        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] < currentvalue:
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue


data = [54,26,93,17,77,31,44,55,20]
shellSort(data)
print("Hasil modifikasi:", data)