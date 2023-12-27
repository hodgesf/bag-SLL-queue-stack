# Name: Frank Hodges
# OSU Email: hodgesf@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Bag ADT and Dynamic Array
# Due Date: October 30th
# Description: This assignment consists of 2 parts.
# In the first part, there is an implementation of a Dynamic Array.
# Then in the second part, there is an implementation of a Bag ADT using the Dynamic Array from Part 1.

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag.
        :param value: value to be added to bag
        :return: None
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method adds a new element to the bag.
        :param value: value to be removed from bag
        :return: None
        """
        for items in range(self._da.length()):
            if self._da[items] == value:
                self._da.remove_at_index(items)
                return True
        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value
        object
        :param value: value to count occurence of
        :return: count of value specified
        """
        count = 0
        for num in range(self._da.length()):
            if self._da[num] == value:
                # everytime that value is encountered, increase the count
                count += 1
        return count

    def clear(self) -> None:
        """
        This method clears the contents of the bag
        :param: None
        :return: None
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method compares the contents of a bag with the contents of a second bag provided as
        a parameter. The method returns True if the bags are equal (contain the same number of
        elements, and also contain the same elements without regard to the order of elements).
        Otherwise, it returns False.
        :param second_bag: bag to compare to original bag
        :return: boolean value of true or false depending on evaluation
        """

        if self._da.length() != second_bag._da.length():  # if they aren't the same length
            return False

        for items in range(0, self._da.length()):
            compare = self._da.get_at_index(items)
            if self.count(compare) != second_bag.count(compare):
                # if the count of an item isn't equal to the count of same item in second bag
                return False
        return True

    def __iter__(self):
        """
        This method enables the Bag to iterate across itself.
        ***This implementation is modeled after the example in the exploration.***
        """
        self._index = 0

        return self

    def __next__(self):
        """
        This method will return the next item in the Bag, based on the current location of the
        iterator.

        ***This implementation is modeled after the example in the exploration.***
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
