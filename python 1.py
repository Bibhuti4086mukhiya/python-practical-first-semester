class abc:
    def xyz(self,x):
        print(x)
    @classmethod
    def class_xyz(cls,x):
        print(cls)
        print(x)
    @staticmethod
    def static_xyz(x):
        print(x)
obi=abc()
obi.xyz(5)
obi.class_xyz(3)
obi.static_xyz(2)


