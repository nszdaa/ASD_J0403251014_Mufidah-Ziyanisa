# =====================================
# Praktikum 2 - Adjacency List
# Nama : Mufidah Ziyanisa
# NIM  : J0403251014
# =====================================

# Membuat adjacency list menggunakan dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Menampilkan adjacency list
print("Adjacency List:\n")

for node in graph:
    print(node, "->", graph[node])