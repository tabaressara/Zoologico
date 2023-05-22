import models.Zoologico as zoologicoModel
import models.Habitat as habitatModel
import models.Animal as animalModel
import controller.controllerZoo as zooController

class vistaZoo():
    def mostrar_menu(self):
        self.zoologicoM = zoologicoModel.Zoo()
        self.control = zooController.controllerZoo(zoologicoModel, self)

        print("bienvenido al zoologico")

        while True:

            print("1) Agregar animal")
            print("2) Agregar habitat")
            print("3) Agregar animal a habitat")
            print("4) Listar")
            print("5) Realizar accion")
            print("6) agregar alimento")
            print("7) eliminar alimento")
            print("0. Salir ")
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 0:
                print("hasta luego")
                break
            else:
                print(self.control.menu(opcion))
    def solicitar_dato(self, mensaje):
        return input(mensaje)

    def menu_crear_animal(self):

        id = int(input("ingrese el id del animal"))
        nombre = input("ingrese el nombre del animal")
        especie = input("ingrese la especie del animal")
        edad = int(input("ingrese la edad del animal"))
        dieta = input("ingrese la dieta del animal")
        salud = int(input("ingrese la salud del animal"))
        hDormir = int(input("ingrese las horas de sueño del animal"))
        cantidad = int(input("ingrese la cantidad de comida del animal"))
        temperatura = int(input("ingrese la temperatura del animal"))

        nuevoA = animalModel.Animal(id, nombre, especie, edad, dieta, salud, hDormir, cantidad, temperatura)

        return nuevoA