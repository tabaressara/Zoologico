import models.Habitat as habitatModel
import models.Animal as animalModel
import models.Zoologico as zoologicoModel


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
            self.eliminarAlimento()

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
        zoologicoModel.animal_registro(nuevo)

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
            nuevoH = habitatModel.Desertico(id, "Desertico", capacidad, 60, 40, oasis, captus)

        elif opcion == 2:
            corales = int(self.vista.solicitar_dato("ingrese el numero de corales en el habitat: "))
            profundidad = int(self.vista.solicitar_dato("ingrese la profundidad del habitat: "))
            nuevoH = habitatModel.Acuatico(id, "Acuatico", capacidad, 19, 0, corales, profundidad)

        elif opcion == 3:
            rocas = int(self.vista.solicitar_dato("ingrese el numero de rocas en el habitat: "))
            lianas = int(self.vista.solicitar_dato("ingrese el numero de lianas en el habitat: "))
            nuevoH = habitatModel.Selvatico(id, "Selvatico", capacidad, 39, 20, rocas, lianas)

        elif opcion == 4:
            hielo = int(self.vista.solicitar_dato("ingrese la cantidad de hielo en el habitat: "))
            iceberg = int(self.vista.solicitar_dato("ingrese la cantidad de icebergs en el habitat: "))
            nuevoH = habitatModel.Polar(id, "Polar", capacidad, -1, -20, hielo, iceberg)

        elif opcion == 5:
            nombre = self.vista.solicitar_dato("ingrese el nombre del habitat: ")
            temperaturaMax = int(self.vista.solicitar_dato("ingrese la temperatura maxima del habitat: "))
            temperaturaMin = int(self.vista.solicitar_dato("ingrese la temperatura minima del habitat: "))
            nuevoH = habitatModel.Habitat(id, nombre, capacidad, temperaturaMax, temperaturaMin)

        else:
            print("VALOR NO VALIDO")

        self.modelo.agregar_habitat(nuevoH)

    def añadirAnimal(self):

        nombreA = self.vista.solicitar_dato("Ingrese nombre del animal: ")
        nombreH = self.vista.solicitar_dato("Ingrese nombre del habitat: ")

        animal = next((a for a in self.modelo.registro if a.nombre == nombreA), None)
        habitat = next((h for h in self.modelo.habitats if h.nombre == nombreH), None)

        self.modelo.agregarAnimal(animal)
        self.modelo.eliminar_animal(animal)

    def listar(self):
        self.modelo.listarHabitats()

    def realizarAccion(self):
        nombreA = self.vista.solicitar_dato("Ingrese nombre del animal: ")
        animal = next((a for a in self.modelo.registro if a.nombre == nombreA), None)

        print("Va a realizar una accion")
        print("1) comer")
        print("2) dormir")
        print("3) jugar")
        opcion = int(self.vista.solicitar_dato("escoja una opcion: "))

        if opcion == 1:
            tipo = animal.dieta
            alimento = self.vista.solicitar_dato("ingrese el nombre del alimento")
            cantidadC = int(self.vista.solicitar_dato("ingrese la cantidad de alimento"))

            if alimento in self.modelo.dietas[tipo]:
                if animal.comido + cantidadC <= animal.cantidad:
                    print(f"{animal.nombre} ha comido {cantidadC} de {alimento}.")
                    animal.comido += cantidadC
                else:
                    print(f"{animal.nombre} no puede comer tanta comida")
            else:
                print(f"{animal.nombre} no puede comer {alimento}.")

        elif opcion == 2:
            tiempo = int(self.vista.solicitar_dato("ingrese el tiempo que va a dormir el animal"))

            if tiempo < 0:
                print("El número de horas de sueño debe ser mayor o igual a cero.")

            elif tiempo > animal.hDormir:
                print(f"El tiempo máximo de sueño para {animal.nombre} es de {animal.hDormir} horas.")

            else:
                if animal.sueno + tiempo <= animal.hDormir:
                    print(f"{animal.nombre} ha dormido durante {tiempo} horas.")
                    animal.sueno += tiempo
                else:
                    print(f"{animal.nombre} no puede dormir tanto tiempo")

        elif opcion == 3:
            if animal.jugado:
                print(f"{animal.nombre} ya jugó hoy.")
            else:
                print(f"{animal.nombre} está jugando.")
                animal.jugado = True

        else:
            print("Acción no válida.")

    def agregarAlimento(self):
        alimento = self.vista.solicitar_dato("ingrese el nombre del alimento")
        tipo = self.vista.solicitar_dato("ingrese el nombre de la dieta")
        if tipo in self.modelo.dietas:
            self.modelo.dietas[tipo].append(alimento)
            print(f"Se ha agregado {alimento} al tipo de alimentación {tipo}")
        else:
            print(f"No se reconoce el tipo de alimentación {tipo}")

    def eliminarAlimento(self):
        alimento = self.vista.solicitar_dato("ingrese el nombre del alimento")
        tipo = self.vista.solicitar_dato("ingrese el nombre de la dieta")
        if tipo in self.modelo.dietas and alimento in self.modelo.dietas[tipo]:
            self.modelo.dietas[tipo].remove(alimento)
            print(f"Se ha eliminado {alimento} del tipo de alimentación {tipo}")
        else:
            print(f"No se encontró {alimento} en el tipo de alimentación {tipo}")