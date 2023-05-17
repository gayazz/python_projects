#accept a number & check whether it is + or -
num=int(input('enter a number : '))
if num>0:
    print(num ,'is a positive number')
elif num==0:
    print(num ,'is neither positive nor negative')
else:
    print(num ,'is not a positive number')
    