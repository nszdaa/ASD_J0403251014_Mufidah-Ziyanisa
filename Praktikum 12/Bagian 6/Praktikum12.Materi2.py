# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Praktikum 12 - Implementasi Algoritma Dijkstra
# Praktikum 12 Materi 2
# ==========================================================

# Import library heapq
# Digunakan untuk membuat priority queue
import heapq

# Representasi weighted graph menggunakan dictionary
# Format:
# Node : {Tetangga : Bobot}
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):

    # Menyimpan jarak minimum dari node awal
    # Awalnya semua node bernilai tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue digunakan untuk memilih
    # node dengan jarak terkecil terlebih dahulu
    pq = [(0, start)]

    # Selama masih ada node di priority queue
    while pq:

        # Mengambil node dengan jarak minimum
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Perbarui jarak minimum
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    # Mengembalikan hasil jarak terpendek
    return distances


# Menjalankan algoritma Dijkstra
# Node awal = A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print(hasil)

# ==========================================================
# Output:
# {'A': 0, 'B': 4, 'C': 2, 'D': 3}
#
# Penjelasan:
# Jarak dari A ke A = 0
# Jarak dari A ke B = 4
# Jarak dari A ke C = 2
# Jarak dari A ke D = 3
#
# Jalur A -> D dipilih melalui C
# karena A -> C -> D = 2 + 1 = 3
# lebih kecil dibanding A -> B -> D = 4 + 5 = 9
# ==========================================================