# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Latihan 3 -  Implementasi Algoritma Prim
# ==========================================================

import heapq

# Representasi graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Priority queue untuk menyimpan edge
    edges = []

    # Memasukkan semua edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge dari node baru
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot =", total)


# ==================================================
# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan?
#    Node awal yang digunakan adalah A.
#
# 2. Edge mana yang dipilih pertama kali?
#    Edge (A, C) dengan bobot 2 dipilih pertama
#    karena merupakan edge terkecil dari node A.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Prim memilih edge dengan bobot terkecil yang
#    menghubungkan node yang sudah dikunjungi
#    dengan node yang belum dikunjungi.
#
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST adalah 6.
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Prim membangun MST mulai dari satu node dan
#    memperluasnya sedikit demi sedikit. Kruskal
#    mengurutkan semua edge berdasarkan bobot lalu
#    memilih edge terkecil yang tidak membentuk cycle.
# ==================================================