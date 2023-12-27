# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT implementation of Stacks and Queues
# Due Date: 11/05/2023
# Description: Implementation of a singly linked list methods


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        This method adds a new node at the beginning of the list (right after the front sentinel). It
        is implemented with O(1) runtime complexity.
        :param value: value to be inserted
        :return: None
        """
        # Create a new node with the given value and set its next pointer to the current first node
        new_node = SLNode(value, self._head.next)

        # Update the front sentinel's next pointer to the new node
        self._head.next = new_node

    def insert_back(self, value: object) -> None:
        """
        This method adds a new node at the end of the list. It is implemented with O(N)
        runtime complexity.
        :param value: value to be inserted
        :return: None
        """
        # Create a new node with the given value and set its next pointer to None
        new_node = SLNode(value, None)

        # If the list is empty, set the head to the new node and return
        if self._head is None:
            self._head = new_node
            return

        # Otherwise, traverse the list to find the last node and set its next pointer to the new node
        node = self._head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method inserts a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”. If the
        linked list contains N nodes (the sentinel node is not included in this count), valid indices for
        this method are [0, N] inclusive. It is implemented with O(N) runtime complexity.
        :param index: index of node to be input
        :param value: value to input at given index
        :return: None
        """
        if index < 0:
            raise SLLException()

        new_node = SLNode(value)

        if index == 0:
            # Insert at the front of the list (right after the front sentinel)
            self.insert_front(value)
            return

        node = self._head
        count = 0

        while count < index and node.next is not None:
            node = node.next
            count += 1

        if index - 1 == count:
            raise SLLException()

        # Insert the new node at the specified index
        new_node.next = node.next
        node.next = new_node

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the node at the specified index position from the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”. If the list
        contains N elements (the sentinel node is not included in this count), valid indices for this
        method are [0, N - 1] inclusive. It is implemented with O(N) runtime complexity.
        :param index: index of node to be removed
        :return: None
        """
        if index < 0:
            raise SLLException()

        if index == 0:
            # If the index is 0, remove the node right after the front sentinel
            if self._head.next is not None:
                self._head.next = self._head.next.next
            else:
                raise SLLException()
        else:
            node = self._head
            count = 0
            size = self.length()

            if index >= size:
                raise SLLException()

            while count < size - 1:
                node = node.next
                count += 1
                if count == index:
                    node.next = node.next.next

    def remove(self, value: object) -> bool:
        """
        This method traverses the list from the beginning to the end, and removes the first node
        that matches the provided value. The method returns True if a node was removed from the
        list. Otherwise, it returns False. It is implemented with O(N) runtime complexity.
        :param value: value to be removed
        :return: True if a node with the specified value is removed, False otherwise
        """
        node = self._head
        size = self.length()
        count = 0
        while count <= size - 1:
            if node.next.value == value:
                node.next = node.next.next
                return True
            node = node.next
            count += 1
        return False

    def count(self, value: object) -> int:
        """
        This method counts the number of elements in the list that match the provided value. The
        method then returns this number. It is implemented with O(N) runtime complexity.
        :param value: value to compose count for
        :return: number of occurrences of the specified value in the list
        """
        count = 0
        index = 0
        node = self._head
        size = self.length()
        while index < size + 1:
            if node.value == value:
                count += 1
            index += 1
            node = node.next
        return count

    def find(self, value: object) -> bool:
        """
        This method returns a Boolean value based on whether or not the provided value exists in
        the list. It is implemented with O(N) runtime complexity.
        :param value: value to evaluate if it is in the list or not
        :return: True if the specified value is found in the list, False otherwise
        """
        index = 0
        node = self._head
        size = self.length()
        while index < size + 1:
            if node.value == value:
                return True
            index += 1
            node = node.next
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        This method returns a new LinkedList that contains the requested number of nodes from the
        original list, starting with the node located at the requested start index. If the original list
        contains N nodes, a valid start_index is in the range [0, N - 1] inclusive. The original list
        cannot be modified. The runtime complexity of your implementation is O(N).
        :param start_index: index from which to start the slice
        :param size: number of nodes to include in the slice
        :return: a new LinkedList containing the specified slice
        """
        if start_index < 0 or size < 0:
            raise SLLException()

        list_length = self.length()
        if start_index >= list_length or (start_index + size) > list_length:
            raise SLLException()

        new_list = LinkedList()
        current_node = self._head.next  # Start from the first node (skip the sentinel node)
        index = 0

        if self.length() == 0:
            raise SLLException()

        # Move to the node at the specified start_index
        while current_node is not None and index < start_index:
            current_node = current_node.next
            index += 1

        # Copy the next "size" nodes from the original list to the new list
        count = 0
        while count < size:
            new_list.insert_back(current_node.value)
            current_node = current_node.next
            count += 1

        return new_list


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
