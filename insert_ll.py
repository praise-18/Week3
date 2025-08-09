class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
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
        head = insert_end(head, val)
    display(head)
