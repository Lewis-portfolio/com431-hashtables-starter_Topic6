# Lewis
# Date: 05, 11, 2025
# Hash table:
from linkedlist import TuplesLinkedList

class HashTable():
    """ A hash table. """
    def __init__(self):
        self.buckets = [TuplesLinkedList() for i in range(17)]


    def hash(self, key):
        """ Adds the calculation of the letters in a string. """
        value = 0
        for letter in key:
            value += ord(letter)
        return value % 17


    def put(self, key, value):
        """ Puts a value in the linked list of the specified bucket. """
        bucket = self.hash(key)
        self.buckets[bucket].add(key, value)

    def get(self, key):
        """ Gets the requested value in the linked list of a specified bucket. """
        bucket = self.hash(key)
        self.buckets[bucket].find(key)
