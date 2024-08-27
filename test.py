# class Animal:
#     def __init__(self,name):
#         self.name = name 

#     def eat(self):
#         print(f"{self.name} ест")
    
#     def sleep(self):
#         print(f"{self.name} спит")

# class Walker:
#     def walk(self):
#         print(f"{self.name} ходит")

# class Swimmer:
#     def swim(self):
#         print(f"{self.name} плавает")


# class Flyer:
#     def fly(self):
#         print(f"{self.name} летает")

# class Penguin(Animal, Walker, Swimmer):
#     def __init__(self, name):
#         super().__init__(name)

#     def describe(self):
#         print(f"{self.name} может ходить и плавать.")

# class Duck(Animal, Walker, Swimmer, Flyer):
#     def __init__(self, name):
#         super().__init__(name)

#     def describe(self):
#         print(f"{self.name} может ходить, плавать и летать.")

# class Bat(Animal , Flyer):
#     def __init__(self, name):
#         super().__init__(name)

#     def describe(self):
#         print(f"{self.name} может летать.")

# penguin = Penguin("Пингвин")
# duck = Duck("утка")
# bat =Bat("Летучая мышь")

# penguin.walk()
# penguin.swim()
# penguin.describe()

# duck.walk()
# duck.swim()
# duck.fly()
# duck.describe()

# bat.fly()
# bat.describe()
# class Vehicle:
#     def move(self):
#         pass
    
#     def fuel(self):
#         pass
    
# class Car(Vehicle):
#     def move(self):
#         print("Машина едет по дороге")
    
#     def fuel(self):
#         print("Машина использует: Бензин")

# class Bicycle(Vehicle):
#     def move(self):
#         print("Велосипед едет по велодорожке")
    
#     def fuel(self):
#         print("Велосипед использует: Силу")

# class Boat(Vehicle):
#     def move(self):
#         print("Лодка плывет по воде")
    
#     def fuel(self):
#         print("Лодка использует: Дизельное топливо")

# vehicles = [Car(), Bicycle(), Boat()]

# for vehicle in vehicles:
#     vehicle.move()

class Vehicle:
    def __init__ (self, marka, fuel):
        self.marka = marka
        self.fuel  = fuel

    def move(self):
        print(f'{self.marka} движется')

    def fuel(self):
        print(f'Тип топлива: {self.fuel}')


class Car(Vehicle):
    def move(self):
        print(f'{self.marka} едет по дороге')


class Bicycle(Vehicle):
    def move(self):
        print(f'{self.marka} движется по велосипедной дорожке')


class Boat(Vehicle):
    def move(self):
        print(f'{self.marka} плывет по воде')



car = Car('Автомобиль', 'Бензин')
bicycle = Bicycle('Велосипед', 'Не требуется')
boat = Boat('Лодка', 'Дизель')


for vehicle in (car, bicycle, boat):
    vehicle.move()
    vehicle.fuel()

