class House:

    def __init__(self):
        self.numberOfFloors = int(input('Введите этажность нового здания: '))


print('Покатаемся на лифте?')
while True:
    new_build = House()
    print('Едем на лифте вниз!')
    while new_build.numberOfFloors > 0:
        print('Текущий этаж равен: ', new_build.numberOfFloors)
        new_build.numberOfFloors -= 1
    a_ = input('Строим ещё одно здание (Yes/No)')
    if a_ == 'N' or a_ == 'n':
        break
