class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def addTwoLists(first, second):
    res = None
    last = None
    carry = 0
    while first or second:
        a = first.data if first else 0
        b = second.data if second else 0
        s = carry + a + b
        carry = s // 10
        s = s % 10
        newNode = Node(s)
        if res is None:
            res = newNode
            last = res
        else:
            last.next = newNode
            last = newNode
        if first:
            first = first.next
        if second:
            second = second.next
    if carry > 0:
        last.next = Node(carry)
    return res
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()
if __name__ == "__main__":
    first = Node(2)
    first.next = Node(4)
    first.next.next = Node(3)
    second = Node(5)
    second.next = Node(6)
    second.next.next = Node(4)
    result = addTwoLists(first, second)
    print("Sum List:", end=" ")
    printList(result)
