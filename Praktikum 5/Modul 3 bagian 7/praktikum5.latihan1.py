#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Latihan 1
#Latihan: Rekursi Dasar
#=============================================

def pangkat(a, n): 
    # 1. KONDISI BERHENTI (Base Case)
    # Jika pangkat (n) sudah nol, program berhenti "menyelam" 
    # dan mulai mengirim balik angka 1 ke atas.
    if n == 0: 
        return 1 
    
    # 2. PROSES REKURSI (Recursive Case)
    # Program belum bisa mengalikan 'a' sekarang karena harus tahu 
    # hasil dari 'pangkat(a, n - 1)' terlebih dahulu.
    # Ini akan menumpuk operasi perkalian di memori (Stack).
    return a * pangkat(a, n - 1) 

# 3. TITIK MULAI
# Memanggil 2 pangkat 4.
print(pangkat(2, 4))  # Output: 16