"""

"""

class Queue():
    def __init__(self):
        self._elements = []

    def push(self, x):
        self._elements.insert(x, 0)
    
    def pop(self):
        if len(self._elements) != 0:
            self._elements.pop(0)