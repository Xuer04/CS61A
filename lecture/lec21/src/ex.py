class List(object):

    """Docstring for List. """

    def __init__(self, length, element=None):
        self.length = length
        if element is None:
            self.element = []
        else:
            self.element = element

    def add(self, value):
        self.element.append(value)
        self.length += 1

    def delete(self, value):
        assert value in self.element, "the value isn't in the list."
        self.element.remove(value)
        self.length -= 1

