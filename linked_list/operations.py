class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_beging(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_node
        
    def display_all(self):
        current = self.head

        while current:
            print(current.data)

            current = current.next


ll = Linked_list()

ll.insert_at_end(12)
ll.insert_at_end(21)
ll.insert_at_end(11)
ll.insert_at_end(22)

ll.display_all()