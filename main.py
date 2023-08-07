# main.py to test the code

from LinkedList import LinkedList

if __name__ == "__main__":
    data_list = [1, 3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    
    linked_list = LinkedList()
    for data in data_list:
        linked_list.insert(data)

    print("Linked List:")
    linked_list.display()
