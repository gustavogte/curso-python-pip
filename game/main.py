# importa la libreria random
import random

# se establecen las opciones
options = ("piedra", "papel", "tijera")

# inicializamos los marcadores de user y pc
pc_wins = 0
user_wins = 0

# se inicializa el numero de rondas
rounds = 1

# se solicita el ingreso del nombre del jugador
user_name = input("Introduce tu nombre: ")

# se establece el ciclo para el juego
while True:
    # se muesta el numero de rondas
    print(" * " * 10)
    print(f" Ronda {rounds}")
    print(" * " * 10)

    # se captura la opción de jugador
    user_option = input("Elige una opción: \npiedra, papel o tijera => ").lower()
    # se valida que la opción del jugador sea valida
    if not user_option in options:
        print(f"La opción {user_option} no es válida")
        continue  # se continua el codigo para solicitar nuevamente la opción
    pc_option = random.choice(
        options
    )  # se seleciona de manera aleatoria la opción de la PC

    # se muestras las opciones seleccionadas por el usuario y pc
    print(f"User opcion => {user_option}")
    print(f"PC option => {pc_option}")

    # se evalua si el jugador y pc seleccionaron la misma opción
    if user_option == pc_option:
        print("empate")

    # se evaluan las opciones del jugador y pc para determinar el ganador
    elif user_option == "piedra":
        if pc_option == "tijera":
            print(f"{user_option} gana a {pc_option}, ganaste!")
            user_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )
        else:
            print(f"{pc_option} gana a {user_option}, gana PC")
            pc_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )

    elif user_option == "papel":
        if pc_option == "piedra":
            print(f"{user_option} gana a {pc_option}, ganaste!")
            user_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )
        else:
            print(f"{pc_option} gana a {user_option}, ganó PC")
            pc_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )

    elif user_option == "tijera":
        if pc_option == "papel":
            print(f"{user_option} gana a {pc_option}, ganaste!")
            user_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )
        else:
            print(f"{pc_option} gana a {user_option}, ganó PC")
            pc_wins += 1
            print(
                f"Marcador de la ronda {rounds}:\n {user_name} = {user_wins} | PC = {pc_wins}"
            )

    rounds += 1  # incrementa la ronda

    # si la pc gana dos rondas es el ganador
    if pc_wins == 2:
        print("El ganador de la ronda es la PC")
        break  # se rompe la ejecución
    # si el usuario gana dos rondas es el ganador
    if user_wins == 2:
        print(f"El ganador de la ronda es {user_name}")
        break  # se rompe la ejecución
