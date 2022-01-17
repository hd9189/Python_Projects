# _ indicates that the function is private, but could still access
class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __int__(self, name):
        self.name = name
        self.priv = _Private(name)

    # _ indicates that the function is private, but could still access
    def _display(self):
        print('Hello')

    def display(self):
        print('Hi')

a = NotPrivate()
a.display()