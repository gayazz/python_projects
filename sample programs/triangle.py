#accept 3 sides of a triangle & check whether triangle is possible or not
s1=int(input('enter side 1 : '))
s2=int(input('enter side 2 : '))
s3=int(input('enter side 3 : '))
if s1!=0 and s2!=0 and s3!=0:
    if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
        print('the sides form a triangle')
    else:
        print('the sides will not form a triangle')
else:
    print('the sides will not form a triangle')
    