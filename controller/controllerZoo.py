import models.Habitat as habitatModel
import models.Animal as animalModel
import models.Zoologico as zoologicoModel
import streamlit as st


class controllerZoo():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self, opcion):
        if opcion == 1:
            try:
                self.crearAnimal()
            except ValueError:
                self.vista.mensajeError("Hay un error para crear el animal")
        elif opcion == 2:
            try:
                self.crearHabitat()
            except ValueError:
                self.vista.mensajeError("Hay un error para crear el Habitat")
        elif opcion == 3:
            try:
                self.añadirAnimal()
            except ValueError:
                self.vista.mensajeError("Hay un error para añadir el animal al habitat")
        elif opcion == 4:
            try:
                self.listar()
            except ValueError:
                self.vista.mensajeError("Hay un error para listar los habitats y animales")
        elif opcion == 5:
            try:
                self.realizarAccion()
            except ValueError:
                self.vista.mensajeError("Hay un error para que el animal realice una accion")
        elif opcion == 6:
            try:
                self.agregarAlimento()
            except ValueError:
                self.vista.mensajeError("Hay un error para agregar un alimento")
        elif opcion == 7:
            try:
                self.eliminarAlimento()
            except ValueError:
                self.vista.mensajeError("Hay un error para eliminar un alimento")

    def crearAnimal(self):
        nuevo = self.vista.menu_crear_animal()
        if nuevo:
            self.modelo.agregarAnimal(nuevo)
            return True

    def crearHabitat(self):
        nuevo = self.vista.menu_crear_habitat()
        if nuevo:
            self.modelo.agregarHabitat(nuevo)
            return True

    def añadirAnimal(self):
        self.vista.menu_añadir_animal()

    def listar(self):
        print("bien")
    def realizarAccion(self):
        print("bien")

    def agregarAlimento(self):
        print("bien")

    def eliminarAlimento(self):
        print("bien")
