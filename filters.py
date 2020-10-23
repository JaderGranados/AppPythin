class Empleado():

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} trabaja como {} y gana {}".format(self.nombre, self.cargo, self.salario)


empleados = [
    Empleado("Jader", "Ingeniero", 30000000),
    Empleado("Ana", "Técnica", 3000000),
    Empleado("Felipe", "Ingeniero", 4589777),
    Empleado("Mario", "Tecnólogo", 47955)
]

salarios_altos = filter(lambda empleado: empleado.salario > 1000000, empleados)

for empleado in salarios_altos:
    print(empleado)

def calculo_comision(empleado):
    if empleado.salario < 1000000:
        empleado.salario = empleado.salario * 1.03
    return empleado

empleados_comision = map(calculo_comision, empleados)

for empleado in empleados_comision:
    print(empleado)

def if __name__ == "__main__":
    for empleado in salarios_altos:
        print(empleado)