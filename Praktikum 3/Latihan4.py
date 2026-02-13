class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan elemen di akhir
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Method untuk menggabungkan dua linked list
    def merge(self, list2):
        if not self.head:
            return list2.head

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head
        return self.head
    
list1 = SingleLinkedList()
list2 = SingleLinkedList()

# Input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1: ")

if data1.strip() != "":
    for item in data1.split(","):
        list1.append(int(item.strip()))

# Input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2: ")

if data2.strip() != "":
    for item in data2.split(","):
        list2.append(int(item.strip()))

print("\nLinked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

# Gabungkan
list1.merge(list2)

print("Linked List setelah digabungkan:", end=" ")
list1.display()
