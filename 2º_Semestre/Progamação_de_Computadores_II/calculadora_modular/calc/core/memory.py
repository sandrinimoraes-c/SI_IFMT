
class Memory:
    def __init__(self):
        self.value = 0.0
        self.has_value = False

    def clear(self):
        self.value = 0.0
        self.has_value = False

    def add(self, x: float):
        self.value += x
        self.has_value = True

    def sub(self, x: float):
        self.value -= x
        self.has_value = True

    def recall(self):
        return self.value if self.has_value else 0.0

memory = Memory()
