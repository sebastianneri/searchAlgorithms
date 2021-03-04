from time import time
def drawPath(mapa, path):
    actual = 0
    dim = mapa.find("\n")
    for i in path:
        siguiente = i
        if mapa[actual] not in ["_", "Q"]:
            if siguiente - actual in [- dim - 1, dim + 1]:
                mapa = mapa[:actual] + "|" + mapa[actual + 1:]

            elif siguiente - actual in [- dim -2 , dim + 2]:
                mapa = mapa[:actual] + '\\' + mapa[actual + 1:]

            elif siguiente - actual in [- dim, dim]:
                mapa = mapa[:actual] + '/' + mapa[actual + 1:]

        actual = i
    return mapa

def getResults(mapa, problema, algoritmo, nombre, print_map):
    t0 = time()
    result = algoritmo(problema, graph_search=True)
    t1 = time()
    path = [x[1] for x in result.path()]
    if print_map:
        print(f"------------------------------------------- Mapa Final {nombre} -------------------------------------------")
        print(drawPath(mapa, path))
    print(f"Total Pasos: {len(result.path())}\nTiempo: {t1-t0} sgs\n")
    return