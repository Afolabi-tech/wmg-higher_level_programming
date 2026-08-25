#!/usr/bin/python3
"""Defines a Node and a SinglyLinkedList."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next Node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets/sets the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets/sets the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Returns a printable representation of the linked list."""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing).

        Args:
            value (int): The data of the new Node.
        """
        new_node = Node(value)
        
        """ Empty list and insertion at the head. """
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        
        """ Insertion at the middle. """
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
