#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Materi 5
#Backtracking dengan Pruning (Pemangkasan) 
#=============================================


#Penjelasan Konsep:
#Pruning adalah strategi untuk menghentikan eksplorasi
#pada cabang yang sudah pasti tidak memenuhi syarat.
#Dengan pruning, pencarian menjadi lebih efisien karena
#tidak semua kemungkinan dieksplor sampai akhir.

def biner_batas(n, batas, hasil="", jumlah_1=0):

    #PRUNING
    #Jika jumlah '1' sudah melebihi batas,
    #maka cabang ini dihentikan (tidak dilanjutkan).
    if jumlah_1 > batas:
        return

    #BASE CASE
    #Jika panjang kombinasi sudah n,
    #maka cetak hasil.
    if len(hasil) == n:
        print(hasil)
        return

    #CHOOSE + EXPLORE

    #Pilih '0' (jumlah_1 tidak berubah)
    biner_batas(n, batas, hasil + "0", jumlah_1)

    #Pilih '1' (jumlah_1 bertambah 1)
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


#Pemanggilan fungsi
biner_batas(4, 2)

