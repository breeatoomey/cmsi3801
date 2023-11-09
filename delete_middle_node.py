class LinkedListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, items: list):
        self.head = None
        [self.append(item) for item in items]

    def append(self, data):
        node = LinkedListNode(data)
        if not self.head:
            self.head = node
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next
            temp_node.next = node

    def __repr__(self):
        s = ""
        temp = self.head
        while temp:
            s += str(temp.data) + "->"
            temp = temp.next
        return s + "|"


def delete_middle_node(node: LinkedListNode) -> None:
    node.data = node.next.data
    node.next = node.next.next


l1 = LinkedList(list("abcdef"))
node_c = l1.head.next.next
print("            ", l1)
delete_middle_node(node_c)
print("deleting c: ", l1)

print("----------------------------------")

l2 = LinkedList(list("abcdefghijk"))
node_b = l2.head.next
print("            ", l2)
delete_middle_node(node_b)
print("deleting b: ", l2)

print("----------------------------------")

l3 = LinkedList([1, 2, 3, 4, 5, 6, 7])
node_6 = l3.head.next.next.next.next.next
print("            ", l3)
delete_middle_node(node_6)
print("deleting 6: ", l3)
