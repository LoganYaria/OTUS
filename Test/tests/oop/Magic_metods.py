class Hello:
    def __init__(self, amount):
        self.amount=amount

    def __str__(self):
        return 'HeLlO:{}'.format(self.amount)

    def __repr__(self):
        return "hel*FUCKING*lo - {}".format(self.amount)
    #Репрезентация. удобно на классе каждый класс про себя рассказывает)

    def __eq__(self, other):
        return self.amount==other.amount
    #сравнение объектов класса

    def __add__(self,other):
        if not isinstance(other,Hello):
            raise ValueError("не сложить это говно")
        return self.__class__(self.amount+other.amount)
    #сложенеие объектов класса

    def __call__(self,*args):
        return str(self) + " got args " + str(args)

b1=Hello(100)
b2=Hello(100)
print(b1)
print(b2)
print ([b1,b2])
print (b1==b2)
print (b1+b2)

print(callable(b2))
print(b2('говно'))