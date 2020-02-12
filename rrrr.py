def div():

   a=int(input("enter ur num : "))
   b=int(input("enter ur num : "))
   print('THE RESULT IS', a / b)
def idx():
   n=[1,2,3]
   i=("enter your index value")
   p=(print("index value",n[i]))
   print(n[5])

def file():
   o = open('sssss.txt', 'r')
   print(o.write())

def vlu():
   e=int(input("enter a number: "))
   print("entered num is",e)

try:
   div()
   idx()
   file()
   vlu()
except ZeroDivisionError :
    print("can't divied by 0")
    idx()
    file()
    vlu()
except ValueError :
   print("enter numberical value")
   file()
   div()
   vlu()
except FileNotFoundError:
   print("create file first")
   vlu()
   div()
   idx()

except IndexError:
   print("correct index")
   div()
   idx()
   file()

print("BIVUTI")