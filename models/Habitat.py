class Habitat:
    def __init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.temperaturaMax = temperaturaMax
        self.temperaturaMin = temperaturaMin
        self.animales = []

        def agregarAnimal(self, animal):
            if len(self.animales) >= int(self.capacidad):
                print(f"No se puede agregar a {animal.nombre} al habitat {self.nombre} porque está lleno")
            elif animal.temperatura > self.temperaturaMax or animal.temperatura < self.temperaturaMin:
                print(
                    f"No se puede agregar a {animal.nombre} al habitat {self.nombre} porque no se adapta a la temperatura")
            else:
                self.animales.append(animal)

        def listar_animales(self):
            if self.animales:
                print(
                    f"Hábitat {self.nombre}   temperatura maxima: {self.temperaturaMax}°C, temperatura minima: {self.temperaturaMin}°C, capacidad: {self.capacidad}")
                for animal in self.animales:
                    print(f" - {animal.nombre} ({animal.especie})")
            else:
                print("No hay animales en este hábitat.")

class Desertico(Habitat):
    def __init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin, oasis, captus):
        super().__init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin)
        self.oasis = oasis
        self.captus = captus

class Acuatico(Habitat):
    def __init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin, corales, profundidad):
        super().__init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin)
        self.corales = corales
        self.profundidad = profundidad

class Selvatico(Habitat):
    def __init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin, rocas, lianas):
        super().__init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin)
        self.rocas = rocas
        self.lianas = lianas

class Polar(Habitat):
    def __init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin, hielo, iceberg):
        super().__init__(self, id, nombre, capacidad, temperaturaMax, temperaturaMin)
        self.hielo = hielo
        self.iceberg = iceberg