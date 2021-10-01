from LinkedList import LinkedList
from MyClassError import MyClassError


def menu():
    while True:
        try:
            action = int(input("===============================================\n" +
                               "1.  Print LinkedList\n" +
                               "2.  Enter items from the keyboard\n" +
                               "3.  Add random elements in the interval [A-B]\n" + 
                               "4.  Add an item by index\n" +
                               "5.  Delete the item by index\n" +
                               "6.  Сyclically move the list by K positions\n" + 
                               "7.  Exit\n" + 
                               "===============================================\n"))
            break
        except ValueError:
            print("Must be INT")
            continue
    return action
    

def print_linkedList(linkedList):
    print(linkedList)


def enter_items_from_keyboard(linkedList):
    n = int(input("How many items do you want to add? "))
    linkedList.enter_from_the_keyboard(n)


def add_random_elements(linkedList):
    n = int(input("How many items do you want to add? "))
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    linkedList.fill_the_list_randomly(n, A, B)


def add_an_item_by_index(linkedList):
    item = input("Enter item: ")
    index = int(input("Enter index: "))
    linkedList.insert(index, item)


def delete_the_item_by_index(linkedList):
    index = int(input("Enter index: "))
    linkedList.del_elem_by_index(index)


def cyclically_move_by_K_positions(linkedList):
    K = int(input("How many items do you want to move the list to? "))
    linkedList.cyclic_shift_by_K_positions(K)


def main():
    linkedList = LinkedList()
    
    dictionary_of_actions = {1 : print_linkedList, 2 : enter_items_from_keyboard, 3 : add_random_elements,
                             4 : add_an_item_by_index, 5 : delete_the_item_by_index, 6 : cyclically_move_by_K_positions, 7 : exit}

    while True:
        action = menu()
        try:
            dictionary_of_actions[action](linkedList)
        except (MyClassError, ValueError, KeyError) as message:
            print(str(message))


main()
