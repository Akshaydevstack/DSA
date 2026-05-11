class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    

head = Node(10)
node2 = Node(20)
node3 = Node(30)

head.next=node2
node2.prev = head
node2.next = node3
node3.prev = node2


head = node2.prev

print(head.data)