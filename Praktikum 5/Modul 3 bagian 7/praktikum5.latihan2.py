#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Latihan 2
#Latihan: Tracing Rekursi 
#=============================================

def countdown(n):

    #Base case: jika n == 0, hentikan rekursi
    if n == 0:
        print("Selesai")
        return  # fungsi berhenti dan kembali ke pemanggil sebelumnya

    #Fase masuk (turun rekursi)
    #Cetak nilai n sebelum memanggil fungsi lagi
    print("Masuk:", n)

    #Pemanggilan rekursif
    #Fungsi memanggil dirinya sendiri dengan n-1
    countdown(n - 1)

    #Fase keluar (naik/backtracking)
    #Baris ini dijalankan setelah fungsi rekursif selesai
    print("Keluar:", n)


#Pemanggilan awal fungsi
countdown(3)

"""
Alur Program Singkat:

1. countdown(3) → cetak "Masuk: 3"
2. countdown(2) → cetak "Masuk: 2"
3. countdown(1) → cetak "Masuk: 1"
4. countdown(0) → cetak "Selesai" (base case)

Setelah mencapai base case, fungsi selesai satu per satu:
- Cetak "Keluar: 1"
- Cetak "Keluar: 2"
- Cetak "Keluar: 3"

Output "Keluar" terbalik karena rekursi bekerja seperti stack (Last In First Out).
"""