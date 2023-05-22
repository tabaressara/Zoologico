import models.Animal as animalModel
import models.Habitat as habitatModel
import models.Zoologico as zoologicoModel
import controller.controllerZoo as zooController

class vistaZoo():

    def __init__(self):
        self.nuevo = zoologicoModel.Zoo()
        self.control = zooController.controllerZoo(self.nuevo, self)
    def solicitar_dato(self, mensaje):
        return input(mensaje)