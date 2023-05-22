import models.Zoologico as zoologicoModel
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