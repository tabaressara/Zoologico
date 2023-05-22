import models.Zoologico as zoologicoModel
import models.Habitat as habitatModel
import models.Animal as animalModel
import controller.controllerZoo as zooController
import streamlit as st

class vistaZoo():

    def __init__(self):
        self.modelZoo = zoologicoModel.Zoo()
        self.control = zooController.controllerZoo(self.modelZoo, self)
    def mostrar_menu(self):

        st.title("Bienvenido al zoologico")

        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Agregar animal",
                                                            "Agregar habitat",
                                                            "Agregar animal a habitat",
                                                            "Listar",
                                                            "Realizar accion",
                                                            "Agregar alimento",
                                                            "Eliminar alimento"])

        with tab1:
            st.header("Agregar un animal al zoologico")
            botonAgregar = st.button("Agregar animal", key="botonAgregarAnimal")
        with tab2:
            st.header("Agregar un habitat al zoologico")
            botonHabitat = st.button("Agregar Habitat", key="botonAgregarHabitat")
        with tab3:
            st.header("Agregar animal a habitat del zoologico")
            botonAnimalH = st.button("Agregar animal", key="botonAgregarAnimalHabitat")
        with tab4:
            st.header("Listar habitats y animales")
            botonListar = st.button("Agregar animal", key="botonListar")
        with tab5:
            st.header("Realizar accion")
            botonAccion = st.button("Agregar animal", key="botonAccion")
        with tab6:
            st.header("Agregar alimento a dieta")
            botonAlimento = st.button("Agregar animal", key="botonAgregarAlimento")
        with tab7:
            st.header("Eliminar alimento de dieta")
            botonQuitar = st.button("Agregar animal", key="botonEliminarAlimento")

        if botonAgregar:
            st.session_state["opcion"] = 1
        elif botonHabitat:
            st.session_state["opcion"] = 2
        elif botonAnimalH:
            st.session_state["opcion"] = 3
        elif botonListar:
            st.session_state["opcion"] = 4
        elif botonAccion:
            st.session_state["opcion"] = 5
        elif botonAlimento:
            st.session_state["opcion"] = 6
        elif botonQuitar:
            st.session_state["opcion"] = 7

        if "opcion" in st.session_state:
            self.control.menu(st.session_state["opcion"])

    def solicitar_dato(self, mensaje):
        return input(mensaje)

    def menu_crear_animal(self):

        with st.container():
            st.subheader("Ingrese todos los datos del animal")
            id = st.text_input("Ingrese el numero de identificacion del animal:")
            nombre = st.text_input("Ingrese el nombre del animal")
            especie = st.text_input("Ingrese la especie del animal")
            edad = st.number_input("Ingrese la edad del animal")
            salud = st.number_input("Ingrese la salud del animal")
            temperatura = st.number_input("Ingrese la temperatura del animal")
            hDormir = st.number_input("Ingrese las horas de sueño del animal")
            cantidad = st.number_input("Ingrese la cantidad de comida del animal")
            dieta = st.selectbox("Seleccione la dieta del animal", self.modelZoo.dietas)
            boton_accion = st.button("Crear animal ")

        if boton_accion:
            if not id.isnumeric():
                raise ValueError("El ID debe ser un valor numérico")

            nuevoA = animalModel.Animal(id, nombre, especie, edad, dieta, salud, hDormir, cantidad, temperatura)
            st.success("El animal fue creado con exito")
            return nuevoA

    def menu_crear_habitat(self):

        with st.container():
            st.subheader("Ingrese todos los datos del Habitat")
            nombre = st.selectbox("Elige el nombre del habitat", self.modelZoo.nombreHabitats)
            capacidad = st.number_input("Ingrese la capacidad del habitat")

            if nombre == "Desertico":
                temperaturaMax = 60
                temperaturaMin = 41
                oasis = st.number_input("Ingrese el numero de oasis en el habitat")
                captus = st.number_input("Ingrese el numero de captus en el habitat")
            elif nombre == "Acuatico":
                temperaturaMax = 0
                temperaturaMin = 20
                corales = st.number_input("Ingrese el numero de corales en el habitat")
                profundidad = st.number_input("Ingrese la profundidad del habitat")
            elif nombre == "Selvatico":
                temperaturaMax = 40
                temperaturaMin = 21
                rocas = st.number_input("Ingrese el numero de rocas en el habitat")
                lianas = st.number_input("Ingrese el numero de lianas en el habitat")
            elif nombre =="Polar":
                temperaturaMax = -1
                temperaturaMin = -20
                hielo = st.number_input("Ingrese la cantidad de hielo del habitat")
                iceberg = st.number_input("Ingrese el numero de icebergs en el habitat")

            boton_accion = st.button("Crear animal ")

            if boton_accion:
                if self.modelZoo.repetidos(nombre):
                    self.mensajeError("Ya hay un habitat")
                else:
                    if nombre == "Desertico":
                        nuevo = habitatModel.Desertico(nombre, capacidad, temperaturaMax, temperaturaMin, oasis, captus)
                    elif nombre == "Acuatico":
                        nuevo = habitatModel.Acuatico(nombre, capacidad, temperaturaMax, temperaturaMin, corales, profundidad)
                    elif nombre == "Selvatico":
                        nuevo = habitatModel.Selvatico(nombre, capacidad, temperaturaMax, temperaturaMin, rocas, lianas)
                    elif nombre == "Polar":
                        nuevo = habitatModel.Polar(nombre, capacidad, temperaturaMax, temperaturaMin, hielo, iceberg)

                    st.success("El habitat fue creado")
                    return nuevo

    def menu_añadir_animal(self):

        animalOpcion = [f"Nombre: {animal.nombre}, Especie: {animal.especie}" for animal in self.modelZoo.registro]

        with st.container():
            st.subheader("Animal que agregaras a un habitat")
            if len(self.modelZoo.registro) == 0:
                st.error("No hay animales en el zoologico")
            elif len(self.modelZoo.habitats) == 0:
                st.error("No hay habitats en el zoologico")
            else:
                animalD = st.selectbox("Escoja un animal", animalOpcion)
                habitatD = st.selectbox("Escoja un habitat", self.modelZoo.habitats)

                if habitatD.temperaturaMax < animalD.temperatura or habitatD.temperaturaMin > animalD.temperatura:
                    self.mensajeError("El animal no puede vivir en este habitat")
                elif habitatD.capacidad == len(habitatD.animales):
                    self.mensajeError("No hay espcio en el habitat")
                else:
                    boton_accion = st.button("Añadir animal a habitat ")

                    if boton_accion:
                        habitatD.agregarAnimal(animalD)
                        self.modelZoo.eliminarAnimal(animalD)
                        self.mensajeExitoso("Se agrego el animal a un habitat")




    def mensajeExitoso(self, mensaje):
        st.success(mensaje)
    def mensajeError(self, mensaje):
        st.error(mensaje)