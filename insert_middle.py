class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_middle(head, data):
    if not head:
        return Node(data)
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    new_node = Node(data)
    new_node.next = slow
    prev.next = new_node
    return head
def display(head):
    temp = head
    while temp:
        print(temp.data, "->", end=" ")
        temp = temp.next
    print("NULL")
if __name__ == "__main__":
    head = None
    n = int(input("Enter number of elements: "))
    for _ in range(n):
        val = int(input("Enter value: "))
        node = Node(val)
        node.next = head
        head = node
    head = insert_middle(head, 99)
    display(head)
