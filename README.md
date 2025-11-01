# Computación 2025 - Backgammon

Nombre: Lucas Hugo Moran
Legajo: 64043

Este proyecto es una implementación completa del juego de mesa clásico Backgammon, desarrollado íntegramente en Python. Ofrece dos interfaces distintas: una robusta CLI (Command-Line Interface) para la lógica de consola y una GUI (Graphical User Interface) desarrollada con Pygame para una experiencia visual.

## Requisitos

- Python 3.10 o superior
- Pygame
- Requests
- Flask

## Instalación

1. Clona el repositorio en tu directorio de trabajo:

```bash
git clone https://github.com/lucas-hm/computacion-2025-backgammon-lucas-hm.git
```

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Ejecuta el archivo main.py:

```bash
python3 -m main.py
```

## Uso

El main muestra un menú de opciones para elegir entre la CLI y la GUI. La CLI se encarga de la lógica de juego y la GUI se encarga de la interfaz gráfica.

### CLI y GUI

La CLI se encarga de la lógica de juego y proporciona una interfaz de usuario simple para el usuario. Mientras que el pygame es una interfaz gráfica que se encarga de mostrar la partida en pantalla.

### Build and RUN the container

Build the container:

```bash
docker build -t backgammon-app .
```

Run the container:

```bash
docker run --name my-backgammon -it backgammon-app
```
