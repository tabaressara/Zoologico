# Simulador de Zoológico 
Este proyecto consiste en la implementación de un
programa en Python que simula el funcionamiento de un zoológico. El
programa utiliza los conceptos de programación orientada a objetos,
incluyendo la creación de clases, relaciones, herencia, sobrescritura,
sobrecarga, modificadores de acceso e interfaces gráficas.

## Funcionalidades del programa 
### El programa permite al usuario realizar las siguientes acciones:

- Crear animales en el registro del zoológico: Permite al usuario crear
nuevos animales para agregarlos al zoológico. Se deben proporcionar
detalles como el nombre, la especie y el hábitat al que pertenecerá el
animal.

- Añadir un nuevo hábitat al zoológico: Permite al usuario crear un nuevo
hábitat y agregarlo al zoológico. El programa ofrece una selección de
tipos de hábitat predefinidos, como desértico, selvático, polar y
acuático. Cada hábitat tiene características específicas, como la
temperatura, la dieta y la capacidad máxima de animales.

- Añadir un nuevo animal a un hábitat existente: Permite al usuario
agregar un nuevo animal a un hábitat existente en el zoológico. El
programa verifica si el hábitat cumple con las condiciones necesarias
para alojar al animal y si hay espacio disponible.

- Listar hábitats y animales: Permite al usuario ver la lista de todos los
hábitats del zoológico y los animales que se encuentran en cada uno de
ellos. Se muestra información detallada de cada animal, como su nombre,
edad, tipo de alimentación y estado de salud.

- Realizar acciones en animales: Permite al usuario realizar acciones
específicas en un animal seleccionado. Las acciones disponibles son:
comer (verificando si el alimento es adecuado para el tipo de dieta del
animal), dormir (especificando el número de horas y verificando si es
suficiente tiempo para el animal) y jugar (indicando si el animal ya ha
jugado en el día).

- Administrar alimentos: Permite al usuario agregar y editar diferentes
tipos de alimentos para los animales en el zoológico. Los alimentos se
asignan según el tipo de dieta de cada animal (carnívoro, herbívoro u
omnívoro).

- Consulta en línea mediante API: El programa permite realizar consultas
en línea utilizando una API para obtener información relevante para el
zoológico, como datos sobre especies de animales o características de
hábitats específicos.

## El programa también maneja errores de entrada y salida de datos, proporcionando mensajes de error y solicitando al usuario que ingrese datos válidos cuando sea necesario.

### Implementación
El programa se implementa utilizando el lenguaje de
programación Python y hace uso de la biblioteca Streamlit para crear una
interfaz gráfica interactiva. La implementación sigue los principios de
programación orientada a objetos, utilizando clases para representar los
animales, hábitats y otras entidades del zoológico. Se aplican conceptos
como la herencia y la sobrescritura de métodos para modelar las
relaciones entre las diferentes clases.

El programa se despliega en la nube utilizando las funcionalidades
proporcionadas por Streamlit, lo que permite acceder al simulador del
zoológico a través de un navegador web sin necesidad de instalar el
programa localmente.
