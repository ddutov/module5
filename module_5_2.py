import time

class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor < 1 or self.new_floor > self.number_of_floors:
            print(f"Такого этажа не существует в {self.name}")
        else:
            current_floor = 1
            while current_floor <= new_floor:
                print(current_floor)
                time.sleep(0.5)
                current_floor += 1
            print(f"Лифт приехал на {self.new_floor} этаж")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Горский', 18)
h3 = House('Домик в деревне', 2)
# h1.go_to(int(input(f'Введите номер этажа ЖК Эльбрус ')))
# h2.go_to(int(input(f'Введите номер этажа ЖК Горский ')))
# h3.go_to(int(input(f'Введите номер этажа в Домике в деревне ')))
print(len(h1))
print(len(h2))
print(len(h3))
print(str(h1))
print(str(h2))
print(str(h3))
