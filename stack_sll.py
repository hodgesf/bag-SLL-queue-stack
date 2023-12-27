# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT implementation of Stacks and Queues
# Due Date: 11/05/2023
# Description: Implementation of stack methods by using a linked list


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the top of the stack. It is implemented with O(1)
        runtime complexity.
        :param value: value to push
        :return: None
        """
        # Create a new node with the given value
        new_node = SLNode(value)

        # Set the next of the new node to the current head
        new_node.next = self._head

        # Update the head to the new node
        self._head = new_node

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value. If the stack is
        empty, the method raises a custom “StackException”. It is implemented with O(1)
        amortized runtime complexity.
        :param: None
        :returns: The value of the element that has been removed from the stack
        """
        if self.is_empty():
            raise StackException

        # Get the value of the current head node
        val = self._head.value

        # Update the head to the next node
        self._head = self._head.next

        return val

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it. If the
        stack is empty, the method raises a custom “StackException”. It is implemented
        with O(1) runtime complexity.
        :param: None
        :return: The value of the current head node in the stack
        """
        if self.is_empty():
            raise StackException

        # Get the value of the current head node
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
