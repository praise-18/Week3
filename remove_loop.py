class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node
def removeLoop(loop_node, head):
    ptr1 = head
    while True:
        ptr2 = loop_node
        while ptr2.next != loop_node and ptr2.next != ptr1:
            ptr2 = ptr2.next
        if ptr2.next == ptr1:
            break
        ptr1 = ptr1.next
    ptr2.next = None
def detectAndRemoveLoop(head):
    slow = head
    fast = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            removeLoop(slow, head)
            return
def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("NULL")
head = None
head = push(head, 20)
head = push(head, 4)
head = push(head, 15)
head = push(head, 10)
head.next.next.next.next = head.next  # create loop
detectAndRemoveLoop(head)
printList(head)
