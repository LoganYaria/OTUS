class Aircraft:
    gear='down'

    def __init__(self,type,model,engine):
        '''Class construcotr'''
        self.type=type
        self.model=model
        self.engine=engine

    def gear_down(self):
        self.gear='down'
        print(f'Gear of {self.type} {self.model} is down')

    def gear_up(self):
        self.gear = 'up'
        print(f'Gear of {self.type} {self.model} is up')

    def fly(self):
        if self.gear== "down":
            self.gear_up()
        print(f'The aircraft {self.type} {self.model} is flying and gear is {self.gear}')


boeing_747=Aircraft('boeing','747',4)

#print (boeing_747.type,boeing_747.model,boeing_747.engine)
print (boeing_747.fly())