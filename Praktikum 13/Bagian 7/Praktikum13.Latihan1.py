# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 13 - Graph III: Spanning Tree 
# ======================================

# ==========================================================
# Latihan 1 - Memahami Konsep Spanning Tree
# ==========================================================

# Daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==================================================
# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal berisi semua edge yang tersedia dan
#    dapat memiliki cycle (siklus). Sedangkan spanning
#    tree adalah subgraph yang menghubungkan semua
#    vertex tanpa membentuk cycle.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena tujuan spanning tree adalah menghubungkan
#    seluruh vertex dengan jalur yang paling sederhana.
#    Jika terdapat cycle, maka ada edge yang tidak
#    diperlukan sehingga bukan lagi tree.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena untuk graph dengan n vertex, spanning tree
#    hanya membutuhkan n - 1 edge agar semua vertex
#    tetap terhubung tanpa cycle. Pada graph ini ada
#    4 vertex, sehingga spanning tree hanya memiliki
#    3 edge, sedangkan graph awal memiliki 5 edge.
# ==================================================