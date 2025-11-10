from exceptions import BangException

class Player: 
    def __init__(self, name, revolver):
        self.name = name
        self.revolver = revolver
    
    def shoot(self):
        try:
            print(f'{self.name} нажал на курок')
            self.revolver.pull_trigger()
        except BangException as e:
            print(f'{self.name}Убит! {e}')
            return True #Проигрыш
        return False#Выйгрыш
    
