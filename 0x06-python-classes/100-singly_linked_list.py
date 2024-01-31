#!/usr/bin/python3
"""Singly linked list module
    Classes:
        Node: defines node of a singly linked list
        SinglyLinkedList: defines a singly linked list
"""


class Node:
    """Defines node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initiates private instance attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node atribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node attribute"""
        if not isinstance(value, Node) and not isinstance(value, None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines singly linked list"""
    def __init__(self):
        self.__head = None
        self.__first_node = None

    def __str__(self):
        """Prints data contained int the linked list"""
        data_str = ""

        while self.__head:
            data_str += self.__head.__data
            self.__head = self.__head.__next_node

    def sorted_insert(self, value):
        """Inserts a new node in a sorted manner"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        node_inserted = False
        new_node = Node(value)
        if self.__first_node:
            current_node = self.__first_node
            prev_node = None

            while current_node.__next_node:
                if current_node.__data >= value:
                    new_node.__next_node = current_node
                    if prev_node:
                        prev_node.__next_node = new_node
                        node_inserted = True
                    else:
                        self.__first_node = current_node
                    break

                prev_node = current_node
                current_node = current_node.__next_node

            if not node_inserted:
                if prev_node:
                    prev_node.__next_node = new_node
                else:
                    self.__head = new_node
                    if current_node:
                        self.__head.__next_node = current_node
