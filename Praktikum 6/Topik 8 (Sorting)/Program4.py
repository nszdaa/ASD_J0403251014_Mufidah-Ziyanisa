#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 4
#=============================================

#Implementasi algoritma bubble sort yang lebih efisien.
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:   # ascending
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1
        
alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print("Sebelum modifikasi:", alist)

#Latihan: modifikasilah program yang
#awalnya mengurutkan secara menaik (ascending) 
#menjadi mengurutkan secara menurun (descending).

# Modifikasi menjadi descending
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i+1]:   # descending
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1
        
alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print("Hasil modifikasi:", alist)