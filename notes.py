# Safira Nur Fauziah

"""Notes Schedule Sederhana Menggunakan Linked List"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    # Menambah data
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Mencari data  
    def search(self, x): 
 
        current = self.head
        count = 0 
   
        while current != None: 
            if current.data == x: 
                return ("Schedule ditemukan pada posisi:", count) 

            count = count + 1  
            current = current.next
          
        return False
    
    # Menghapus data
    def delete(self, key):  
          
        temp = self.head  
    
        if (temp is not None):  
            if (temp.data == key):  
                self.head = temp.next
                temp = None
                return
    
        while(temp is not None):  
            if temp.data == key:  
                break
            prev = temp  
            temp = temp.next
    
        if(temp == None):  
            return
    
        prev.next = temp.next
        temp = None

    # Melihat data yang sudah diinputkan
    def output(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            current_node = current_node.next


def main():
    Linklist = LinkedList() 

    data = int(input("Jumlah schedule yang ingin dimasukkan: "))
    for x in range (data):
        awal = str(input("Masukkan schedule: "))
        Linklist.add(awal)

    print()
    print("List schedule: ")
    Linklist.output()

    print()
    cari = str(input("Masukkan schedule yang ingin dicari: "))
    print(Linklist.search(cari))

    hapus = str(input("Apakah anda ingin menghapus data ( {} ) ? (Ketik Yes/No) " .format(cari)))

    if hapus == "Yes":
        Linklist.delete(cari)
        print()
        print("Schedule telah dihapus!")
        print()
        print("List schedule: ")
        print(Linklist.output())
    else:
        print("Perintah dibatalkan")

if __name__ == "__main__":
    main()