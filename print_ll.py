class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
if __name__ == "__main__":
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    printLinkedList(head)
