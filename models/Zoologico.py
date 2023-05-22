class Zoo:
    def __init__(self):
        self.habitats = []
        self.registro = []
        self.dietas = {"carnivoro": [], "herbivoro": [], "omnivoro": []}

    def animal_registro(self, animal):
        self.registro.append(animal)

    def agregar_habitat(self, habitat):
        self.habitats.append(habitat)

    def eliminar_animal(self, animal):
        self.registro.remove(animal)

    def listarHabitats(self):
        if self.habitats:
            for habitat in self.habitats:
                habitat.listar_animales()
        else:
            print("No hay hábitats en el zoológico.")