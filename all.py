def amstt(a):
    o = len(str(a))
    s = 0
    t = a
    while t > 0:
        digit = t % 10
        s += digit ** o
        t //= 10
    if a == s:
        return True
    else:
        return False

def Divideby8(x):
    if x%8==0:
        return True
    else:
        return False

def smallest(a,b,c):
    if a < b and a < c :
        return a
    elif b < c and b < a:
        return b
    else:
        return c

def evenorodd(x):
    if (x%2==0):
        return "Even"
    else:
        return "Odd"

def ispalindrome(x):
    rev = 0
    temp = x
    while temp>0:
        rev = (rev*10)+(temp%10);
        temp = temp//10
    if rev == x :
        return True
    else:
        return False

if __name__=="__main__":
    print("Check amstrong number or not>")
    a = int(input("Enter the number"))
    print(amstt(a))

    print("\nCheck the divisibility by 8>")
    x = int(input("Enter the number:"))
    print(Divideby8(x))

    print("\nCheck the smallest number>")
    a = input("Enter the first number:")
    b = input("Enter the second number:")
    c = input("Enter the third number:")
    print(smallest(a,b,c))

    print("\nCheck whether even or odd>")
    x = int(input("Enter the number:"))
    print(evenorodd(x))

    print("\nCheck palindrome or not>")
    a = input("Enter the number")
    print(ispalindrome(x))
