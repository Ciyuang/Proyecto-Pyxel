# ──────────────────────────────────────────────────────────────
# ░░ CONSTANTES VISUALES
# ──────────────────────────────────────────────────────────────

p = "🔲" # Muros
e = "  " # Espacios
s = "🤖" #Jugador
m = "🏁" # Meta 
t1 = "👺" # Trampa 1 
t2 = "👽" # Trampa 2
v  = " ♥️"

# ──────────────────────────────────────────────────────────────
# ░░ NIVELES DEL JUEGO COMO MATRICES
# ──────────────────────────────────────────────────────────────

laberinto1 = [
    [p, p, p, p, p, p, p, p, p, p],
    [p, s, e, e, e, e, e, e, e, p],
    [p, p, p, p, p, e, p, p, e, p],
    [p, e, e, e, e, e, p, e, e, p],
    [p, e, p, p, p, e, p, e, p, p],
    [p, e, p, t1, e, e, p, e, p, p],
    [p, e, p, p, p, p, p, e, p, p],
    [p, e, e, e, e, e, e, e, p, p],
    [p, p, p, p, p, p, p, e, e, p],
    [p, p, p, p, p, p, p, p, m, p]
]

laberinto2 = [
    [p, p, p, p, p, p, p, p, p, p, p],
    [p, s, e, e, e, p, t1, e, e, e, p],
    [p, p, p, e, p, p, p, e, p, e, p],
    [p, e, e, e, e, t1, p, e, p, e, p],
    [p, e, p, p, p, e, p, e, p, e, p],
    [p, e, p, t1, e, e, p, e, p, e, p],
    [p, e, p, p, p, p, p, e, p, e, p],
    [p, e, e, e, e, e, e, e, p, e, p],
    [p, p, t1, p, p, p, p, t1, p, e, p],
    [p, t1, e, e, e, e, e, e, e, e, m],
    [p, p, p, p, p, p, p, p, p, p, p]
]

laberinto3 = [
    [p, p, p, p, p, p, p, p, p, p, p, p],
    [p, s, e, e, e, t1, p, e, e, e, e, p],
    [p, t1, p, e, p, p, p, p, t1, p, e, p],
    [p, e, p, e, e, e, e, e, e, t1, e, p],
    [p, p, p, p, t1, p, p, p, e, p, p, p],
    [p, e, e, t1, e, p, e, e, e, e, e, p],
    [p, t1, p, e, p, p, p, e, p, t1, e, p],
    [p, e, e, t1, e, e, e, e, p, t1, t1, p],
    [p, p, e, p, p, e, p, p, p, p, e, p],
    [p, e, e, t1, e, e, e, e, e, e, e, p],
    [p, p, t1, p, p, p, t1, p, p, e, m, p],
    [p, p, p, p, p, p, p, p, p, p, p, p]
]

laberinto4 = [
    [p,p,p,p,p,p,p,p,p,p,p,p,p],
    [p,s,e,e,p,e,e,e,e,e,e,e,p],
    [p,e,p,e,p,e,p,p,p,p,p,e,p],
    [p,e,p,e,p,e,p,t1,e,t2,e,e,p],
    [p,e,p,e,p,e,p,e,p,p,p,e,p],
    [p,t2,p,e,e,e,e,e,p,t1,p,e,p],
    [p,p,p,p,p,p,p,p,p,e,p,e,p],
    [p,m,e,p,e,e,e,e,e,e,p,e,p],
    [p,p,e,p,e,p,e,p,p,p,p,e,p],
    [p,p,e,p,e,p,e,p,t1,e,t2,e,p],
    [p,p,e,p,e,p,e,p,p,p,p,e,p],
    [p,p,e,e,e,p,e,e,e,e,e,e,p],
    [p,p,p,p,p,p,p,p,p,p,p,p,p]
]

laberinto5 = [
    [p,p,p,p,p,p,p,p,p,p,p,p,p,p],
    [p,s,e,e,e,e,e,e,p,e,e,e,e,p],
    [p,p,p,p,p,e,p,e,p,e,p,p,e,p],
    [p,t2,p,e,e,e,p,e,e,e,p,e,e,p],
    [p,e,p,e,p,t1,p,p,p,p,p,e,p,p],
    [p,e,p,e,p,p,p,e,e,e,e,e,t2,p],
    [p,e,p,e,p,e,e,e,p,p,p,p,p,p],
    [p,e,e,e,p,e,p,p,p,e,e,t1,e,p],
    [p,p,p,p,p,e,p,t2,e,e,p,p,e,p],
    [p,t1,p,e,e,e,p,e,p,p,p,t2,e,p],
    [p,e,e,e,p,e,t1,e,p,t2,e,e,t2,p],
    [p,e,p,p,p,p,p,p,p,p,p,p,e,p],
    [p,e,e,e,e,e,e,e,e,e,e,e,m,p],
    [p,p,p,p,p,p,p,p,p,p,p,p,p,p]
]


