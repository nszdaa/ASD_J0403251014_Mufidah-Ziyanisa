#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Materi 4
#Konsep Dasar Backtracking
#=============================================

#Penjelasan Konsep:
#Backtracking adalah teknik pencarian solusi dengan mencoba
#semua kemungkinan secara sistematis.

#Pola umum backtracking:
#1. Choose   = memilih satu kemungkinan
#2. Explore  = melanjutkan ke kemungkinan berikutnya (rekursif)
#3. Kembali (otomatis saat fungsi selesai / unwinding)

#Pada contoh ini, kita akan menghasilkan semua kombinasi
#biner sepanjang n (hanya terdiri dari '0' dan '1').

def biner(n, hasil=""):
    #Base Case
    #Jika panjang string sudah sama dengan n,
    #maka kombinasi sudah lengkap dan dicetak.
    if len(hasil) == n:
        print(hasil)
        return

    #Choose + Explore
    #Pilih '0' dan lanjutkan eksplorasi
    biner(n, hasil + "0")

    #Pilih '1' dan lanjutkan eksplorasi
    biner(n, hasil + "1")


# Pemanggilan fungsi
biner(3)