#=============================================
#Nama   : Mufidah Ziyanisa
#NIM    : J0403251014
#Kelas  : TPL A/P1
#=============================================

#=============================================
#Implementasi Dasar: Node pada Linked List
#=============================================

class Node:
    #konstruktor yang dijalankan secara otomatis ketika kelas Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data
        self.next = None 

#1) membuat node dengan instantiasi class node
nodeA = Node("A")       
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal : menelusuri node dari head sampai none
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
