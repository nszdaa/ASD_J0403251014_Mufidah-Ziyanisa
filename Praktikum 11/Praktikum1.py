# =====================================
# Praktikum 1 - Adjacency Matrix
# Nama : Mufidah Ziyanisa
# NIM  : J0403251014
# =====================================

# Membuat adjacency matrix graph
adj_matrix = [
    [0, 1, 1, 0],  # simpul 0
    [1, 0, 1, 0],  # simpul 1
    [1, 1, 0, 1],  # simpul 2
    [0, 0, 1, 0]   # simpul 3
]

# Menampilkan adjacency matrix
print("Adjacency Matrix:\n")

for baris in adj_matrix:
    print(baris)

# Penjelasan setiap baris
print("\nPenjelasan:")

print("Baris 0 : Simpul 0 terhubung ke simpul 1 dan 2")
print("Baris 1 : Simpul 1 terhubung ke simpul 0 dan 2")
print("Baris 2 : Simpul 2 terhubung ke simpul 0, 1, dan 3")
print("Baris 3 : Simpul 3 terhubung ke simpul 2")