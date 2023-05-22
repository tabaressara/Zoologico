class Habitat:
    def __init__(self, nombre, capacidad, temperaturaMax, temperaturaMin):
        self.nombre = nombre
        self.capacidad = capacidad
        self.temperaturaMax = temperaturaMax
        self.temperaturaMin = temperaturaMin
        self.animales = []

    def agregarAnimal(self, animal):
        self.animales.append(animal)
class Desertico(Habitat):
    def __init__(self, nombre, capacidad, temperaturaMax, temperaturaMin, oasis, captus):
        super().__init__(nombre, capacidad, temperaturaMax, temperaturaMin)
        self.oasis = oasis
        self.captus = captus

class Acuatico(Habitat):
    def __init__(self, nombre, capacidad, temperaturaMax, temperaturaMin, corales, profundidad):
        super().__init__(nombre, capacidad, temperaturaMax, temperaturaMin)
        self.corales = corales
        self.profundidad = profundidad

class Selvatico(Habitat):
    def __init__(self, nombre, capacidad, temperaturaMax, temperaturaMin, rocas, lianas):
        super().__init__(nombre, capacidad, temperaturaMax, temperaturaMin)
        self.rocas = rocas
        self.lianas = lianas

class Polar(Habitat):
    def __init__(self, nombre, capacidad, temperaturaMax, temperaturaMin, hielo, iceberg):
        super().__init__(nombre, capacidad, temperaturaMax, temperaturaMin)
        self.hielo = hielo
        self.iceberg = iceberg