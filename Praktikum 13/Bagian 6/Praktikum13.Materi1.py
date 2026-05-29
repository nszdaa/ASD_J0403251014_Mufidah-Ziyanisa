# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge dalam format:
# (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan edge yang terpilih ke dalam MST
mst = []

# Menyimpan total bobot MST
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Memproses setiap edge yang telah diurutkan
for weight, u, v in edges:

    # Jika salah satu node belum terhubung,
    # maka edge dianggap aman untuk dipilih
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot edge ke total bobot
        total_weight += weight

        # Menandai node sebagai sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge yang terpilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)

# ==================================================
# Jawaban Analisis
# ==================================================
#
# 1. Edge pertama yang dipilih adalah C-D
#    karena memiliki bobot paling kecil yaitu 1.
#
# 2. Algoritma Kruskal selalu memilih edge
#    dengan bobot terkecil terlebih dahulu.
#
# 3. Edge yang masuk MST adalah:
#    C-D (1)
#    A-C (2)
#    B-D (3)
#
# 4. Total bobot MST:
#    1 + 2 + 3 = 6
#
# 5. Edge A-B dan A-D tidak dipilih karena
#    semua node sudah terhubung sehingga
#    penambahan edge tersebut tidak diperlukan.
#
# ==================================================