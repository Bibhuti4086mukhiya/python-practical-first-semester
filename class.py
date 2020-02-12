class student:
    def __init__(self,a,b):
        self.name=a
        self.roll=b

    def display(self):
        print("hello i'm",self.name)
        print("my roll is",self.roll)
obj=student('bibhuti','455')
obj.display()