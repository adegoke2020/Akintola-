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

#To convert the single linked list into a binary search tree

    def list_to_bst(self, data_list):
        data_list.sort()
        return self._list_to_bst(data_list, 0, len(data_list) - 1)

    def _list_to_bst(self, data_list, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        new_node = Node(data_list[mid])
        
        new_node.left = self._list_to_bst(data_list, start, mid - 1)
        new_node.right = self._list_to_bst(data_list, mid + 1, end)

        return new_node

#To test the Binary Search Tree

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    
    linked_list = LinkedList()
    for data in data_list:
        linked_list.insert(data)

    print("Linked List:")
    linked_list.display()

    bst_root = linked_list.list_to_bst(data_list)
    print("\nBinary Search Tree Inorder Traversal:")
    linked_list.inorder_bst_traversal(bst_root)
