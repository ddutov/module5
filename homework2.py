class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self):
        """ Установить количество этажей """
        number_of_floors = self
        print('Этажность установлена. В строении ', number_of_floors, 'этажей!')

build_1 = House
print('Объект "Строение" создан. Количество этажей не определено.')
build_1.set_new_number_of_floors(input('Ввдите требуемое количество этажей: '))

