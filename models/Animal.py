class Animal:
    def __init__(self, id, nombre, especie, edad, dieta, salud, hDormir, cantidad, temperatura):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.dieta = dieta
        self.salud = salud
        self.hDormir = hDormir
        self.cantidad = cantidad
        self.temperatura = temperatura
        self.sueno = 0
        self.jugado = False
        self.comido = 0