class ShoppingList:
    def __init__(self, list_name, description):
        self.list_name = list_name
        self.description = description
        self.items = []
    def show_item():
        for i in range(0, len(self.items)):
            print(f"{i + 1} {self.items[i].item_name}")
