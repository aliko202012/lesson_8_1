# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     def __make_computations(self):
#         add = self.__cpu + self.__memory
#         sub = self.__cpu - self.__memory
#         mult = self.__cpu * self.__memory
#         div = self.__cpu / self.__memory
#         print (f'Сложения:{add}\nВычитание:{sub}\nУмножение:{mult}\nДеление: {div}')

#     def get_cpu(self):
#         return self.__cpu

#     def get_memory(self):
#         return self.__memory

#     def info(self):
#         print (f'Computer cpu={self.__cpu}, memory={self.__memory}\n{self.__make_computations()}')

# computer = Computer(8, 12)
# print(computer.info())
# print("CPU:", computer.get_cpu())
# print("Memory:", computer.get_memory())


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        add = self.__cpu + self.__memory
        sub = self.__cpu - self.__memory
        mult = self.__cpu * self.__memory
        div = self.__cpu / self.__memory
        return f'Сложение: {add}\nВычитание: {sub}\nУмножение: {mult}\nДеление: {div}'

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def info(self):
        return f'Computer cpu={self.__cpu}, memory={self.__memory}\n{self.__make_computations()}'

computer = Computer(8, 12)
print(computer.info())
print("CPU:", computer.get_cpu())
print("Memory:", computer.get_memory())