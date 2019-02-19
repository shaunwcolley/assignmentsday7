
lists = []
user_input = ""

from grocery_item import GroceryItem
from shopping_list import ShoppingList


def add_list():
    list = ShoppingList(input("Please enter name of list (store name):\n>> "), input("Please describe list (why this store?):\n>> "))
    lists.append(list)

def show_lists():
    for i in range(0, len(lists)):
        print(f"{i + 1} {lists[i].list_name}")

def view_all_lists():
    for i in range(0, len(lists)):
        print(f"{lists[i].list_name} - {lists[i].description}")
        print("-----------------------------")
        for item in lists[i].items:
            print(f"{item.item_name} - {item.quantity}")
        print("\n")

def add_item():
    a = True
    while a == True:
        try:
            show_lists()
            list_add = int(input("Please enter list number:\n>> "))
            if list_add - 1 not in range(0, len(lists)):
                print("Please enter appropriate list number.")
            else:
                item = GroceryItem(input("Item name:\n>> "), input("How many:\n>> "))
                lists[list_add - 1].items.append(item)
                print(f"{item.quantity} {item.item_name} added to {lists[list_add - 1].list_name}")
                a = False
        except ValueError:
            print("Did you really only enter a list number?")
        except:
            print("Something really bad has happened, please try again. If it does not work, quit the app and try again.")

def del_list():
    show_lists()
    a = True
    while a == True:
        try:
            list_del = int(input("Please enter list number:\n>> "))
            if list_del <= len(lists):
                del lists[(list_del - 1)]
                a = False
            else:
                print(f"Please give a number up to {str(len(lists))}, thank you!")
        except ValueError:
            print("Are you trying to make the coder do more work? Please ONLY enter a number!")
        except:
            print("Something really bad has happened, please try again. If it does not work, quit the app and try again.")



def show_menu():
    print("Please enter the following:")
    print("1 to create a new list")
    print("2 to add new item to list")
    print("3 to delete list")
    print("4 to view all lists")
    print("q to quit")


while user_input != "q":
    show_menu()
    user_input = input(">> ")
    if user_input == "1":
        add_list()
    elif user_input == "2":
        add_item()
    elif user_input == "3":
        del_list()
    elif user_input == "4":
        view_all_lists()
    elif user_input != "q":
        print("Please Enter Valid Input")
