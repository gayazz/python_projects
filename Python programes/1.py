#Write a Python program to solve the equation z = |x y| * (x + y).

x=int(input("Enter x value:"))
y=int(input("Enter y value:"))
a=abs(x-y)
z=(a*(x+y))
print(z)