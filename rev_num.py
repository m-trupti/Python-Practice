def rev_num(num): 
    reverse = 0 
    while(num > 0): 
        rem = num %10 
        reverse = (reverse *10) + rem 
        num = num //10 
    print("Reverse number is ", reverse)
number = int(input("Enter a number to reverse :  "))
rev_num(number)
