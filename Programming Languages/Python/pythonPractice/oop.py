class Car:
    def __init__ (self, color:str, make:str, model:str, year:int) -> None:
        self.color = color
        self.make = make
        self.model = model
        self.year = year    
        
    def __str__(self) -> str:
        return f' {self.make}, {self.model}, {self.color}, {self.year}'
    
    def drive(self) -> None:
        print(f'{self.make} {self.model} is driving ...')
        
    def stop(self) -> None:
        print(f'{self.make} {self.model} is stopped ...')

    def getInfo(self) -> str:
        print( f'Make: {self.make}, Model: {self.model}, Color: {self.color}, Year: {self.year}')
        
        
        
ford: Car = Car('blue', 'Ford', 'Mustang', 1966)
bmw: Car = Car('black', 'BMW', 'M4', 2020)

# ford.getInfo()
# ford.drive()

# bmw.getInfo()
# bmw.drive()

# bmw.stop()
# ford.stop()

print(ford)



