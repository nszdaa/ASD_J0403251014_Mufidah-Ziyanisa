# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Praktikum 12 - Implementasi Algoritma Dijkstra
# Praktikum 12 Materi 1
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
    # Semua node awalnya bernilai tak hingga
    distances = {
        node: float('inf')
        for node in graph
    }

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue
    # Menyimpan pasangan (jarak, node)
    pq = [(0, start)]

    # Selama masih ada node di priority queue
    while pq:

        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Periksa semua tetangga node saat ini
        for neighbor, weight in graph[current_node].items():

            # Hitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:

                # Update jarak
                distances[neighbor] = distance

                # Masukkan kembali ke priority queue
                heapq.heappush(
                    pq,
                    (distance, neighbor)
                )

    # Mengembalikan hasil jarak terpendek
    return distances


# Menjalankan fungsi Dijkstra
# Node awal = A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
print(hasil)