class House:
    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        """ Установить новое количество этажей """
        self.number_of_floors = floors
        print('Этажность установлена. В Cтроении ', self.number_of_floors, 'этажей!')


build_1 = House()
print('Объект "Строение" создан. Количество этажей: ', build_1.number_of_floors)
build_1.set_new_number_of_floors(input('Задайте требуемое количество этажей: '))
