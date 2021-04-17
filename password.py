import random

def password(n):
    passwordList = []
    list_A = [1,"h","r","y","f","x","j","i",2,8,"g","r","j",8,"g","w","c",9,"h","v",0,"b","j","o",2,"a","x","z",3, 4, 8,5, 6]
    while n > 0:
        passwordList.append(random.choice(list_A[random.randrange(0, 30)]))
        n = n - 1
    print(passwordList)
n = int(input("Please enter a number"))


password(n)