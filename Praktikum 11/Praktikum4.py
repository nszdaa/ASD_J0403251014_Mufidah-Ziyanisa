# ================================================
# Praktikum 4 - Studi Kasus Dunia Nyata
# Studi Kasus : Jaringan Komputer Topologi Bus
# Nama : Mufidah Ziyanisa
# NIM  : J0403251014
# ================================================

# ADJACENCY LIST
graph = {
    "Server": ["PC1", "PC2"],
    "PC1": ["Server", "PC2", "PC3"],
    "PC2": ["Server", "PC1", "PC3"],
    "PC3": ["PC2", "Printer", "PC1"],
    "Printer": ["PC3"]
}

# NAMA NODE
nodes = ["Server", "PC1", "PC2", "PC3", "Printer"]

# ADJACENCY MATRIX
matrix = [
#          S  P1 P2 P3 PR
    [0, 1, 1, 0, 0],  # Server
    [1, 0, 1, 1, 0],  # PC1
    [1, 1, 0, 1, 0],  # PC2
    [0, 1, 1, 0, 1],  # PC3
    [0, 0, 0, 1, 0]   # Printer
]

# MENAMPILKAN NAMA NODE
print("DAFTAR NODE:")
for node in nodes:
    print("-", node)

# MENAMPILKAN HUBUNGAN ANTAR NODE
print("\nHUBUNGAN ANTAR NODE:")
for node in graph:
    print(node, "terhubung ke", graph[node])

# MENAMPILKAN ADJACENCY LIST
print("\nADJACENCY LIST:")
for node in graph:
    print(node, "->", graph[node])

# MENAMPILKAN ADJACENCY MATRIX
print("\nADJACENCY MATRIX:")

for row in matrix:
    print(row)