laberinto6 = [
    [p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p],
    [p,s,e,e,e,e,p,e,e,e,e,e,e,e,e,e,e,e,p],
    [p,p,p,p,p,e,p,e,p,p,p,p,p,p,p,p,p,e,p],
    [p,e,e,e,p,e,p,e,p,e,e,e,e,e,p,t1,p,e,p],
    [p,e,p,e,p,e,p,e,p,e,p,p,p,e,p,e,p,e,p],
    [p,e,p,e,p,e,e,e,p,e,p,t2,p,e,e,t1,p,e,p],
    [p,e,p,e,p,p,p,p,p,e,p,e,p,e,p,p,p,e,p],
    [p,e,p,e,e,e,e,e,e,e,p,e,p,e,p,e,e,e,p],
    [p,e,p,e,p,t1,p,p,p,p,p,t2,p,e,p,e,p,p,p],
    [p,e,p,e,p,e,e,e,p,t2,e,e,e,e,p,e,e,e,p],
    [p,e,p,e,p,p,p,e,p,p,p,p,p,e,p,p,p,e,p],
    [p,e,p,e,e,e,p,e,e,e,e,e,e,e,e,e,e,e,p],
    [p,p,p,p,p,e,p,p,p,p,p,p,p,p,p,p,p,p,p],
    [p,t2,e,e,p,e,e,e,e,e,e,e,e,e,e,e,e,e,p],
    [p,p,p,e,p,p,p,p,p,p,p,p,p,p,p,p,p,e,p],
    [p,e,e,e,e,e,p,e,e,e,e,e,e,e,e,e,p,e,p],
    [p,e,p,p,p,e,p,e,p,e,p,p,p,e,p,e,p,e,p],
    [p,e,e,m,p,e,e,e,p,e,t1,e,e,e,p,e,e,e,p],
    [p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p]
]


laberinto7 = [
    [p,e,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p],
    [p,e,e,e,p,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,p],
    [p,e,p,e,p,e,p,p,p,p,p,p,p,p,p,p,p,p,p,e,p],
    [p,e,p,e,p,e,p,t1,p,e,e,e,e,e,e,e,e,e,e,e,p],
    [p,e,p,e,p,e,p,e,p,e,p,p,p,p,p,e,p,e,p,e,p],
    [p,e,p,e,e,e,p,e,p,e,p,t2,e,e,p,e,p,t1,p,e,p],
    [p,e,p,p,p,p,p,e,p,e,p,p,p,e,p,e,p,p,p,e,p],
    [p,e,p,t2,e,e,e,e,p,e,e,t1,p,e,p,e,e,e,p,e,p],
    [p,t1,p,p,p,e,p,e,p,p,p,e,p,e,p,p,p,e,p,e,p],
    [p,e,e,e,p,e,p,e,e,e,e,e,p,e,p,e,e,e,p,e,p],
    [p,p,p,e,p,e,p,p,p,p,p,p,p,e,p,e,p,p,p,e,p],
    [p,e,e,e,p,e,p,t1,e,e,e,e,e,e,p,e,p,e,e,e,p],
    [p,e,p,p,p,e,p,p,p,e,p,p,p,p,p,e,p,e,p,e,p],
    [p,e,p,e,e,e,e,e,e,e,p,e,e,e,e,e,e,p,t2,e,p],
    [p,e,p,e,p,p,p,p,p,p,p,e,p,p,p,e,p,e,p,p,p],
    [p,e,p,t1,p,e,p,p,p,t2,p,e,e,e,p,t2,p,e,e,t1,p],
    [p,e,p,p,p,e,p,p,p,e,p,e,p,e,p,p,p,p,p,e,p],
    [p,e,e,e,e,e,p,t1,e,e,p,t2,p,e,e,e,e,e,e,e,p],
    [p,p,p,p,p,p,p,e,p,p,p,p,p,p,p,p,p,e,p,p,p],
    [p,e,e,s,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,t1,p],
    [p,p,p,m,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p]
]





niveles = [laberinto1, laberinto2, laberinto3, laberinto4, laberinto5, laberinto6, laberinto7]

# ──────────────────────────────────────────────────────────────
# ░░ FUNCIONES DE ACTUALIZACION E IMPRESION EN CONSOLA
# ──────────────────────────────────────────────────────────────

