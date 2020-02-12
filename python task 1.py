a=(input('Enter your name:'))
b=(input('Enter your surname:'))
c=(input('Enter your Email:'))
d=(input('Enter your password:'))
e=(input('Enter your Repassword:'))
if d==e:
        print('you have successfully created an account.')
else:
        print('password does not match.')

f=open('acc.txt','w')
f.write(a)
f.write(b)
f.write(c)
f.write(d)
f.close()

z=(input('to login'
         'Enter your Email:'))
y=(input('Enter your password:'))
if d==y==e and c==z:
    print('u r weicome')
else:
    print('check ur Email and try again:')

