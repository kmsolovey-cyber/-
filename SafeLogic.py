import random

class SafeLogic:
    def __init__(self):
        self.secret = [random.randint(0, 9) for _ in range(3)]
        print("Секретный код:", self.secret)

    def check(self, digits):
        if digits == self.secret:
            return (0, 255, 0)  # зелёный
        return (255, 0, 0)      # красный
