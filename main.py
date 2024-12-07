class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def update(self, index, value):
        pass

    def remove(self, value):
        pass
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end = ' ')
            current = current.next

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.push(1)
    my_list.push(2)
    my_list.push(3)
    my_list.display()
