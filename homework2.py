class House:
    def __init__(self):
        self.number_of_floors = 0

    def __set__(self, floors):
        """ Установить новое количество этажей """
        self.number_of_floors = floors

build_1 = House()
print('Объект "Строение" создан. Количество этажей: ', build_1.number_of_floors)
build_1.__set__(input('Задайте требуемое количество этажей: '))
print('Этажность установлена. В строении ', build_1.number_of_floors, 'этажей!')

