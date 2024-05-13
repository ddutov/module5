class Buiding:
    total = 0
    def __init__(self):
       Buiding.total += 1


for i in range(0, 40):
    new_object = Buiding()
    print('новый объект № ', Buiding.total)
    i += 1
