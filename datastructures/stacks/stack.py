"""Implementation of Stack using List DataType in Python"""

class Stack:
    """Stack Class
    Consists of 2 Methods:
        - push(element): Pushes Element into Stack
        - pop(element): Pops Element from Stack
    """
    def __init__(self) -> None:
        self.stack = []
        self.num_elements = 0

    def __is_empty(self) -> bool:
        return self.stack is None

    def push(self, element: int) -> None:
        """Push Operation: Pushing an element into the stack"""
        if self.__is_empty() is False and isinstance(element, int):
            self.stack.append(element)
            self.num_elements+=1
            print(f"Element {element} push to stack at position: {len(self.stack)-1}")
        else:
            raise ValueError("This stack only allows integer values")

    def pop(self) -> int:
        """Pop Operation: Popping the element pushed into the stack"""
        if self.__is_empty() is False:
            self.num_elements -= 1
            return self.stack.pop()

        else:
            print("Stack is Empty...!!!")

    def display_stack(self) -> list:
        """Display Operation: Shows current Elements in the stack"""
        return self.stack[::-1]


def main():
    """Main() Method"""

    stack_basic = Stack()
    stack_basic.push(1)
    stack_basic.push(2)
    print(f"Number of Elements in Stack: {stack_basic.num_elements}")
    element_popped = stack_basic.pop()
    print(f"Element popped from stack: {element_popped}")
    stack_basic.push(3)
    stack_basic.push(4)
    stack_basic.push(5)
    element_popped = stack_basic.pop()
    print(f"Element popped from stack: {element_popped}")
    print(f"Current Stack: {stack_basic.display_stack()}")

if __name__ == '__main__':
    main()
