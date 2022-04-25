class Car:
    pass

class Animal(Car):
    pass

toyota=Car#присваивание класса объекту
toyota1 = toyota()
toyota2=Animal()#наделение объекта свойствами клсаа кар блять
lada=Car()
dog=Animal()

#проверяет принадлежность объекта к классу
print ("toyota2<-Car", isinstance(toyota2,Car))
