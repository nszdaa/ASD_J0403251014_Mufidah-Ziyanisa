# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal = 0
    distances[start] = 0

    # Relaksasi edge sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:

            for neighbor, weight in graph[node].items():

                # Jika ditemukan jalur lebih pendek
                if (distances[node] != float('inf')
                        and distances[node] + weight < distances[neighbor]):

                    distances[neighbor] = distances[node] + weight

    return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)


# Jawaban Analisis:

# 1. Bobot langsung dari A ke B adalah 5

# 2. Total bobot jalur A -> C -> B adalah 2
#    karena 4 + (-2) = 2

# 3. Jalur yang menghasilkan jarak lebih kecil menuju B
#    adalah A -> C -> B dengan total bobot 2
#    dibanding A -> B yang bobotnya 5

# 4. Bellman-Ford dapat digunakan pada graph
#    dengan bobot negatif karena algoritma ini
#    memeriksa dan memperbarui jarak berkali-kali
#    melalui proses relaksasi edge.

# 5. Relaksasi edge adalah proses mengecek
#    apakah ada jalur yang lebih pendek menuju
#    suatu node melalui edge tertentu.

# 6. Perbedaan utama:
#    - Dijkstra tidak dapat menangani bobot negatif
#      tetapi lebih cepat.
#    - Bellman-Ford dapat menangani bobot negatif
#      tetapi prosesnya lebih lambat.