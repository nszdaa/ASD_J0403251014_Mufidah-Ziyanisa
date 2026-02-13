class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan elemen ke circular linked list
    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        # Jika sudah ada elemen
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Mencari elemen dalam circular linked list
    def search(self, key):
        if not self.head:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break

        return False

    # Menampilkan isi list
    def display(self):
        if not self.head:
            print("(Tidak ada elemen)")
            return

        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

cll = CircularLinkedList()

data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if data_input.strip() == "":
    print("(Tidak ada elemen)")
else:
    elements = data_input.split(",")
    for item in elements:
        cll.append(int(item.strip()))

    key = int(input("Masukkan elemen yang ingin dicari: "))

    if cll.search(key):
        print(f"Elemen {key} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")
