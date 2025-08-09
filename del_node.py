class Node:
    def __init__(self, data): self.data = data; self.next = None
def delete_node(head, value):
    if head and head.data == value:
        return head.next
    temp = head
    while temp and temp.next:
        if temp.next.data == value:
            temp.next = temp.next.next
            return head
        temp = temp.next
    return head
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("NULL")
head = Node(10)
head.next = Node(20)
head.next.next=Node(30)
head = delete_node(head, 10)
print_list(head)
