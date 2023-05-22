import models.Habitat as habitatModel
import models.Animal as animalModel


class controllerZoo():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self, opcion):
        if opcion == 1:
            self.crearAnimal()
        elif opcion == 2:
            self.crearHabitat()
        elif opcion == 3:
            self.añadirAnimal()
        elif opcion == 4:
            self.listar()
        elif opcion == 5:
            self.realizarAccion()
        elif opcion == 6:
            self.agregarAlimento()
        elif opcion == 7:
            self.EliminarAlimento()

    def crearAnimal(self):
        id = int(self.vista.solicitar_dato("ingrese el id del animal"))
        nombre = self.vista.solicitar_dato("ingrese el nombre del animal")
        especie = self.vista.solicitar_dato("ingrese la especie del animal")
        edad = int(self.vista.solicitar_dato("ingrese la edad del animal"))
        dieta = self.vista.solicitar_dato("ingrese la dieta del animal")
        salud = int(self.vista.solicitar_dato("ingrese la salud del animal"))
        hDormir = int(self.vista.solicitar_dato("ingrese las horas de sueño del animal"))
        cantidad = int(self.vista.solicitar_dato("ingrese la cantidad de comida del animal"))
        temperatura = int(self.vista.solicitar_dato("ingrese la temperatura del animal"))

        nuevo = animalModel.Animal(id, nombre, especie, edad, dieta, salud, hDormir, cantidad, temperatura)
        self.modelo.animal_registro(nuevo)

    def crearHabitat(self):
        print("escoge un habitat para crear")
        print("1) desertico")
        print("2) acuatico")
        print("3) selvatico")
        print("4) polar")
        print("5) otro")

        opcion = int(self.vista.solicitar_dato("escoja una opcion: "))

        id = int(self.vista.solicitar_dato("ingrese el id del habitat: "))
        capacidad = int(self.vista.solicitar_dato("ingrese la capacidad del habitat: "))

        if opcion == 1:
            oasis = int(self.vista.solicitar_dato("ingrese el numero de oasis en el habitat: "))
            captus = int(self.vista.solicitar_dato("ingrese el numero de captus en el habitat: "))
            nuevo = habitatModel.Desertico(id, "Desertico", capacidad, 60, 40, oasis, captus)

        elif opcion == 2:
            corales = int(self.vista.solicitar_dato("ingrese el numero de corales en el habitat: "))
            profundidad = int(self.vista.solicitar_dato("ingrese la profundidad del habitat: "))
            nuevo = habitatModel.Acuatico(id, "Acuatico", capacidad, 19, 0, corales, profundidad)

        elif opcion == 3:
            rocas = int(self.vista.solicitar_dato("ingrese el numero de rocas en el habitat: "))
            lianas = int(self.vista.solicitar_dato("ingrese el numero de lianas en el habitat: "))
            nuevo = habitatModel.Selvatico(id, "Selvatico", capacidad, 39, 20, rocas, lianas)

        elif opcion == 4:
            hielo = int(self.vista.solicitar_dato("ingrese la cantidad de hielo en el habitat: "))
            iceberg = int(self.vista.solicitar_dato("ingrese la cantidad de icebergs en el habitat: "))
            nuevo = habitatModel.Polar(id, "Polar", capacidad, -1, -20, hielo, iceberg)

        elif opcion == 5:
            nombre = self.vista.solicitar_dato("ingrese el nombre del habitat: ")
            temperaturaMax = int(self.vista.solicitar_dato("ingrese la temperatura maxima del habitat: "))
            temperaturaMin = int(self.vista.solicitar_dato("ingrese la temperatura minima del habitat: "))
            nuevo = habitatModel.Habitat(id, nombre, capacidad, temperaturaMax, temperaturaMin)

        else:
            print("VALOR NO VALIDO")

        self.modelo.agregar_habitat(nuevo)

    def añadirAnimal(self):

        nombreA = self.vista.solicitar_dato("Ingrese nombre del animal: ")
        nombreH = self.vista.solicitar_dato("Ingrese nombre del habitat: ")

        animal = next((a for a in self.modelo.registro if a.nombre == nombreA), None)
        habitat = next((h for h in self.modelo.habitats if h.nombre == nombreH), None)

        self.modelo.agregarAnimal(animal)
        self.modelo.eliminar_animal(animal)