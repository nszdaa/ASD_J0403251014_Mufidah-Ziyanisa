# =====================================
# Praktikum 3 - Konversi Matrix ke List
# Nama : Mufidah Ziyanisa
# NIM  : J0403251014
# =====================================

# Adjacency Matrix
matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]
# Nama node
nodes = [0, 1, 2, 3]
# Dictionary untuk adjacency list
adj_list = {}
# Konversi matrix ke adjacency list
for i in range(len(matrix)):
    tetangga = []

    for j in range(len(matrix[i])):
        if matrix[i][j] == 1:
            tetangga.append(nodes[j])

    adj_list[nodes[i]] = tetangga
# Menampilkan adjacency list
print("Adjacency List:\n")
for node in adj_list:
    print(node, "->", adj_list[node])