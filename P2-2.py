def len_s(s):
    count=0
    for i in s:
        if i!='':
            count+=1

    print("The total lenth of the string : ",count)

s=str(input("Enter a statement : "))
len_s(s)
