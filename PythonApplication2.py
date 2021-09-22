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


def Merge(array, begin, end, statistic_):
    mid = begin + (end - begin) // 2
    i = begin; j = mid + 1; temp_arr = []; 

    statistic_[3] += 2            # 2 порівняння
    while(i <= mid and j <= end): 
        if(array[i] <= array[j]):
            temp_arr.append(array[i])
            i+=1
        else: 
            temp_arr.append(array[j])
            j+=1
        statistic_[1] += 1        # 1 присвоєння 
        statistic_[2] += 1        # 1 інкремент
        statistic_[3] += 3        # 3 порівняння

    statistic_[3] += 1            # 1 порівняння
    while(i<=mid):
        temp_arr.append(array[i])
        i+=1
        statistic_[1] += 1        # 1 присвоєння 
        statistic_[2] += 1        # 1 інкремент
        statistic_[3] += 1        # 1 порівняння

    statistic_[3] += 1            # 1 порівняння
    while(j<=end):
        temp_arr.append(array[j])
        j+=1
        statistic_[1] += 1        # 1 присвоєння 
        statistic_[2] += 1        # 1 інкремент
        statistic_[3] += 1        # 1 порівняння

    for m in range(len(temp_arr)):
        array[begin+m] = temp_arr[m]
        statistic_[1] += 1        # 1 присвоєння 
        statistic_[2] += 1        # 1 інкремент
        statistic_[3] += 1        # 1 порівняння


def MergeSort(array, left, right, statistic_):

    statistic_[0] += 1            # 1 рекурсивний виклик
    statistic_[3] += 1            # 1 порівняння
    if(left < right):
        MergeSort(array, left, left + (right - left) // 2, statistic_)
        MergeSort(array, left + (right - left) // 2 + 1, right, statistic_)
        Merge(array, left, right, statistic_)


while True:
    try:
        recursive_counter = 0
        assignment_counter = 0
        incremental_counter = 0
        comparative_counter = 0

        statistic_of_counters = [recursive_counter, assignment_counter, incremental_counter, comparative_counter]

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
    
        MergeSort(arr, 0, n-1, statistic_of_counters)

        print("\n\nSorted array: ")
        print_array(arr)

        counters = 0
        for i in range (len(statistic_of_counters)):
            counters += statistic_of_counters[i]
        
        print("\n\nOperations performed: " + str(counters) + '\n' + '='*30 + '\n')

    except ValueError: 
        print("\nValue should be INT\n")
        continue
