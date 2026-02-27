#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Materi 2
#Tracing masuk/keluar
#=============================================

#Tujuannya untuk memahami proses "Masuk" (stacking) dan "Keluar" (unwinding)
#pada fungsi rekursif menggunakan call stack.

def hitung(n):
    #Base Cas
    #Jika n == 0, fungsi berhenti
    if n == 0:
        print("Selesai")
        return
    
    #Fase Stacking (Masuk)
    #Fungsi dipanggil dan masuk ke dalam stack
    print("Masuk:", n)
    #Pemanggilan rekursif (masalah diperkecil)
    hitung(n - 1)

    #Fase Unwinding (Keluar
    #Dieksekusi setelah fungsi rekursif selesai
    print("Keluar:", n)


#Pemanggilan fungsi
hitung(3)