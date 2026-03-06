#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 3 
#=============================================

#Implementasi algoritma bubble sort pada Python.
def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                # Tukar dua data bersebelahan yang urutannya salah
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print(data)
