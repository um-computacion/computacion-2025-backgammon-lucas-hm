import pygame
import sys
import random
import os

# Importar las clases de lógica del juego
from core.dice import Dice
from core.tablero import board
from core.jugador import Jugador
from core.juego import Juego

# --- Configuración de Pygame ---
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
CAPTION = "Backgammon en Pygame"
FPS = 60

# Colores (R, G, B)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
GRIS_CLARO = (200, 200, 200)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)


class GameGUI:
    """Clase principal para la interfaz gráfica del juego."""
    def __init__(self):
        """Inicializa la interfaz gráfica del juego."""
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        pygame.display.set_caption(CAPTION)
        self.reloj = pygame.time.Clock()
        self.juego = Juego()  # Instancia de la lógica del juego
        self.fuente_base = pygame.font.Font(None, 24)
        self.dados_resultado = []
        self.estado_juego = "ESPERANDO_DADOS"
        self.corriendo = False
        
        self._cargar_imagen_tablero()
        self._inicializar_jugadores()

    def _cargar_imagen_tablero(self):
        """Carga la imagen del tablero desde el archivo."""
        self.imagen_tablero = None
        try:
            ruta_imagen = os.path.join("assets", "Tablero.png")
            imagen_cargada = pygame.image.load(ruta_imagen).convert()
            self.imagen_tablero = pygame.transform.scale(
                imagen_cargada, (ANCHO_PANTALLA, ALTO_PANTALLA)
            )
            print("Imagen de tablero cargada exitosamente.")
        except (pygame.error, FileNotFoundError) as error:
            print(f"ERROR: No se pudo cargar la imagen del tablero. Error: {error}")
            self.imagen_tablero = None

    def _inicializar_jugadores(self):
        """Inicializa los jugadores para la interfaz gráfica."""
        # Simulación de inicialización de jugadores
        self.juego.jugadores.nombre1 = "Jugador 1"
        self.juego.jugadores.nombre2 = "Jugador 2"
        self.juego.jugadores.color1 = "○"
        self.juego.jugadores.color2 = "●"
        self.juego.jugadores = {
            "B": {"nombre": "Jugador 1 (Blancas)", "color": "B"},
            "N": {"nombre": "Jugador 2 (Negras)", "color": "N"},
        }

    def dibujar_tablero(self):
        """Dibuja la representación gráfica del tablero de Backgammon."""
        # Dibujar la imagen de fondo primero
        if self.imagen_tablero:
            self.pantalla.blit(self.imagen_tablero, (0, 0))
        else:
            self.pantalla.fill(GRIS_CLARO)
            
        self._dibujar_estructura_tablero()
        self._dibujar_estado_juego()
        self._dibujar_puntos_tablero()

    def _dibujar_estructura_tablero(self):
        """Dibuja la estructura básica del tablero."""
        pygame.draw.rect(
            self.pantalla, NEGRO, 
            (20, 20, ANCHO_PANTALLA - 40, ALTO_PANTALLA - 40), 2
        )
        pygame.draw.line(
            self.pantalla, NEGRO, 
            (ANCHO_PANTALLA // 2, 20), 
            (ANCHO_PANTALLA // 2, ALTO_PANTALLA - 20), 2
        )

    def _dibujar_estado_juego(self):
        """Dibuja el estado del juego (barra, fuera, turno, dados)."""
        # Información de barra y fuera
        textos_estado = [
            (f"Barra B: {len(self.juego.tablero.barra_blancas)}", 40, AZUL),
            (f"Barra N: {len(self.juego.tablero.barra_negras)}", 60, ROJO),
            (f"Fuera B: {len(self.juego.tablero.fuera_blancas)}", 90, AZUL),
            (f"Fuera N: {len(self.juego.tablero.fuera_negras)}", 110, ROJO),
        ]
        
        for texto, pos_y, color in textos_estado:
            superficie = self.fuente_base.render(texto, True, BLANCO, color)
            self.pantalla.blit(superficie, (ANCHO_PANTALLA - 150, pos_y))

        # Turno actual
        jugador_actual = self.juego.obtener_jugador_actual()
        texto_turno = self.fuente_base.render(
            f"Turno: {jugador_actual['nombre']} ({self.juego.turno_actual})",
            True, NEGRO
        )
        self.pantalla.blit(texto_turno, (20, 20))

        # Dados
        if self.dados_resultado:
            dados_texto = f"Dados: {', '.join(map(str, self.dados_resultado))}"
        else:
            dados_texto = "Presiona ESPACIO para tirar dados"
            
        texto_dados = self.fuente_base.render(dados_texto, True, NEGRO)
        self.pantalla.blit(texto_dados, (20, 50))

    def _dibujar_puntos_tablero(self):
        """Dibuja los puntos del tablero con sus fichas."""
        x_start_izq = 50
        x_start_der = ANCHO_PANTALLA // 2 + 30
        y_start = 50

        # Puntos 1-12 (Abajo)
        for i in range(1, 13):
            x_pos = x_start_izq + ((i - 1) * 25 if i <= 6 else (i - 1) * 25 + 20)
            fichas_str = "".join(self.juego.tablero.celda[i])
            texto_punto = self.fuente_base.render(f"{i}: {fichas_str}", True, NEGRO)
            self.pantalla.blit(texto_punto, (x_pos, ALTO_PANTALLA - y_start))

        # Puntos 13-24 (Arriba)
        for i in range(13, 25):
            if i <= 18:
                j = 24 - i
                x_pos = x_start_izq + (j * 25)
            else:
                j = 24 - i
                x_pos = x_start_der + ((j - 6) * 25)

            fichas_str = "".join(self.juego.tablero.celda[i])
            texto_punto = self.fuente_base.render(f"{i}: {fichas_str}", True, NEGRO)
            self.pantalla.blit(texto_punto, (x_pos, y_start))

    def manejar_eventos(self):
        """Maneja los eventos de Pygame."""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.corriendo = False
            elif evento.type == pygame.KEYDOWN:
                self._manejar_teclas_presionadas(evento)

    def _manejar_teclas_presionadas(self, evento):
        # Teclas de control
        """Maneja las teclas presionadas durante el juego."""
        if evento.key == pygame.K_SPACE and self.estado_juego == "ESPERANDO_DADOS":
            self._tirar_dados()
        elif (evento.key == pygame.K_m and 
            self.estado_juego == "HACIENDO_MOVIMIENTOS" and 
            self.dados_resultado):
            self._procesar_movimiento_prueba()

    def _tirar_dados(self):
        """Simula el lanzamiento de dados."""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        # Si los dados son iguales, se simulan 4 movimientos de ese dado
        if dado1 == dado2:
            self.dados_resultado = [dado1, dado1, dado1, dado1]
            print(f"DOBLES {dado1}! {self.juego.turno_actual} tiene 4 movimientos de {dado1}")
        else:
            self.dados_resultado = [dado1, dado2]
            print(f"{self.juego.turno_actual} tira {dado1} y {dado2}")
            
        self.estado_juego = "HACIENDO_MOVIMIENTOS"

    def _procesar_movimiento_prueba(self):
        """Procesa un movimiento de prueba cuando se presiona M."""
        if self.juego.tablero.puede_mover_desde_barra(self.juego.turno_actual):
            self._mover_desde_barra()
        else:
            self._mover_ficha_normal()
            
        self._verificar_fin_turno()
        self._verificar_victoria()

    def _mover_desde_barra(self):
        """Intenta mover una ficha desde la barra."""
        dado_usar = self.dados_resultado[0]
        punto_destino = dado_usar if self.juego.turno_actual == "B" else 25 - dado_usar
        exito, mensaje = self.juego.procesar_movimiento(0, punto_destino, dado_usar)
        print(f"Intento de mover desde barra: {mensaje}")
        if exito:
            self.dados_resultado.pop(0)

    def _mover_ficha_normal(self):
        """Intenta mover una ficha normal."""
        dado_usar = max(self.dados_resultado)
        desde, hasta = self._encontrar_movimiento_simple(dado_usar)

        if desde is not None:
            exito, mensaje = self.juego.procesar_movimiento(desde, hasta, dado_usar)
            print(f"Intento de mover {desde} a {hasta}: {mensaje}")
            if exito:
                self.dados_resultado.remove(dado_usar)
        else:
            print("No se encontró un movimiento simple para el dado más grande.")

    def _verificar_fin_turno(self):
        """Verifica si el turno ha terminado."""
        if not self.dados_resultado:
            print(f"Fin del turno para {self.juego.turno_actual}")
            self.juego.cambiar_turno()
            self.estado_juego = "ESPERANDO_DADOS"

    def _verificar_victoria(self):
        """Verifica si hay un ganador."""
        ganador, color_ganador = self.juego.tablero.win_conditions()
        if ganador:
            nombre_ganador = self.juego.jugadores[color_ganador]["nombre"]
            print(f"\n¡Felicidades {nombre_ganador}! Has ganado el juego.")
            self.corriendo = False

    def _encontrar_movimiento_simple(self, dado):
        """Busca el primer movimiento válido simple para el jugador actual."""
        jugador = self.juego.turno_actual
        fichas_jugador = "○" if jugador == "B" else "●"
        
        puntos_busqueda = range(24, 0, -1) if jugador == "B" else range(1, 25)
        
        for desde in puntos_busqueda:
            if (self.juego.tablero.celda[desde] and 
                self.juego.tablero.celda[desde][0] == fichas_jugador):    
                movimiento_valido = self._verificar_movimiento_valido(desde, dado, jugador)
                if movimiento_valido:
                    return movimiento_valido
        return None, None

    def _verificar_movimiento_valido(self, desde, dado, jugador):
        """Verifica si un movimiento es válido."""
        hasta = desde + dado if jugador == "B" else desde - dado
        # Verificar bear off
        if self._es_bear_off_valido(desde, hasta, jugador, dado):
            valido, _ = self.juego.tablero.movimiento_valido(desde, 25, jugador, dado)
            if valido:
                return desde, 25
        # Verificar movimiento normal
        if 1 <= hasta <= 24:
            valido, _ = self.juego.tablero.movimiento_valido(desde, hasta, jugador, dado)
            if valido:
                return desde, hasta
        return None

    def _es_bear_off_valido(self, desde, hasta, jugador, dado):
        """Verifica si un bear off es válido."""
        if jugador == "B" and hasta > 24:
            return (self.juego.tablero.puede_sacar(jugador) and 
                    (25 - desde) == dado)
        elif jugador == "N" and hasta < 1:
            return (self.juego.tablero.puede_sacar(jugador) and 
                    desde == dado)
        return False

    def ejecutar(self):
        """Bucle principal del juego."""
        self.corriendo = True
        while self.corriendo:
            self.manejar_eventos()
            self.dibujar_tablero()
            pygame.display.flip()
            self.reloj.tick(FPS) 
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    juego_gui = GameGUI()
    juego_gui.ejecutar()
