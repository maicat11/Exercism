class Node(object):
    def __init__(self, value):
        self.value = value

    def value(self):
        return self.value

    def next(self):
        pass


class LinkedList(object):
    def __init__(self, values=[]):
        self.length = len(values)
        for val in values:
            self.push(val)

    def __len__(self):
        return self.length

    def head(self):
        if self.length == 0:
            raise EmptyListException('Empty list.')
        return self.head

    def push(self, value):
        self.head = Node(value)
        # pass

    def pop(self):
        pass

    def reversed(self):
        pass


class EmptyListException(Exception):
    pass
