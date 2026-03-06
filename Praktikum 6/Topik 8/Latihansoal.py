"""
Gunakanlah program-program pengurutan di atas untuk menyelesaikan
permasalahan berikut:
Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:
[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
Soal:
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
2. Kandidat berapa saja yang lolos?

Gunakanlah program-program pengurutan yang telah dipelajar untuk menyelesaikan permasalahan berikut: 
Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100. Berikut adalah data hasil tes potensi akademik yang tersedia: [43, 76, 12, 89, 33, 57, 98, 22, 68, 9] Soal: 
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah. 
2. Kandidat berapa saja yang lolos?
"""

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Bubble Sort descending
for i in range(len(data)):
    for j in range(0, len(data)-i-1):
        if data[j] < data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print("Data setelah diurutkan:", data)

print("5 Kandidat dengan nilai tertinggi:")
for i in range(5):
    print(data[i])