import streamlit as st
class Zoo:
    def __init__(self):

        if "dietas" in st.session_state:
            self.dietas = st.session_state["dietas"]
        else:
            self.dietas = {"carnivoro": [], "herbivoro": [], "omnivoro": []}

        if "habitats" in st.session_state:
            self.habitats = st.session_state["habitats"]
        else:
            self.habitats = []
            st.session_state["habitats"] = []

        if "registro" in st.session_state:
            self.registro = st.session_state["registro"]
        else:
            self.registro = []
            st.session_state["registro"] = []

        self.nombreHabitats = ["Desertico", "Acuatico", "Selvatico", "Polar"]

    def agregarHabitat(self, habitat):
        self.habitats.append(habitat)
        st.session_state["habitats"] = self.habitats

    def agregarAnimal(self, animal):
        self.registro.append(animal)
        st.session_state["registro"] = self.registro

    def eliminarAnimal(self, animal):
        self.registro.remove(animal)
        st.session_state["registro"] = self.registro

    def agregarAlimento(self, alimento, tipo):
        self.dietas[tipo].append(alimento)
        st.session_state["dietas"] = self.dietas

    def eliminarAlimento(self, alimento, tipo):
        self.dietas[tipo].remove(alimento)
        st.session_state["dietas"] = self.dietas

    def listarHabitats(self, nombre):
        for habitat in self.habitats:
            if habitat.nombre == nombre:
                return habitat
    def listarAnimales(self):
        nombre = []
        for animal in self.registro:
            agregar = animal.nombre + " - " + animal.especie
            nombre.append(agregar)
        return nombre
    def animalesHabitats(self):
        lista = []
        for habitat in self.habitats:
            for animal in habitat.animales:
                lista.append(animal.nombre)
        return lista

