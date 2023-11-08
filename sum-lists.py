import copy


class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def length(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    def pad_with_zeros(self, num_zeros):
        for _ in range(num_zeros):
            new_node = Node(0)
            new_node.next = self.head
            self.head = new_node

    def __repr__(self):
        string_representation = ""
        current_node = self.head
        while current_node:
            string_representation += str(current_node.data) + (
                " -> " if current_node.next else ""
            )
            current_node = current_node.next
        return string_representation


def reverse_list(head: Node) -> Node:
    previous_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


def sum_lists(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    result_list: LinkedList = LinkedList()
    result_head: Node = sum_numbers(list_1.head, list_2.head, 0)
    result_list.head = result_head
    return result_list


def sum_lists_forward(list_1: LinkedList, list_2: LinkedList) -> LinkedList:
    diff_length = abs(list_1.length() - list_2.length())
    list_1.pad_with_zeros(
        diff_length
    ) if list_1.length() < list_2.length() else list_2.pad_with_zeros(diff_length)

    reversed_list_1: Node = reverse_list(copy.deepcopy(list_1.head))
    reversed_list_2: Node = reverse_list(copy.deepcopy(list_2.head))

    result_list: LinkedList = LinkedList()

    result_head_reversed: Node = sum_numbers(reversed_list_1, reversed_list_2, 0)
    result_head: Node = reverse_list(result_head_reversed)

    result_list.head = result_head
    return result_list


def sum_numbers(list_1_head: Node, list_2_head: Node, carry: int) -> Node:
    if not list_1_head and not list_2_head and carry == 0:
        return None

    sum = carry
    if list_1_head:
        sum += list_1_head.data
        list_1_head = list_1_head.next
    if list_2_head:
        sum += list_2_head.data
        list_2_head = list_2_head.next

    result_node = Node(sum % 10)
    carry = sum // 10

    result_node.next = sum_numbers(list_1_head, list_2_head, carry)
    return result_node


print("--------------------------------------------")
print("              Reversed Order                ")
print("--------------------------------------------")
list_1: LinkedList = LinkedList()
[list_1.append(i) for i in [7, 1, 6]]

list_2: LinkedList = LinkedList()
[list_2.append(i) for i in [5, 9, 2]]

result_1: LinkedList = sum_lists(list_1, list_2)
print(f"({list_1}) + ({list_2}) = {result_1}")

print("--------------------------------------------")

list_3: LinkedList = LinkedList()
[list_3.append(i) for i in [1, 5, 9]]

list_4: LinkedList = LinkedList()
[list_4.append(i) for i in [2, 3, 6, 7]]

result_2: LinkedList = sum_lists(list_3, list_4)
print(f"({list_3}) + ({list_4}) = {result_2}")

print("--------------------------------------------")

list_5: LinkedList = LinkedList()
[list_5.append(i) for i in [9, 7, 8]]

list_6: LinkedList = LinkedList()
[list_6.append(i) for i in [6, 8, 5]]

result_3: LinkedList = sum_lists(list_5, list_6)
print(f"({list_5}) + ({list_6}) = {result_3}")

print("--------------------------------------------")
print("               Forward Order                ")
print("--------------------------------------------")

forward_list_1: LinkedList = LinkedList()
[forward_list_1.append(i) for i in [6, 1, 7]]

forward_list_2: LinkedList = LinkedList()
[forward_list_2.append(i) for i in [2, 9, 5]]

forward_result_1: LinkedList = sum_lists_forward(forward_list_1, forward_list_2)
print(f"({forward_list_1}) + ({forward_list_2}) = {forward_result_1}")

print("--------------------------------------------")

forward_list_3: LinkedList = LinkedList()
[forward_list_3.append(i) for i in [3, 7, 5, 8]]

forward_list_4: LinkedList = LinkedList()
[forward_list_4.append(i) for i in [2, 3]]

forward_result_2: LinkedList = sum_lists_forward(forward_list_3, forward_list_4)
print(f"({forward_list_3}) + ({forward_list_4}) = {forward_result_2}")

print("--------------------------------------------")

forward_list_5: LinkedList = LinkedList()
[forward_list_5.append(i) for i in [9, 9, 7, 7]]

forward_list_6: LinkedList = LinkedList()
[forward_list_6.append(i) for i in [9, 0]]

forward_result_3: LinkedList = sum_lists_forward(forward_list_5, forward_list_6)
print(f"({forward_list_5}) + ({forward_list_6}) = {forward_result_3}")
