from keys import Key

class Inventory:
    def __init__(self):
        self.keys = []

    def add_key(self, key):
        self.keys.append(key)

    def count_keys(self):
        return len(self.keys)

    def __str__(self):
        return f"Inventory: {', '.join(str(key) for key in self.keys)}"