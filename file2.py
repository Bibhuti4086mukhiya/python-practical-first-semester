f=open("IMG_E8278.JPG","rb")
e=f.read()
f.close()

s=open("ola.jpeg","wb")
s.write(e)
f.close()

'''
a=int(input("enter ur num"))
b=int(input("enter ur num"))
try:
    print('the resut:',a/b)
except ZeroDivisionError:
    print(" u can't divide by 0")
print("over")
'''
try:
    a = int(input("enter ur num"))
    b=int(input("enter ur num"))
    print(a/b)
except ArithmeticError as e:
    print(type(e))
    print("description:",e)
    print(e.__class__)
    print(e.__class__.__name__)
print('over')