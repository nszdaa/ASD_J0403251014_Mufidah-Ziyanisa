#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Latihan 4
#Latihan: Kombinasi Huruf
#=============================================
 
def kombinasi(n, hasil=""): 
 
    # 1. BASE CASE (Kondisi Berhenti)
    # Jika panjang string 'hasil' sudah sama dengan 'n', 
    # cetak hasilnya dan berhenti (kembali ke tumpukan sebelumnya).
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    # 2. RECURSIVE CALL (Panggilan Berulang)
    # Setiap langkah akan bercabang menjadi dua pilihan:
    
    # Cabang kiri: Menambahkan huruf "A" ke kombinasi saat ini
    kombinasi(n, hasil + "A") 
    
    # Cabang kanan: Menambahkan huruf "B" ke kombinasi saat ini
    # Baris ini baru akan jalan setelah semua cabang "A" di atas selesai.
    kombinasi(n, hasil + "B") 
 
# Menjalankan fungsi untuk kombinasi 2 huruf
kombinasi(2)