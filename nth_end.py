class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node
def getNthFromEnd(head, n):
    main_ptr = head
    ref_ptr = head
    count = 0
    while count < n:
        if ref_ptr is None:
            return -1
        ref_ptr = ref_ptr.next
        count += 1
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    return main_ptr.data
head = None
head = push(head, 20)
head = push(head, 4)
head = push(head, 15)
head = push(head, 35)
n = 2
print("Nth node from end is", getNthFromEnd(head, n))
