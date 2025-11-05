# Lewis
# Date: 05, 11, 2025
# Hash table:
from linkedlist import TuplesLinkedList

class HashTable():
    """ A hash table. """
    def __init__(self):
        self.buckets = [TuplesLinkedList() for i in range(31)]


    def hash(self, key):
        """ Adds the calculation of the letters in a string. """
        value = 0
        factor = 31
        power = 0
        for letter in key:
            value += (ord(letter) * factor**power)
            power += 1
        return value


    def put(self, key, value):
        """ Puts a value in the linked list of the specified bucket. """
        bucket = self.hash(key) % len(self.buckets)
        self.buckets[bucket].add(key, value)

    def get(self, key):
        """ Gets the requested value in the linked list of a specified bucket. """
        bucket = self.hash(key) % len(self.buckets)
        return self.buckets[bucket].find(key)
