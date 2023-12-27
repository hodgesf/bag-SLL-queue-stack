# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Linked List and ADT implementation of Stacks and Queues
# Due Date: 11/05/2023
# Description: Implementation of queue methods by using a linked list


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
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
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        This method adds a new value to the end of the queue. It is implemented with O(1)
        runtime complexity.
        :param value: value to add
        :return: None
        """
        # Create a new node with the given value
        new_node = SLNode(value)

        # If the queue is empty, set both head and tail to the new node
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            # If the queue is not empty, update the current tail's next pointer to the new node
            self._tail.next = new_node
            # Update the tail pointer to the new node
            self._tail = new_node

    def dequeue(self) -> object:
        """
        This method removes and returns the value from the beginning of the queue. If the queue is
        empty, the method raises a custom “QueueException”. It is implemented with O(1)
        runtime complexity.
        :return: Element removed from the front of the queue
        """
        # Check if the queue is empty and raise an exception if so
        if self.is_empty():
            raise QueueException()

        # Retrieve the value from the head node
        val = self._head.value

        # Update the head pointer to the next node in the queue
        self._head = self._head.next

        return val

    def front(self) -> object:
        """
        This method returns the value of the front element of the queue without removing it. If the
        queue is empty, the method raises a custom “QueueException”. It is implemented
        with O(1) runtime complexity.
        :return: Value of the front element
        """
        # Check if the queue is empty and raise an exception if so
        if self.is_empty():
            raise QueueException()

        # Return the value of the head node
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
