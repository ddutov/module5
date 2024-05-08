class Building:
    def __init__(self, floor=None):
        self.numberOfFloors = int(floor)
        self.buildingType = input('назначение здания: ')
        print(f'в здании {self.numberOfFloors} этажей, это - {self.buildingType}')
        self.prop = []  # список параметров здания
        self.prop.append(self.numberOfFloors)   # добавляем параметр здания в список
        self.prop.append(self.buildingType)  # добавляем параметр здания в список

    def __eq__(self, other):
        return self.prop == other.prop


house_1 = Building(floor=input('сколько этажей в доме_1: '))
house_2 = Building(floor=input('сколько этажей в доме_2: '))
if Building.__eq__(self=house_1, other=house_2):
    print('здания одинаковы по параметрам')
else:
    print('это разные эдания')
