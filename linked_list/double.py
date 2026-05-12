class Node:

    def __init__(self, data):

        self.data = data

        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):

        self.head = None

    # Insert at End
    def insert_at_end(self, data):

        new_node = Node(data)

        # Empty list
        if self.head is None:

            self.head = new_node
            return

        current = self.head

        # Traverse till last node
        while current.next:

            current = current.next

        # Connect last node with new node
        current.next = new_node

        # Connect new node back to previous node
        new_node.prev = current

    # Insert at Position
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        # Traverse to previous position node
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        # Connect new node forward
        new_node.next = current.next
        # Connect new node backward
        new_node.prev = current
        # If node exists after current
        if current.next:
            current.next.prev = new_node

        # Connect current to new node
        current.next = new_node

    # Delete at Position
    def delete_at_position(self, position):

        if self.head is None:
            return

        # Delete head
        if position == 0:

            self.head = self.head.next

            if self.head:
                self.head.prev = None

            return

        current = self.head

        # Traverse to target node
        for _ in range(position):

            if current is None:
                return

            current = current.next

        if current is None:
            return

        # Connect previous node to next node
        current.prev.next = current.next

        # If next node exists
        if current.next:
            current.next.prev = current.prev

    # Forward Traversal
    def display_forward(self):

        current = self.head

        while current:

            print(current.data, end=" <-> ")

            current = current.next

        print("NULL")

    # Backward Traversal
    def display_backward(self):

        current = self.head

        if current is None:
            return

        # Move to last node
        while current.next:

            current = current.next

        # Traverse backward
        while current:

            print(current.data, end=" <-> ")

            current = current.prev

        print("NULL")


dll = DoublyLinkedList()

dll.insert_at_end(9)
dll.insert_at_end(12)

dll.insert_at_position(2, 0)
dll.insert_at_position(3, 2)

dll.delete_at_position(2)

print("Forward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()
