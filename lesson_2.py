class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Имя: {self.fullname}, Возраст: {self.age}, Семейное положение: {self.is_married}")

class Teacher(Person):
    salary = 0

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate(self):
        bonus = (self.experience // 3) * 3000
        return Teacher.salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт: {self.experience} лет, Зарплата: {self.calculate()}")


teacher = Teacher("Сергей Иванов", 34, True, 8)
teacher.introduce_myself()