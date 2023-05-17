#Check if the nth power of a number is even or not.
num=int(input('enter a number : '))
power=int(input('enter the nth power for the number : '))
x=num**power
if x%2==0:
    print('the nth power of the number is even')
else:
    print('the nth power of the number is odd')
