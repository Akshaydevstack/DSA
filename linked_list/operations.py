
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    
class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node 
            return 
        
        current = self.head
        
        while current.next:
            current = current.next
            
        current.next = new_node
    
    def insert_at_position(self,data,position):
        new_node = Node(data)
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        
        for _ in range(position-1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self,position):
        
        if self.head is None:
            return 
        
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        
        for _ in range(position-1):
            if current.next is None:
                return
            
            current = current.next
        
        if current and current.next is None:
            return
        
        current.next = current.next.next
            
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data)
            
            current = current.next
        

ll = Linked_list()

ll.insert_at_end(9)
ll.insert_at_end(12)

ll.insert_at_position(2,0)
ll.insert_at_position(3,2)

ll.delete_at_position(2)

ll.display()
        