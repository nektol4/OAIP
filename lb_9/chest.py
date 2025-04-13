class Chest:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []
        self.opened = False

    def open(self):
        if not self.opened:
            self.opened = True
            print("The chest is opened.")
        else:
            print("The chest is already opened.")

    def close(self):
        if self.opened:
            self.opened = False
            print("The chest is closed.")
        else:
            print("The chest is already closed.")

    def add_item(self, item):
        if not self.opened:
            print("The chest is closed. Open it to add an item.")
            return
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Item '{item}' added to the chest.")
        else:
            print("The chest is full, cannot add more items.")

    def remove_item(self, item):
        if not self.opened:
            print("The chest is closed. Open it to remove an item.")
            return
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' removed from the chest.")
        else:
            print(f"Item '{item}' not found in the chest.")

    def show_items(self):
        if not self.opened:
            print("The chest is closed. Open it to see the contents.")
            return
        if self.items:
            print("The chest contains the following items:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("The chest is empty.")

    def clear_chest(self):
        if not self.opened:
            print("The chest is closed. Open it to clear.")
            return
        self.items = []
        print("The chest has been cleared.")