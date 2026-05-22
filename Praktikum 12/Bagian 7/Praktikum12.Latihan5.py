# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Studi Kasus Jalur Terpendek Antar Kota
# Algoritma Dijkstra
# ==========================================================

import heapq

# Representasi graph berbobot
# Format:
# Kota : {Tujuan : Bobot}

graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek
    dari node awal ke semua node lain
    menggunakan algoritma Dijkstra
    """

    # Semua node diberi jarak tak hingga
    distances = {
        node: float('inf')
        for node in graph
    }

    # Jarak node awal = 0
    distances[start] = 0

    # Priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        # Lewati jika sudah ada jarak lebih kecil
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Update jika ditemukan jalur lebih pendek
            if distance < distances[neighbor]:

                distances[neighbor] = distance

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances


# Node awal
node_awal = 'Bogor'

# Jalankan Dijkstra
hasil = dijkstra(graph, node_awal)

# Tampilkan hasil
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis
# ==========================================================

# 1. Node awal yang digunakan adalah Bogor.

# 2. Node dengan jarak paling kecil dari node awal
#    adalah Depok dengan jarak 2.

# 3. Node dengan jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.

# 4. Algoritma Dijkstra bekerja dengan memilih
#    node dengan jarak terkecil terlebih dahulu,
#    lalu memperbarui jarak ke node tetangga
#    jika ditemukan jalur yang lebih pendek.
#    Pada kasus ini:
#    Bogor -> Depok = 2
#    Bogor -> Depok -> Jakarta = 4
#    Bogor -> Depok -> Bandung = 8
#    sehingga diperoleh jalur terpendek
#    dari Bogor ke semua kota.