def findReverse(n):
    reverse=0
    remainder=0
    while(n!=0):
        remainder=n%10
        reverse=reverse*10+remainder
        n=int(n/10)
    return reverse
    
num=int(input("Enter a number : "))
reverse=findReverse(num)
print("The reverse number is = ",reverse)
