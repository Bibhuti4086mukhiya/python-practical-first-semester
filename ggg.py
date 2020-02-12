'''
 def ispilindrome(string):
    left_pos=0
    right_pos=len(string)-1
    while right_pos>=left_pos:
        if not string[left_pos]==string[right_pos]:
            return False
        left_pos=left_pos+1
        right_pos=right_pos-1
        return True
print(ispilindrome("oo"))
 '''
'''
lower=int(input("enter ur number"))
upper=int(input("enter ur number"))
for i in range(lower,upper+1):
    if i%7==0 and i%5==0:
        print(i)
'''
'''
list=[]
for i in range(5,700):
    if i%7==0 and i%5==0:
        print(i)
'''
'''
c=37.5
f=(c*(9/5)) +32
print(" 37.5  degree celsius into fehrenheit is",f)
'''
num=int(input("enter ur number"))
for i in range():