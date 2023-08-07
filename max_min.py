from node import Node

class LinkedList:
    def __init__(self):
    self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def find_max_min(self):
        if self.head is None:
            return None, None

        current = self.head
        max_data = current.data
        min_data = current.data

        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data

#To print the Maximum and Minimum values in the linked list

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    
    linked_list = LinkedList()
    for data in data_list:
        linked_list.insert(data)

    print("Linked List:")
    linked_list.display()

    max_data, min_data = linked_list.find_max_min()
    print(f"Maximum data: {max_data}")
    print(f"Minimum data: {min_data}")