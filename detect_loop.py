class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node
def detectLoop(h):
    slow = h
    fast = h
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
head = None
head = push(head, 20)
head = push(head, 4)
head = push(head, 15)
head = push(head, 10)
head.next.next.next.next = head  # create loop
print("Loop detected" if detectLoop(head) else "No loop")
