class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode
if __name__ == "__main__":
    head = None
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    print("Original List:", end=" ")
    printList(head)
    head = reverse(head)
    print("Reversed List:", end=" ")
    printList(head)
