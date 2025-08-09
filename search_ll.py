class Node:
    def __init__(self, data): self.data = data; self.next = None
def search(head, key):
    while head:
        if head.data == key:
            return True
        head = head.next
    return False
head = Node(10)
head.next = Node(20)
head.next.next=Node(30)
print("Found" if search(head, 20) else "Not Found")
