import numpy as np

def crearMapa(n, m, obstacles_count, lakes_count, show_levels=True):
    """
    crearMapa:
        función que dados los parámetros n, m, obstacles_count, lakes_count y show_levels, crea un mapa topográfico
        hecho aleatoriamente con strings.

    ----- Parameters -----
    :param n: Valor entero mayor a 2 que representa el tamaño de la dimensíon x del mapa
    :param m: Valor entero mayor a 2 que representa el tamaño de la dimensíon y del mapa
    :param obstacles_count:  Valor entero del total de obstáculos que deben ser incluídos en el mapa
    :param lakes_count: Integer Valor entero del total de lagos que deben ser incluidos en el mapa
    :param show_levels: Valor booleano que indica si se deben mostrar los niveles topográficos del mapa, se muestran por default
    :return: String del mapa y la ubicación unidimensional del rover
    """
    if n*m < 9 or lakes_count + obstacles_count + 1 > (n-2)*(m-2):
        return "No se puede crear ese mapa con ese número de obstáculos y lagos. Intenta otra combinación en la que quepan los lagos, obstáculos y la nave."
    map = ""
    obstacle = "*"
    lake = "_"
    levels = ["0", "1", "2", "3", "4", "5"]
    used_space = []
    count_used_places = 0
    rover = "Q"
    ubi_rover = 0
    print(f"\nNave: {rover}\nObstáculos: {obstacle}\nLagos: {lake}\n")

    #---------- Creación del mapa con los bordes -----------

    for i in range(n):
        for j in range(m):
            if i == n - 1 or i == 0 or j == 0 or j == m - 1:
                map += "#"
                used_space.append(count_used_places)
            elif show_levels:
                map += np.random.choice(levels)
            else:
                map += " "
            count_used_places += 1
        map += "\n"
        if i < n - 1:
            used_space.append(count_used_places)
            count_used_places += 1

    #----------- Insertamos los objetos aleatoriamente en el string -----------
    for i in range(lakes_count + obstacles_count + 1):
        random_place = np.random.randint(0, n*m)
        while random_place in used_space:
            random_place = np.random.randint(0, n * m)
        if i < lakes_count:
            map = map[:random_place] + lake + map[random_place+1:]
        elif i < obstacles_count + lakes_count and i >= lakes_count:
            map = map[:random_place] + obstacle + map[random_place + 1:]
        else:
            map = map[:random_place] + rover + map[random_place + 1:]
        used_space.append(random_place)

    return map

if __name__ == '__main__':
    print(crearMapa.__doc__)

    # ---------- TEST 1 ----------
    print("---------- TEST 1 ----------\n")
    print(crearMapa(2, 2, 11, 18, False))

    # ---------- TEST 2 ----------
    print("---------- TEST 2 ----------\n")
    print(crearMapa(10, 10, 22, 5, True))

    # ---------- TEST 3 ----------
    print("---------- TEST 3 ----------\n")
    print(crearMapa(0, 3000, 11012831, 181223, True))

    # ---------- TEST 4 ----------
    print("---------- TEST 4 ----------\n")
    print(crearMapa(20, 30, 15, 32, False))

    # ---------- TEST 5 ----------
    print("---------- TEST 5 ----------\n")
    print(crearMapa(15, 30, 22, 45, True))



