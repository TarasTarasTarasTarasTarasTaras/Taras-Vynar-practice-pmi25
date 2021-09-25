from LinkedList import LinkedList


def menu() -> str:
    str_menu = input("  Enter 'random' if you want to fill the LinkedList with random values from A to B\n" +
                     "  Enter 'fill' if you want to fill the LinkedList yourself\n" +
                     "  Enter 'exit' if you want to exit\n")
    return str_menu
    

def main():
    while True:
        linkedList = LinkedList()
        number = 10; positions = 3; A = 5; B = 25;
        action = menu()
        if action == "exit":
            break
        elif action != "random" and action != "fill":
            print("\nPlease try again")
            continue
        else:
            if action == "fill":
                if linkedList.enter_from_the_keyboard(number) == False:       # якщо була помилка
                    continue
            elif action == "random":
                if linkedList.fill_the_list_randomly(number, A, B) == False:  # якщо була помилка
                    continue
               
        print("\n" + str(linkedList))
        if linkedList.cyclic_shift_by_K_positions(positions) == False:        # якщо була помилка
            continue

        print("\n Cyclically swifted LinkedList by " + str(positions) + " positions:")
        print(str(linkedList) + "\n")
         
        # main повинен був бути не більше 10 рядків, але розтягнув для читабельності.


main()




