class Aircraft:
    engine=2#если создаешь переменную класса, то хуярб ее с большой буквы так как это константа, мразь


    def fly(self):
        print("Aircraft is flying")

    def taxi(self):
        print("Aircraft is taxing")

class Animal:
    heart=1

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        peint("Animal is sleeping")


boeing =Aircraft()

print(Aircraft.engine)
Aircraft.engine=10
print(boeing.engine)
print(Aircraft.engine)

