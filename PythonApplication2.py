import random

def input_array(arr, n):
    print("Input " + str(n) + " values: ")
    for i in range(n):
        arr[i] = int(input())
        
def input_random_from_A_to_B(arr, n):
    A = int(input(" Input A: "))
    B = int(input(" Input B: "))
    for i in range(n):
        arr[i] = random.randint(A,B)

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')

def Merge(array, begin, end):
    global recursive_counter
    global comparative_counter
    global assignment_counter
    global incremental_counter

    mid = begin + (end - begin) // 2
    i = begin; j = mid + 1; temp_arr = []; 

    comparative_counter += 2      # 2 порівняння
    while(i <= mid and j <= end): 
        if(array[i] <= array[j]):
            temp_arr.append(array[i])
            i+=1
        else: 
            temp_arr.append(array[j])
            j+=1
        assignment_counter += 1   # 1 присвоєння
        comparative_counter += 3  # 3 порівняння
        incremental_counter += 1  # 1 інкремент

    comparative_counter += 1      # 1 порівняння
    while(i<=mid):
        temp_arr.append(array[i])
        i+=1
        assignment_counter += 1   # 1 присвоєння
        comparative_counter += 1  # 1 порівняння
        incremental_counter += 1  # 1 інкремент

    comparative_counter += 1      # 1 порівняння
    while(j<=end):
        temp_arr.append(array[j])
        j+=1
        assignment_counter += 1   # 1 присвоєння
        comparative_counter += 1  # 1 порівняння
        incremental_counter += 1  # 1 інкремент

    for m in range(len(temp_arr)):
        array[begin+m] = temp_arr[m]
        assignment_counter += 1   # 1 присвоєння
        comparative_counter += 1  # 1 порівняння
        incremental_counter += 1  # 1 інкремент


def MergeSort(array, left, right):
    global recursive_counter
    global comparative_counter

    recursive_counter += 1        # 1 рекурсивний виклик
    comparative_counter += 1      # 1 порівняння
    if(left < right):
        MergeSort(array, left, left + (right - left) // 2)
        MergeSort(array, left + (right - left) // 2 + 1, right)
        Merge(array, left, right)


while True:
    try:
        recursive_counter = 0
        assignment_counter = 0
        incremental_counter = 0
        comparative_counter = 0

        int_menu = int(input("  Enter '1' if you want to fill the array yourself\n" +
                             "  Enter '2' if you want to fill the array with random values from A to B\n" +
                             "  Enter '3' if you want to exit\n"))

        if int_menu == 3: break
        elif int_menu < 1 or int_menu > 3:
            print("\nPlease try again\n")
            continue
        else:
            n = 0
            while(n <= 0): 
                n = int(input("\nInput the size of the array (should be > 0) "))
                continue
            arr = [0 for i in range(n)]
            if int_menu == 1: input_array(arr, n)
            else: input_random_from_A_to_B(arr, n)

        print("\nArray: ")
        print_array(arr)
    
        MergeSort(arr, 0, n-1)

        print("\n\nSorted array: ")
        print_array(arr)

        counter = recursive_counter + assignment_counter + incremental_counter + comparative_counter
        print("\n\nOperations performed: " + str(counter) + "\n===========================\n")
    except ValueError: 
        print("\nValue should be INT\n")
        continue