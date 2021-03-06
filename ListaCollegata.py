"""
    File name: LinkedList.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a list_! where each item maintains a reference to the next one
    and methods to check if the list_! is empty, print all items, get the first/last item,
    add a new item at the top/bottom, visualize the item at the top/bottom.
"""


class Record:

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class ListaCollegata:

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return (self.first == None)

    def getFirst(self):
        if self.first == None:
            return None
        else:
            return self.first.elem

    def getLast(self):
        if self.last == None:
            return None
        else:
            return self.last.elem

    def addAsLast(self, elem):
        rec = Record(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            self.last.next = rec
            self.last = rec

    def addAsFirst(self, elem):
        rec = Record(elem)
        if self.first == None:
            self.first = self.last = rec
        else:
            rec.next = self.first
            self.first = rec

    def popFirst(self):
        if self.first == None:
            return None
        else:
            res = self.first.elem
            self.first = self.first.next
            if self.first == None:
                self.last = None  # empty list_!
            return res

    # popLast e deleteRecord not efficient now

    def getFirstRecord(self):
        if self.first == None:
            return None
        else:
            return self.first

    def getLastRecord(self):
        if self.first == None:
            return None
        else:
            return self.last

    def printOrdered(self):
        if self.first == None:
            print("[]")
            return

        print("Elements in the collection (ordered):")
        s = "["
        current = self.first
        while current != None:
            if len(s) > 1:
                s += ", "
            s += str(current.elem)
            current = current.next
        s += "]"
        print(s)