def limpiar():
    """Limpia la consola usando secuencias ANSI. Compatible con terminales modernas."""
    print("\033[H\033[J", end="")

def mostrar_laberinto(laberinto, vidas, nivel_actual):
    limpiar()  # Borra la pantalla antes de dibujar el nuevo estado

    # Mostrar cada fila del laberinto en consola
    for fila in laberinto:
        print("".join(fila))
    print()
    # Mostrar el número de nivel actual sobre las vidas
    print(f"NIVEL: {nivel_actual + 1}\nVIDAS:{v * vidas}")

# ──────────────────────────────────────────────────────────────
# ░░ INTERFAZ DEL JUEGO
# ──────────────────────────────────────────────────────────────

def pantalla_titulo():
    limpiar()
    print("\n\n")
    print("██████╗ ██╗   ██╗██╗   ██╗███████╗██╗      ██████╗  ██████╗████████╗")
    print("██╔══██╗██║   ██║ ██║ ██╔╝██╔════╝██║     ██╔═══██║██╔════╝╚══██╔══╝")
    print("██████╔╝██║   ██║   ██ ╔╝ █████╗  ██║     ██║   ██║ ██████╗   ██║   ")
    print("██╔═══╝ ██║   ██║ ██╔═██╗ ██╔══╝  ██║     ██║   ██║      ██╗  ██║   ")
    print("██║       ██████║██║   ██╗███████╗███████╗╚██████╔╝███████╔╝  ██║   ")
    print("╚═╝          ██╔╝╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ")
    print("        ██  ██╔╝")
    print("         ████╔╝")
    print("         ╚═══╝")
    print("\nBienvenido a *Laberintos PYXELOST*\n")
    input("Presione una tecla para continuar...")

def menu_principal():
    """Muestra el menú principal y devuelve la opción elegida."""
    limpiar()
    print("════════════════════════════════════════════════════════")
    print(" __  __                ___     _         _            _ ")
    print("|  \/  |___ _ _ _  _  | _ \_ _(_)_ _  __(_)_ __  __ _| |")
    print("| |\/| / -_) ' \ || | |  _/ '_| | ' \/ _| | '_ \/ _` | |")
    print("|_|  |_\___|_||_\_,_| |_| |_| |_|_||_\__|_| .__/\__,_|_|")
    print("                                          |_|           ")
    print("════════════════════════════════════════════════════════")
    print()
    print("1. INICIAR")
    print("2. ELEGIR UN NIVEL")
    print("3. CREDITOS")
    print("4. REGLAS")
    print("════════════════════════════════════════════════════════")
    print()
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if opcion in [1, 2, 3, 4]:
                return opcion
        except ValueError:
            pass
        print("Opción inválida. Intenta nuevamente.")

def elegir_nivel():
    """Permite al jugador elegir un nivel específico del listado."""
    limpiar()
    print("═════════════════════════")
    print(" _  _ _         _        ")
    print("| \| (_)_ _____| |___ ___")
    print("| .` | \ V / -_) / -_|_-<")
    print("|_|\_|_|\_/\___|_\___/__/")
    print()
    print("═════════════════════════")
    for i in range(len(niveles)):
        print(f"{i+1}. NIVEL {i+1}")
    print("═════════════════════════")
    while True:
        try:
            nivel = int(input("¿Qué nivel deseas jugar? "))
            if 1 <= nivel <= len(niveles):
                return nivel-1 
        except ValueError:
            pass
        print("Nivel inválido.")

def felicidades():
    limpiar()
    print(" ______   ______   __        ________  ______    ________  ______   ________   ______   ______   ______      ")
    print("/_____/\ /_____/\ /_/\      /_______/\/_____/\  /_______/\/_____/\ /_______/\ /_____/\ /_____/\ /_____/\     ")
    print("\::::_\/_\::::_\/_\:\ \     \__.::._\/\:::__\/  \__.::._\/\:::_ \ \\::: _  \ \\:::_ \ \\::::_\/_\::::_\/_    ")
    print(" \:\/___/\\:\/___/\\:\ \       \::\ \  \:\ \  __   \::\ \  \:\ \ \ \\::(_)  \ \\:\ \ \ \\:\/___/\\:\/___/\   ")
    print("  \:::._\/ \::___\/_\:\ \____  _\::\ \__\:\ \/_/\  _\::\ \__\:\ \ \ \\:: __  \ \\:\ \ \ \\::___\/_\_::._\:\  ")
    print("   \:\ \    \:\____/\\:\/___/\/__\::\__/\\:\_\ \ \/__\::\__/\\:\/.:| |\:.\ \  \ \\:\/.:| |\:\____/\ /____\:\ ")
    print("    \_\/     \_____\/ \_____\/\________\/ \_____\/\________\/ \____/_/ \__\/\__\/ \____/_/ \_____\/ \_____\/ ")
    print("                             \n🎉🎊HA COMPLETADO TODOS LOS NIVELES DEL JUEGO🎊🎉\n")
    print("🤓 SE GANO UN CALAO 🤓\n")
    
    while True:
        respuesta = input("¿Desea volver al menú principal? (si/no): ").lower()
        if respuesta == "si":
            return menu_principal()
        elif respuesta == "no":
            creditos()
            break

