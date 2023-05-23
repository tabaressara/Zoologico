import models.Zoologico as zoologicoModel
import models.Habitat as habitatModel
import models.Animal as animalModel
import controller.controllerZoo as zooController
import streamlit as st
import requests as rq

class vistaZoo():

    def __init__(self):
        self.modelZoo = zoologicoModel.Zoo()
        self.control = zooController.controllerZoo(self.modelZoo, self)
    def mostrar_menu(self):

        st.title("Bienvenido al zoologico")

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8= st.tabs(["Agregar animal",
                                                            "Agregar habitat",
                                                            "Agregar animal a habitat",
                                                            "Listar",
                                                            "Realizar accion",
                                                            "Agregar alimento",
                                                            "Eliminar alimento", "Mostrar API"])

        with tab1:
            st.header("Agregar un animal al zoologico")
            botonAgregar = st.button("Agregar animal", key="botonAgregarAnimal")
        with tab2:
            st.header("Agregar un habitat al zoologico")
            botonHabitat = st.button("Agregar Habitat", key="botonAgregarHabitat")
        with tab3:
            st.header("Agregar animal a habitat del zoologico")
            botonAnimalH = st.button("Agregar animal a habitat", key="botonAgregarAnimalHabitat")
        with tab4:
            st.header("Listar habitats y animales")
            botonListar = st.button("Listar", key="botonListar")
        with tab5:
            st.header("Realizar accion")
            botonAccion = st.button("Realizar accion", key="botonAccion")
        with tab6:
            st.header("Agregar alimento a dieta")
            botonAlimento = st.button("Agregar alimento", key="botonAgregarAlimento")
        with tab7:
            st.header("Eliminar alimento de dieta")
            botonQuitar = st.button("Eliminar alimento", key="botonEliminarAlimento")
        with tab8:
            st.header("Mostrar API")
            botonMostrar = st.button("Eliminar alimento", key="botonMostrar")

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
        elif botonMostrar:
            st.session_state["opcion"] = 8

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
                id = 1
                temperaturaMax = 60
                temperaturaMin = 41
                oasis = st.number_input("Ingrese el numero de oasis en el habitat")
                captus = st.number_input("Ingrese el numero de captus en el habitat")
            elif nombre == "Acuatico":
                id = 2
                temperaturaMax = 0
                temperaturaMin = 20
                corales = st.number_input("Ingrese el numero de corales en el habitat")
                profundidad = st.number_input("Ingrese la profundidad del habitat")
            elif nombre == "Selvatico":
                id = 3
                temperaturaMax = 40
                temperaturaMin = 21
                rocas = st.number_input("Ingrese el numero de rocas en el habitat")
                lianas = st.number_input("Ingrese el numero de lianas en el habitat")
            elif nombre =="Polar":
                id = 4
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
                        nuevo = habitatModel.Desertico(id, nombre, capacidad, temperaturaMax, temperaturaMin, oasis, captus)
                    elif nombre == "Acuatico":
                        nuevo = habitatModel.Acuatico(id, nombre, capacidad, temperaturaMax, temperaturaMin, corales, profundidad)
                    elif nombre == "Selvatico":
                        nuevo = habitatModel.Selvatico(id, nombre, capacidad, temperaturaMax, temperaturaMin, rocas, lianas)
                    elif nombre == "Polar":
                        nuevo = habitatModel.Polar(id, nombre, capacidad, temperaturaMax, temperaturaMin, hielo, iceberg)

                    st.success("El habitat fue creado")
                    return nuevo

    def menu_añadir_animal(self):

        posiblesH = []
        for habitat in self.modelZoo.habitats:
                posiblesH.append(habitat.nombre)

        with st.container():
            st.subheader("Añadir animal a un habitat")
            if len(self.modelZoo.registro) == 0:
                self.mensajeError("No hay animales")
            else:
                listaA = self.modelZoo.listarAnimales()
                probable = st.selectbox("Elija un animal", listaA)
                elegido = self.modelZoo.registro[listaA.index(probable)]

                if len(posiblesH) == 0:
                    self.mensajeError("No hay habitats")
                else:
                    probableH = st.selectbox("Elija un habitat", posiblesH)
                    elegidoH = self.modelZoo.listarHabitats(habitat.nombre)

                    boton_accion = st.button("Agregar animal a habitat")
                    if boton_accion:
                        elegidoH.agregarAnimalH(elegido)
                        self.modelZoo.eliminarAnimal(elegido)
                        self.mensajeExitoso("Animal agregado al habitat con exito")

    def listar(self):

        nombreH = []
        for habitat in self.modelZoo.habitats:
            opcion = habitat.nombre + " - " + str(habitat.capacidad)
            nombreH.append(opcion)

        with st.container():
            st.subheader("Lista Habitats Y animales")
            if len(self.modelZoo.habitats) == 0:
                st.error("No hay habitats en el zoologico")
            else:
                habitat = st.selectbox("Selecciona el habitat a listar", nombreH)
                animalesD = self.modelZoo.habitats[nombreH.index(habitat)].animales

                if len(animalesD) == 0:
                    self.mensajeError("No hay animales en este habitat")
                else:
                    boton_accion = st.button("Listar animales")
                    if boton_accion:
                        for animal in animalesD:
                            st.write(f"ID: {animal.id}")
                            st.write(f"Nombre: {animal.nombre}")
                            st.write(f"Especie: {animal.especie}")
                            st.write(f"Edad: {animal.edad}")
                            st.write(f"Dieta: {animal.dieta}")
                            st.write(f"Salud: {animal.salud}")
                            st.divider()

    def menu_realizar_accion(self):

        contiene = True
        for habitat in self.modelZoo.habitats:
            if len(habitat.animales) == 0:
                contiene = False

        if contiene:
             with st.container():
                st.subheader("Realizar accion")
                opciones = self.modelZoo.animalesHabitats()
                identificador = st.selectbox("Selecciona un animal: ", opciones)
                escogido = self.modelZoo.buscar(identificador)

                accion = st.selectbox("Seleccione una accion: ", "Dormir", "Comer", "Jugar")

                if accion == "Dormir":
                    horas = st.number_input("Ingrese las horas que duerme el animal")
                    if horas < 0:
                        self.mensajeError("Las horas deben ser mayores a 0")
                    elif horas > escogido.sueno:
                        self.mensajeError("Se pasa de las horas permitidas")
                    else:
                        boton_accion = st.button("Dormir")
                        if boton_accion:
                            if escogido.sueno + horas <= escogido.hDormir:
                                self.mensajeExitoso("El animal duerme")
                                escogido.sueno += horas
                            else:
                                self.mensajeError("No puede dormir tanto")
                elif accion == "Comer":
                    st.selectbox("Seleccione un alimento: ", self.modelZoo.dietas[escogido.dieta])
                    boton_accion = st.button("Comer")
                    if boton_accion:
                        self.mensajeExitoso("El animal esta Comiendo")

                elif accion == "Jugar":
                    if escogido.jugado:
                        self.mensajeError("El animal ya jugo hoy")
                    else:
                        boton_accion = st.button("Jugar")
                        if boton_accion:
                            self.mensajeExitoso("El animal esta jugando")
                            escogido.jugado = False



    def menu_añadir_alimento(self):

        with st.container():
            st.subheader("Agregar un alimento alimento")
            tipo = st.selectbox("Selecciona el tipo de dieta", self.modelZoo.dietas)
            alimento = st.text_input("Ingresa el nombre del alimento")

            boton_accion = st.button("Agregar comida")
            if boton_accion:
                self.modelZoo.agregarAlimento(alimento, tipo)
                self.mensajeExitoso("Agregaste un alimento")

    def menu_eliminar_alimento(self):

        with st.container():
            st.subheader("Eliminar un alimento alimento")
            tipo = st.selectbox("Selecciona el tipo de dieta", self.modelZoo.dietas)

            if len(self.modelZoo.dietas[tipo]) == 0:
                self.mensajeError("No hay alimentos")
            else:
                alimento = st.selectbox("Selecciona el alimento", self.modelZoo.dietas[tipo])
                boton_accion = st.button("Eliminar alimento")
                if boton_accion:
                    self.modelZoo.eliminarAlimento(alimento, tipo)
                    self.mensajeExitoso("Eliminaste un alimento")
    def mensajeExitoso(self, mensaje):
        st.success(mensaje)
    def mensajeError(self, mensaje):
        st.error(mensaje)

    def api(self):

        url = "https://pokeapi.co/api/v2/pokemon/"
        buscar = st.text_input("Ingrese un numero")
        boton_accion = st.button("Buscar")
        busqueda = rq.get(url + buscar)
        if boton_accion:
            if busqueda.status_code == 200:
                data = busqueda.json()
                for dato, nombre in data.items():
                    self.mensajeExitoso(dato)
                    st.write(nombre)
            else:
                self.mensajeError("No se encontro la informacion")