import random

def input_array(arr):
    print("Input " + str(len(arr)) + " values: ")
    for i in range(len(arr)):
        arr[i] = enter_validated_number("Arr[" + str(i) + "] = ", "array element")

        
def input_random_from_A_to_B(arr, A, B):
    for i in range(len(arr)):
        arr[i] = random.randint(A,B)


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')


def add_operations(dictionaryCounters, assignment, incremental, comparative):
    dictionaryCounters['assignment_counters'] += assignment
    dictionaryCounters['incremental_counters'] += incremental
    dictionaryCounters['comparative_counters'] += comparative


def Merge(array, begin, end, dictionaryCounters):
    dictionaryCounters['recursive_counters'] += 1
    
    mid = begin + (end - begin) // 2
    i = begin; j = mid + 1; temp_arr = []; 

    dictionaryCounters['comparative_counters'] += 2
    while(i <= mid and j <= end): 
        if(array[i] <= array[j]):
            temp_arr.append(array[i])
            i+=1
        else: 
            temp_arr.append(array[j])
            j+=1
        add_operations(dictionaryCounters, 1, 1, 3)

    dictionaryCounters['comparative_counters'] += 1
    while(i<=mid):
        temp_arr.append(array[i])
        i+=1
        add_operations(dictionaryCounters, 1, 1, 1)

    dictionaryCounters['comparative_counters'] += 1
    while(j<=end):
        temp_arr.append(array[j])
        j+=1
        add_operations(dictionaryCounters, 1, 1, 1)

    for m in range(len(temp_arr)):
        array[begin+m] = temp_arr[m]
        add_operations(dictionaryCounters, 1, 1, 1)


def MergeSort(array, left, right, dictionaryCounters):
    dictionaryCounters['recursive_counters'] += 1
    dictionaryCounters['comparative_counters'] += 1
    if(left < right):
        MergeSort(array, left, left + (right - left) // 2, dictionaryCounters)
        MergeSort(array, left + (right - left) // 2 + 1, right, dictionaryCounters)
        Merge(array, left, right, dictionaryCounters)


def enter_validated_number(string, key):
    try:
        number = int(input(string))
        if key == "size" and number < 1:
            raise SyntaxError
        return number
    except ValueError:
        raise ValueError("  ERROR: " + key + " must be INT\n")
    except SyntaxError:
        raise ValueError("  ERROR: size must be greater than 0\n")


def menu():
    while True:
        dictionaryCounters = dict.fromkeys(['recursive_counters', 'assignment_counters', 'incremental_counters', 'comparative_counters'], 0)

        str_menu = input("  Enter 'random' if you want to fill the array with random values from A to B\n" +
                         "  Enter 'fill' if you want to fill the array yourself\n" +
                         "  Enter 'exit' if you want to exit\n")

        if str_menu == "exit": 
            break
        elif str_menu != "fill" and str_menu != "random":
            print("\nPlease try again\n")
            continue
        else:
            try:
                n = enter_validated_number("Enter size: ", "size")
                arr = [0 for i in range(n)]
                if str_menu == "fill": 
                    input_array(arr)
                else:
                   A = enter_validated_number("Enter A: ", "board")
                   B = enter_validated_number("Enter B: ", "board")
                   if A > B:
                       A=A+B
                       B=A-B
                       A=A-B
                   input_random_from_A_to_B(arr, A, B)
            except ValueError as message:
                    print(str(message))
                    continue
                

        print("\nArray: ")
        print_array(arr)

        MergeSort(arr, 0, n-1, dictionaryCounters)

        print("\n\nSorted array: ")
        print_array(arr)

        print("\n\n" + str(dictionaryCounters))
        counters = 0
        for key in dictionaryCounters:
            counters += dictionaryCounters[key]

        print("\nOperations performed: " + str(counters) + '\n' + '='*30 + '\n')


menu()
