class People:
    def __init__(self, name='', age=0, occupation=''):
        self._name = name
        self._age = age
        self._occupation = occupation
    def __str__(self):
        return f'{self._name} has {self._age} years and work as {self._occupation}'
    
    @property
    def salutation(self):
        if self._occupation:
            return(f'Welcome {self._name} your occupation is {self._occupation}')
        else:
            return(f'Welcome {self._name}')

    def birthday(self):
        self._age +=1
        

people1 = People('João', 40, 'advogado')

people1.salutation()