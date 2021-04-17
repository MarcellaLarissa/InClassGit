def divisors(x):
    n = 1
    while n <= x:
        if (x % n == 0):
            print(n)
        n = n + 1
    
x = int(input("Please enter a number"))

divisors(x)

#fixed logic with help from Geeks for Geeks https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/