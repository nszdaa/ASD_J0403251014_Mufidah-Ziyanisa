#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Latihan 5
#Latihan: Mencari nilai maksimum
#=============================================
 
def cari_maks(data, index=0): 
 
    # 1. BASE CASE (Kondisi Berhenti)
    # Jika index sudah sampai di elemen terakhir, kembalikan nilai tersebut.
    # Di sinilah program berhenti "menyelam" dan mulai membawa angka untuk dibanding.
    if index == len(data) - 1: 
        return data[index] 
 
    # 2. RECURSIVE CALL (Panggilan Berulang)
    # Program terus melompat ke index berikutnya (index + 1) sampai ke ujung.
    # Variabel 'maks_sisa' akan menyimpan pemenang dari elemen-elemen di depannya.
    maks_sisa = cari_maks(data, index + 1) 
 
    # 3. PROSES ADU TANDING (Alur Balik)
    # Setelah kembali dari rekursi, kita bandingkan angka saat ini dengan 
    # angka terbesar yang ditemukan dari sisa data di depannya.
    if data[index] > maks_sisa: 
        return data[index] # Angka saat ini lebih besar, dia jadi pemenang baru
    else: 
        return maks_sisa   # Angka di depannya lebih besar, pemenang tetap sama
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))