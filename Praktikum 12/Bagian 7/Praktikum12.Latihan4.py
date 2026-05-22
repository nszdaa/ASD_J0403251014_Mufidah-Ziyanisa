# ======================================
# Nama  : Mufidah Ziyanisa
# NIM   : J0403251014
# Kelas : TPL 1/P1
# Praktikum 12 - Graph II: Shortest Path 
# ======================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")

for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# Jawaban Analisis:

# 1. Lokasi yang paling dekat dari Gerbang adalah
#    Kantin dengan waktu 2 menit.

# 2. Waktu tempuh terpendek dari Gerbang ke Aula
#    adalah 7 menit.
#    Jalur:
#    Gerbang -> Kantin -> Lab -> Aula
#    2 + 4 + 1 = 7 menit

# 3. Jalur langsung tidak selalu menghasilkan
#    jarak paling kecil karena bisa saja
#    jalur melalui lokasi lain memiliki
#    total bobot lebih kecil.

# 4. Dijkstra cocok digunakan karena semua
#    bobot waktu tempuh bernilai positif
#    dan algoritma ini efektif untuk mencari
#    jalur tercepat pada graph berbobot.