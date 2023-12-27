# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT implementation of Stacks and Queues
# Due Date: 11/05/2023
# Description: Implementation of stack methods by using a dynamic array


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        This method adds a new element to the end of the list. It is implemented with amortized O(1) runtime complexity.
        :param value: value to push
        :return: None
        """
        # Append the new value to the end of the dynamic array
        self._da.append(value)

    def pop(self) -> object:
        """
        This method removes the top element from the stack and returns its value. If the stack is
        empty, the method raises a custom “StackException”. It is implemented with O(1)
        amortized runtime complexity.
        :param: None
        :returns: The value of the element that has been removed from the stack
        """
        if self.is_empty():
            raise StackException()

        # Get the size of the stack and the value of the last element
        size = self.size() - 1
        last_element = self._da[size]

        # Remove the last element from the dynamic array
        self._da.remove_at_index(size)

        return last_element

    def top(self) -> object:
        """
        This method returns the value of the top element of the stack without removing it. If the
        stack is empty, the method raises a custom “StackException”. It is implemented
        with O(1) runtime complexity.
        :param: None
        :return: The value of the last item in the stack
        """
        if self.is_empty():
            raise StackException()

        # Get the size of the stack and the value of the last element
        size = self.size() - 1
        last_element = self._da[size]

        return last_element


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
