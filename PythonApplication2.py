def count_triangles(n):
    result = 0
    for i in range(n):
        for j in range(n-i):
            for k in range(n-i-j):
                result += 1

    k = n - 1
    for i in range(n//2):
        for j in range(k):
            result += j + 1
        k-=2
    print(result)


while True:
    try:
        n = int(input())
        count_triangles(n)
    except ValueError:
        print(" SYNTAX ERROR (should be INT)")
        continue
    break