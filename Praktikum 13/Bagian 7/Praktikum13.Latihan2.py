# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Latihan 2 -  Implementasi Sederhana Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

# Proses pemilihan edge
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# ==================================================
# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    Edge ('C', 'D') dengan bobot 1 dipilih pertama
#    karena memiliki bobot paling kecil.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal menggunakan metode
#    greedy, yaitu selalu memilih edge dengan
#    bobot terkecil yang tidak membentuk cycle.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST yang dihasilkan adalah 6.
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Karena semua node sudah terhubung sehingga
#    penambahan edge lain akan membentuk cycle
#    dan membuat total bobot lebih besar.
# ==================================================