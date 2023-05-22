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

    def alimentoPermitido(self, alimento, tipo):
        for i in range(len(self.dietas[tipo])):
            if self.dietas[tipo][i] == alimento:
                return i
        return -1

    def agregarAlimento(self, alimento, tipo):
        self.dietas[tipo].append(alimento)
        st.session_state["dietas"] = self.dietas

    def eliminarAlimento(self, alimento, tipo):
        self.dietas[tipo].remove(alimento)
        st.session_state["dietas"] = self.dietas

    def repetidos(self, nombre):
        for habitat in self.habitats:
            if nombre == habitat.nombre:
                return True
