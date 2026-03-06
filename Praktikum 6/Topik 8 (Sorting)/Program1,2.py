#=============================================
#Nama    : Mufidah Ziyanisa
#NIM     : J0403251014
#Kelas   : TPL A/P1
#Program : 1 dan 2
#=============================================

# Program 1. Fungsi sorted() pada python untuk mengurutkan list
a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
print("Hasil sorted():", sorted(a))
print("List asli:", a)

# Program 2. Fungsi sort() pada python untuk mengurutkan list
a = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
a.sort()
print("Hasil sort():", a)

print("\n1. Perbedaan sorted() dan sort():")
print("sorted() mengurutkan data tetapi tidak mengubah list asli karena membuat list baru.")
print("sort() mengurutkan langsung pada list sehingga list asli berubah.")

print("\n2. Kondisi list setelah fungsi dijalankan:")
print("sorted() -> list asli tetap sama.")
print("sort() -> list asli berubah menjadi urutan baru.")