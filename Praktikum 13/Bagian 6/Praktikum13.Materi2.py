# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Implementasi Algoritma Prim
# ==========================================================

# Mengimpor modul heapq untuk membuat priority queue
import heapq

# Representasi graph berbobot menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan kandidat edge dalam priority queue
    edges = []

    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot MST
    total_weight = 0

    # Selama masih ada edge yang dapat diproses
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sebagai sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total bobot MST
            total_weight += weight

            # Menambahkan edge dari node baru ke priority queue
            for neighbor, w in graph[v].items():

                # Hanya tambahkan node yang belum dikunjungi
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan MST dan total bobot
    return mst, total_weight


# Menjalankan algoritma Prim dengan node awal A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)


# ==================================================
# Jawaban Analisis
# ==================================================
#
# 1. Node awal yang digunakan adalah A.
#
# 2. Edge pertama yang dipilih adalah A-C
#    karena memiliki bobot terkecil (2)
#    dari semua edge yang terhubung ke A.
#
# 3. Edge berikutnya dipilih berdasarkan
#    bobot terkecil yang menghubungkan
#    node yang sudah dikunjungi dengan
#    node yang belum dikunjungi.
#
# 4. Edge yang masuk MST:
#    A-C (2)
#    C-D (1)
#    D-B (3)
#
# 5. Total bobot MST:
#    2 + 1 + 3 = 6
#
# 6. Perbedaan Prim dan Kruskal:
#    - Prim membangun tree dari satu node awal.
#    - Kruskal memilih edge terkecil secara global.
#
# ==================================================