"""
class Worker:
def __init__(self, name, pay): # Инициализация при создании 
self.name = name # self – это сам объект 
self.pay = pay 
def lastName(self): return self.name.split()[-1] # Разбить строку по символам пробела 
def giveRaise(self, percent): self.pay *= (1.0 + percent) # Обновить сумму выплат

bob = Worker(‘Bob Smith’, 50000) # Создаются два экземпляра и для каждого
sue = Worker(‘Sue Jones’, 60000) # определяется имя и сумма выплат
bob.lastName() # Вызов метода: self – это bob

sue.lastName() # self – это sue

sue.giveRaise(.10) # Обновить сумму выплат для sue
sue.pay
"""


#x = "Mike"
#print(dir(x))

class Aircraft (object):
    def __init__(self,engine,type,glider):
        """Constructor"""
        self.engine = engine
        self.type = type
        self.glider = glider

    def taxi(self):
        """Plane is tasxing"""
        return "Plane %s is tasxing" %self.type

    def fly(self):
        """Plane is flying"""
        return "%s plane %s is flying"%(self.glider,self.type)

if __name__=='__main__':
    plane_1=Aircraft('jet','Boeing737','low wing')
    print(plane_1.fly())
    print(plane_1.taxi())

    plane_2 = Aircraft('screw', 'An2', 'biplane')
    print(plane_2.fly())
    print(plane_2.taxi())


#Еще один пример создания подкласса:

class A320n(Aircraft):
    def fly(self):
        return "This amazing Airbus A320 Neo will fly forever!!!"

plane_3 =A320n('jet','A320n','low wing')
print (plane_3.taxi())
print (plane_3.fly())



def test_delete():
    pass