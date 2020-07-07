def mountain(n):
    k = n-1
    for row in range(0,n):
        for column in range(0,k):
            print(end="  ")
        k = k-1
        for column in range(0,row+1):
            print("* ",end = "  ")
        print("\n")

n1 = int(input())
mountain(n1)