def creditos():
    limpiar()
    print("════════════════════════════════")
    print("  ___            _ _ _          ")
    print(" / __|_ _ ___ __| (_) |_ ___ ___")
    print("| (__| '_/ -_) _` | |  _/ _ (_-<")
    print(" \___|_| \___\__,_|_|\__\___/__/")
    print("")
    print("════════════════════════════════")
    print("Desarrolladores:")
    print("👾 Fabian Camilo Linares Villalba")
    print("👾 Erick")
    print("👾 Juan Carlos Polania Bolivar")
    print("💻  Proyecto: Juego de Laberinto en Python (PYXELOST)")
    print("🎓 Carrera: Ingeniería Civil")
    print("¡Gracias por jugar!\n")
    print("════════════════════════════════")

    while True:
        respuesta = input("¿Desea volver al menú principal? (si/no): ").lower()
        if respuesta == "si":
            return menu_principal()
        elif respuesta == "no":
            creditos()
            break

def reglas():
    limpiar()
    print("════════════════════════")
    print(" ___          _         ")
    print("| _ \___ __ _| |__ _ ___")
    print("|   / -_) _` | / _` (_-<")
    print("|_|_\___\__, |_\__,_/__/")
    print("        |___/           ")
    print("")
    print("════════════════════════")
    print("El movimiento del jugador se realiza con las teclas W, A, S, D")
    print("Las paredes corresponden al caracter 🔲")
    print("El jugador corresponde al caracter 🤖")
    print("Las trampas corresponden a los caracteres 👺 y👽")
    print("El jugador debe llegar a la linea de meta para completar el juego o pasar de nivel 🏁")
    print("El jugador mantiene la cantidad de vidas desde el primero al ultimo nivel")
    print("Si el jugador pierde todas sus vidas este debera volver a empezar desde el nivel 1")
    print("")
    print("═══════════════════════════════")

    while True:
        respuesta = input("¿Desea volver al menú principal? (si/no): ").lower()
        if respuesta == "si":
            return menu_principal()
        elif respuesta == "no":
            creditos()
            break

# ──────────────────────────────────────────────────────────────
# ░░ LÓGICA DEL JUEGO
# ──────────────────────────────────────────────────────────────

def obtener_movimiento(fila, col):
    """Recibe la entrada del jugador y calcula nueva posición tentativa."""
    movimiento = input("MOVIMIENTO (WASD): ").lower()
    if movimiento == "w": 
        return fila - 1, col
    elif movimiento == "s": 
        return fila + 1, col
    elif movimiento == "a": 
        return fila, col - 1
    elif movimiento == "d": 
        return fila, col + 1
    return fila, col  # Movimiento inválido: sin cambio


def procesar_movimiento(laberinto, fila_actual, col_actual, fila_nueva, col_nueva, vidas):
    # Verificar si la nueva posición está dentro del laberinto
    if fila_nueva < 0 or fila_nueva >= len(laberinto):
        # Si se sale por arriba o por abajo, no se mueve
        return fila_actual, col_actual, vidas, False
    if col_nueva < 0 or col_nueva >= len(laberinto[fila_nueva]):
        # Si se sale por los lados, tampoco se mueve
        return fila_actual, col_actual, vidas, False

    # Revisar qué hay en la nueva posición
    destino = laberinto[fila_nueva][col_nueva]

    # Verificar si el destino es una pared u obstáculo bloqueado
    if destino != e and destino != m and destino != t1 and destino != t2:
        # Si no es un espacio vacío, una meta o una trampa, no se mueve
        return fila_actual, col_actual, vidas, False

    # Si pisa una trampa, perder una vida
    if destino == t1 or destino == t2:
        vidas = vidas - 1  # Se resta una vida
        if vidas == 0:
            # Si ya no tiene vidas, el juego termina
            limpiar()
            print("☠️ GAME OVER ☠️\n")
            input("Presione una tecla para volver al menú...")
            return fila_actual, col_actual, 0, "game_over"

    # Mover al jugador
    laberinto[fila_actual][col_actual] = e  # Se borra la posición anterior
    laberinto[fila_nueva][col_nueva] = s    # Se pone el jugador en la nueva posición

    # Revisar si llegó a la meta
    if destino == m:
        return fila_nueva, col_nueva, vidas, "nivel_completado"

    # Movimiento válido normal (a espacio vacío o trampa no mortal)
    return fila_nueva, col_nueva, vidas, True

