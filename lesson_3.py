# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu = cpu
#         self.__memory = memory

#     def __make_computations(self):
#         add = self.__cpu + self.__memory
#         sub = self.__cpu - self.__memory
#         mult = self.__cpu * self.__memory
#         div = self.__cpu / self.__memory
#         return f'Сложения:{add}\nВычитание:{sub}\nУмножение:{mult}\nДеление: {div}'

#     def get_cpu(self):
#         return self.__cpu

#     def get_memory(self):
#         return self.__memory

#     def info(self):
#         return f'Computer cpu={self.__cpu}, memory={self.__memory}\n{self.__make_computations()}'


# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().__init__(cpu, memory)
#         self.__memory_card = memory_card

#     def get_memory_card(self):
#         return self.__memory_card

#     def info(self):
#         return f"Laptop cpu={self.get_cpu()}, memory={self.get_memory()}, memory_card={self.get_memory_card()})"



# computer = Computer(10, 8)
# laptop = Laptop(20, 15 ,128)


# print(computer.info())
# print(laptop.info())

# print("CPU:", computer.get_cpu())
# print("Memory:", computer.get_memory())

# print("Laptop CPU:", laptop.get_cpu())
# print("Laptop Memory:", laptop.get_memory())
# print("Laptop Memory Card:", laptop.get_memory_card())


