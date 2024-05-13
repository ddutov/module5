class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1

    def __str__(self):
        return f'новый объект № {self.total}'


for i in range(0, 40):
    new_object = Buiding()
    # print('новый объект № ', Buiding.total)
    print(new_object)
    i += 1