def jugar(nivel_actual, vidas):
    # Mientras el jugador no haya terminado todos los niveles
    while nivel_actual < len(niveles):

        # Obtener el laberinto del nivel actual como una nueva copia (matriz)
        laberinto = []
        for fila in niveles[nivel_actual]:
            laberinto.append(list(fila))

        # Buscar dónde está el jugador (símbolo 's')
        for i in range(len(laberinto)):
            for j in range(len(laberinto[i])):
                if laberinto[i][j] == s:
                    fila_jugador = i
                    col_jugador = j

        # Este bucle controla el turno del jugador dentro de un nivel
        while True:
            # Mostrar el laberinto en pantalla y las vidas restantes
            mostrar_laberinto(laberinto, vidas, nivel_actual)

            # Obtener hacia dónde se quiere mover el jugador
            nueva_fila, nueva_col = obtener_movimiento(fila_jugador, col_jugador)

            # Procesar ese movimiento y ver qué ocurre
            fila_jugador, col_jugador, vidas, resultado = procesar_movimiento(
                laberinto, fila_jugador, col_jugador, nueva_fila, nueva_col, vidas
            )

            # Revisar el resultado del movimiento
            if resultado == "game_over":
                # Si el jugador perdió todas las vidas, vuelve al menú
                return "menu", 0

            elif resultado == "nivel_completado":
                return "nivel_completado", vidas


# ──────────────────────────────────────────────────────────────
# ░░ PUNTO DE ENTRADA DEL JUEGO
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Muestra la pantalla de bienvenida cuando se ejecuta el programa
    pantalla_titulo()

    # Bucle principal del juego: se repite hasta que el jugador elija salir
    while True:
        # Muestra el menú principal y guarda la opción que elija el jugador
        opcion = menu_principal()

        # Opción 1: Jugar desde el primer nivel
        if opcion == 1:
            nivel_actual = 0     # Empezar desde el primer nivel (índice 0)
            vidas = 3            # Inicializar vidas en 3

            # Bucle de niveles: continúa hasta que se terminen los niveles o el jugador pierda
            while nivel_actual < len(niveles):
                resultado, vidas = jugar(nivel_actual, vidas)

                # Si el jugador pierde todas las vidas o elige salir, volver al menú
                if resultado == "menu":
                    break
                elif resultado == "nivel_completado":
                    nivel_actual += 1
                    if nivel_actual == len(niveles):
                        felicidades()
                        break
                elif resultado == "salir":
                    creditos()
                    break
                else:
                    break  # Por seguridad, si ocurre otro resultado inesperado

        # Opción 2: Jugar un nivel específico
        elif opcion == 2:
            # Permite al jugador elegir un nivel de la lista
            nivel_actual = elegir_nivel()
            vidas = 3  # Las vidas se inicializan igual
            resultado, vidas= jugar(nivel_actual, vidas)

            # Solo si el jugador no eligió volver al menú directamente,
            # y si aún quedan niveles después del que eligió manualmente
            if resultado != "menu" and nivel_actual + 1 < len(niveles):

                # Se le pregunta si desea continuar con los niveles que siguen (en orden)
                continuar = input("¿Deseas continuar con los siguientes niveles? (s/n): ").lower()

                if continuar == "s":
                    # Avanza al siguiente nivel
                    nivel_actual += 1
                    if nivel_actual == len(niveles):
                        felicidades()
                        break

                    # Bucle para continuar con el resto de niveles
                    while nivel_actual < len(niveles):
                        # Se juega el siguiente nivel
                        resultado, vidas = jugar(nivel_actual, vidas)

                        # Si el jugador decide volver al menú en medio del juego, se rompe el ciclo
                        if resultado == "menu":
                            break
                        elif resultado == "nivel_completado":
                            nivel_actual += 1

                            # Si el jugador terminó el último nivel
                        elif nivel_actual == len(niveles):
                            felicidades()
                            break
                else:
                    # Si el jugador no desea continuar, vuelve al menú principal
                    continue


        # Opción 3: Ver los créditos y salir del juego
        elif opcion == 3:
            creditos()  # Muestra los créditos del juego
            break        # Sale del bucle principal y finaliza el programa

        elif opcion == 4:
            reglas()
            break