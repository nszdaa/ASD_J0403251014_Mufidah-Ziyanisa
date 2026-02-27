#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Praktikum 5 Materi 3
#Rekursi pada Data List
#=============================================

#Penjelasan Konsep:
#Rekursi dapat digunakan untuk memproses struktur data list
#secara bertahap dengan menggunakan index.
#Pada contoh ini, kita akan menjumlahkan seluruh elemen list
#dengan cara menggeser index dari 0 sampai akhir list.

#Setiap pemanggilan fungsi akan memproses satu elemen,
#lalu memanggil dirinya sendiri untuk memproses elemen berikutnya.

def jumlah_list(data, index=0):

    #Base Case
    #Jika index sudah sama dengan panjang list,
    #berarti semua elemen sudah diproses.
    #Maka fungsi berhenti dan mengembalikan 0.
    if index == len(data):
        return 0

    #Recursive Case
    #Ambil elemen pada index saat ini,
    #lalu tambahkan dengan hasil rekursi
    #untuk index berikutnya (index + 1).
    return data[index] + jumlah_list(data, index + 1)


#Pemanggilan fungsi
print(jumlah_list([2, 4, 6, 8]))  #Output: 20
