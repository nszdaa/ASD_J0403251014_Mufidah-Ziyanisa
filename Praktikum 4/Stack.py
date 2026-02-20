#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Implementasi Dasar: Stack
#=============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika kelas Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)

#stack ada operasi push(memasukkan heas baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None

    def push(self,data):
       #1 membuat node baru 
       nodeBaru = Node(data) #instantiasi/memamnggil konstruktor pada class Node

       #2 node baru menunjuk ke top yang lama (head lama)
       nodeBaru.next = self.top

       #3 geser top pindah ke node baru 
       self.top = nodeBaru

    def pop(self): #mengambil / menghapus node paling atas (top/head)
        if self.is_empty():
            print("stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        self.top = self.top.next #geser top ke node berikutnya
        return data_terhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
         return None
        return self.top.data
    
    def tampilkan(self):
        #Top -> A -> B
        current = self.top 
        print("Top" , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("peek (lihat top):", s.peek())
s.pop()
s.tampilkan()
print("peek (Lihat Top):", s.peek())





