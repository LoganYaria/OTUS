class Aircraft:
    _engine=2
    __gear='down'

    def __init__(self,type,model):
        '''Class construcotr'''
        self.type=type
        self.model=model

    def get_engine(self):
        return self._engine

    def get_gear_status(self):
        return self.__gear

    def get_type(self):
        return f'{self.type} {self.model}'

    def gear_down(self):
        self.__gear="down"
        print (f'Gear of aircraft {self.type} {self.model} is down')

    def gear_up(self):
        self.__gear="up"
        print (f'Gear of aircraft {self.type} {self.model} is up')

    def fly(self):
        if self.__gear=='down':
            print('Positive rate,gear up!')
        else:
            print(f'{self.type} {self.model} is flying now.' )

if __name__ == '__main__':#при импорте сыбется весь код до этого момента


    aircraft_1=Aircraft('airbus', 'a320')

    print (aircraft_1.type, aircraft_1.model, aircraft_1._Aircraft__gear, aircraft_1._engine)


    Aircraft._engine=990909
    #aircraft_1.gear_up()
    aircraft_1.fly()
    aircraft_1.gear_up()
    aircraft_1.fly()
    print (aircraft_1._engine)