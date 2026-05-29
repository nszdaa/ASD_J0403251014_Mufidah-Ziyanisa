# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Latihan 5
# Kasus 2: Jaringan Komputer
# Menggunakan Algoritma Prim
# ==========================================================

import heapq

# Representasi weighted graph
graph = {
    'RouterA': {'RouterB': 3, 'RouterC': 2},
    'RouterB': {'RouterA': 3, 'RouterD': 5, 'RouterC': 4},
    'RouterC': {'RouterA': 2, 'RouterD': 1, 'RouterB': 4},
    'RouterD': {'RouterB': 5, 'RouterC': 1}
}

# Fungsi Algoritma Prim
def prim(graph, start):
    visited = set([start])
    edges = []

    # Menambahkan edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge dari node yang baru dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Menjalankan algoritma Prim dari RouterA
mst, total = prim(graph, 'RouterA')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

print("Total bobot minimum =", total)

# ==================================================
# Jawaban Analisis:
#
# 1. Kasus apa yang dipilih?
#    Kasus 2: Jaringan Komputer.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Prim.
#
# 3. Edge mana saja yang dipilih dalam MST?
#    (RouterA, RouterC, 2)
#    (RouterC, RouterD, 1)
#    (RouterA, RouterB, 3)
#
# 4. Berapa total bobot MST?
#    2 + 1 + 3 = 6
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Edge (RouterB, RouterC, 4) dan
#    (RouterB, RouterD, 5) tidak dipilih
#    karena sudah ada jalur yang menghubungkan
#    semua router dengan bobot yang lebih kecil.
#    Jika ditambahkan, akan membentuk cycle
#    dan menambah total bobot.
# ==================================================