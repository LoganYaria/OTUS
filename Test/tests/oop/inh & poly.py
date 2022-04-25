class Aircraft:
    _engine=None
    __engine_status="Off"

    def __init__(self, type,model,engine):
        self.type=type
        self.model=model
        self._engine=engine

    def get_engine(self):
        return self._engine

    def get_engine_status(self):
        return self.__engine_status

    def get_name(self):
        return f'{self.type} {self.model}'

    def start_engine(self):
        if self._engine==1:
            self.__engine_status='On'
            print("Starting engine!")
        else:
            self.__engine_status = 'On'
            print("Starting engine nomber 1!")
            print("Starting engine nomber 2!")

    def after_start_check_list(self):
        if self.__engine_status!="On":
            self.start_engine()
        else:
            print(f'After start check list for {self.get_name()}, please!')


class Captein:
#абстрактный метод
    def get_name(self):
        raise NotImplemented("This metod is not implimented!")

    def hello(self):
        print(f'Welcome on bort {self.get_name()}!')


class Prop(Aircraft):
    def __init__(self,type,model):
        #через super образаемся к конструктору Aircraft
        super().__init__(type,model,1)


class Jet(Aircraft,Captein):
#Класс Mixin
    def __init__(self, type,model):
        super().__init__(type,model,2)

    def boom(self):
        print("Boom, I'm Asshole")

    def prefly(self):
        if self.get_engine_status()!="On":
            print(f"Let's start engine of {self.get_name()}")
            self.start_engine()
        else:
            self.after_start_check_list()

#aircraft_1=Prop(type="c", model="172")
#print (aircraft_1.type,aircraft_1.model)
#aircraft_1.start_engine()
#aircraft_1.after_start_check_list()

aircraft_1=Jet(type="Boeing", model="737")
aircraft_1.hello()
aircraft_1.prefly()
aircraft_1.after_start_check_list()



#aircraft_1.prefly()



