# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Latihan 4 
# Studi Kasus: Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal
# ==========================================================

# Daftar edge: (biaya, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan biaya terkecil
edges.sort()

mst = []
total_biaya = 0
connected = set()

# Proses pemilihan edge
for biaya, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, biaya))
        total_biaya += biaya
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum (MST):")
for edge in mst:
    print(edge)

print("\nTotal biaya minimum =", total_biaya)

# ==================================================
# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal.
#
# 2. Edge mana saja yang dipilih?
#    (GedungC, GedungD, 1)
#    (GedungA, GedungC, 2)
#    (GedungB, GedungD, 3)
#
# 3. Berapa total biaya minimum?
#    1 + 2 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena MST dapat menghubungkan seluruh gedung
#    dengan biaya pemasangan kabel minimum tanpa
#    adanya jalur yang tidak diperlukan (cycle).
# ==================================================