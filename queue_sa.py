# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT implementation of Stacks and Queues
# Due Date: 11/05/2023
# Description: Implementation of queue methods by using a static array


# Note: Changing any part of the pre-implemented methods (besides adding  #
#       default parameters) will cause the Gradescope tests to fail.      #


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class.
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True if the queue is empty, False otherwise.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def print_underlying_sa(self) -> None:
        """
        Print underlying StaticArray. Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(self._sa)

    def _increment(self, index: int) -> int:
        """
        Move index to next position.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # ---------------------------------------------------------------------- #

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue. It is implemented with O(1)
        amortized runtime complexity.
        :param value: value to add
        :return: none
        """
        # Check if the queue is full, and if so, double its capacity
        if self._current_size == self._sa.length():
            self._double_queue()

        # Update the back pointer to the next available position and store the value
        self._back = self._increment(self._back)
        self._sa[self._back] = value
        self._current_size += 1

    def dequeue(self) -> object:
        """
        This method removes and returns the value at the beginning of the queue. If the queue is
        empty, the method raises a custom “QueueException”. It must be implemented with O(1)
        runtime complexity.
        :param: none
        :return: element removed
        """
        # Check if the queue is empty and raise an exception if so
        if self.is_empty():
            raise QueueException()

        # Retrieve the element at the front, update the front pointer, and decrease the size
        element = self._sa[self._front]
        self._front = self._increment(self._front)
        self._current_size -= 1

        return element

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it. If the
        queue is empty, the method raises a custom “QueueException”. It is implemented
        with O(1) runtime complexity
        """
        # Check if the queue is empty and raise an exception if so
        if self.is_empty():
            raise QueueException("Queue is empty")

        # Return the element at the front
        return self._sa[self._front]

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        Double the capacity of the underlying static array.
        """
        # Calculate the new capacity and create a new array
        new_capacity = self._sa.length() * 2
        new_array = StaticArray(new_capacity)

        new_front = 0
        new_back = 0

        # Copy elements from the current array to the new array
        for i in range(self._current_size):
            new_array[new_back] = self._sa[self._front]
            new_front = new_back
            new_back += 1
            self._front = self._increment(self._front)

        # Update the Queue's attributes to reflect the new array
        self._sa = new_array
        self._front = 0
        self._back = new_back - 1


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# Basic functionality tests #")
    print("\n# enqueue()")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue()")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for _ in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)
    q.print_underlying_sa()

    print("\n# front()")
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)

    print("\n# Circular buffer tests: #\n")

    def action_and_print(
            header: str, action: callable, values: [], queue: Queue) -> None:
        """
        Print header, perform action,
        then print queue and its underlying storage.
        """
        print(header)
        if values:
            for value in values:
                action(value)
        else:
            action()
        print(queue)
        queue.print_underlying_sa()
        print()

    q = Queue()

    # action_and_print("# Enqueue: 2, 4, 6, 8", q.enqueue, [2, 4, 6, 8], q)

    # Calling the action_and_print() function declared two lines above,
    # would be equivalent to following lines of code:
    print("# Enqueue: 2, 4, 6, 8")
    test_case = [2, 4, 6, 8]
    for value in test_case:
        q.enqueue(value)
    print(q)
    q.print_underlying_sa()
    print()

    action_and_print("# Dequeue a value", q.dequeue, [], q)
    action_and_print("# Enqueue: 10", q.enqueue, [10], q)
    action_and_print("# Enqueue: 12", q.enqueue, [12], q)

    print("# Dequeue until empty")
    while not q.is_empty():
        q.dequeue()
    print(q)
    q.print_underlying_sa()
    print()

    action_and_print("# Enqueue: 14, 16, 18", q.enqueue, [14, 16, 18], q)
    action_and_print("# Enqueue: 20", q.enqueue, [20], q)
    action_and_print("# Enqueue: 22, 24, 26, 28", q.enqueue,
                     [22, 24, 26, 28], q)
    action_and_print("# Enqueue: 30", q.enqueue, [30], q)
