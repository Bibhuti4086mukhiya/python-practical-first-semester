'''
f=open("IMG_E8174.JPG","rb")
c=f.read()
f.close()

f1=open("bibhutiphoto.jpg","wb")
f1=f1.write(c)
f.close()
'''
f=open("bibhuti.txt","rb")
print(f.isatty())

