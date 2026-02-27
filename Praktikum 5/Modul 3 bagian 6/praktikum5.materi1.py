#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Materi 1
#Konsep Dasar Rekursif
#=============================================

#Penjelasan:
#Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri
#untuk menyelesaikan masalah yang lebih kecil sampai mencapai
#kondisi berhenti (base case).

#Dalam rekursi wajib ada:
#1. Base Case      = kondisi berhenti
#2. Recursive Case = pemanggilan fungsi dengan masalah lebih kecil

def faktorial(n):
    #Base Case
    #Jika n == 0, maka faktorial bernilai 1
    #berhenti ketika n = 0
    #Ini adalah kondisi berhenti agar tidak terjadi infinite recursion
    if n == 0:
        return 1

    #Recursive Case
    #Fungsi memanggil dirinya sendiri
    #Masalah diperkecil menjadi (n - 1)
    return n * faktorial(n - 1)


#Pemanggilan fungsi
print(faktorial(5))  #Output: 120