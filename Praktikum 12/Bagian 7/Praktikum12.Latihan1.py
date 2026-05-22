# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9
#    karena 4 + 5 = 9
#
# 2. Total bobot jalur A -> C -> D adalah 3
#    karena 2 + 1 = 3
#
# 3. Jalur terpendek yang dipilih adalah
#    A -> C -> D karena memiliki total bobot lebih kecil.
#
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge
#    paling sedikit karena pada weighted graph setiap edge
#    memiliki bobot yang berbeda. Jalur dengan edge lebih
#    banyak bisa memiliki total bobot lebih kecil.