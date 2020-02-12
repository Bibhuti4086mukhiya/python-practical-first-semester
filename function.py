#def name(place):
   # for x in place:
      #  print(x)

#ocation=('gaushala','ratopool','satopool')
#name(location)

#def  function(x):
   # return 5*x
#print(function(3))
#print(function(4))
#print(function(5))



#def max_of_two(x,y):
 #   if x>y:
  #      return x
   # return y
#def max_of_three(x,y,z):
'''
'''
rows="*"
for i in range (9):
    for j in range(0, i + 1):
        print(rows , end=' ')

    print("\r")
 #   return max_of_two(x,max_of_two(y,z))
#print(max_of_three(222,444,-888))
'''
num=int(input("enter ur numnber"))
if num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
elif num%3==0 and num%5==0:
    print("fizz_buzz")
else:
    print(num ,"isnot divisible by 3 and 5")
'''
'''
limit=int(input("enter ur number"))
for i in range(0,limit+1):
    if i%2==0:
        print(str(i) +" "+'even')
    else:
        print(str(i) +" "+'odd')
'''
'''
def prime(n):
    if  (n==1):
        return false
    elif (n==2):
        return true
     else :
        for x in range(2,n):
            if x%n==0:
                return false
            return true
print(prime(8))
'''

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
        print(test_prime(9)z