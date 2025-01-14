class User:
    def __init__(self, key_name):
        self.key_name = key_name
        self.storage = []

    def __str__(self):
        return f"{self.key_name}"


    def add_storage(self, key):
        self.storage.append(key)
        print(f"You have gained 1 {key}")
    
    def clear_storage(self):
        self.storage = []
        print(f"Your key storage was cleared")

    def show_storage(self):
        if self.storage:
            print(f"This is your inventory of {self.key_name}: {self.storage}")
        else:
            print("Your inventory is empty.")


if __name__ == "__main__":
    inventory = User("Escape Keys")
    inventory.add_storage("Room 1 Key")
    inventory.add_storage("Room 2 Key")
    inventory.add_storage("Room 3 Key")
    inventory.show_storage()
    inventory.clear_storage()
    inventory.show_storage()