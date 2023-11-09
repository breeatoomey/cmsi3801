class StackNode:
    def __init__(self, value, minimum, next=None):
        self.value = value
        self.minimum = minimum
        self.next = next


class Stack:
    def __init__(self, top_value):
        self.top = StackNode(top_value, top_value)

    def push(self, value):
        new_node = StackNode(value, min(value, self.top.minimum))
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("stack is empty")
        else:
            top_value = self.top.value
            self.top = self.top.next
            return top_value

    def min(self):
        return self.top.minimum

    def __repr__(self):
        string_representation = ""
        current_node = self.top
        while current_node:
            string_representation += str(current_node.value) + (
                ", " if current_node.next else ""
            )
            current_node = current_node.next
        return string_representation


# Tests:
Stack = Stack(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)
print(f"min of {Stack} == {Stack.min()}")

print(f"Pop {Stack.pop()}")
print(f"Pop {Stack.pop()}")
print(Stack)

Stack.push(3)
Stack.push(-2)
Stack.push(-1)
print(f"min of {Stack} == {Stack.min()}")

print(f"Pop {Stack.pop()}")
print(f"min of {Stack} == {Stack.min()}")

print(f"Pop {Stack.pop()}")
print(f"min of {Stack} == {Stack.min()}")
