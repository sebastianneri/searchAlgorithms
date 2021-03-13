from Mapa.crearMapa import crearMapa
from simpleai.search import breadth_first, depth_first, greedy, uniform_cost, astar, hill_climbing
from Draw.Drawings import getResults
from SituacionProblema.TercerAvance.SituacionProblema import Rover

if __name__ == '__main__':
    print_map = True
    mapa = crearMapa(20, 30, 20, 1, True)
    problema = Rover(mapa, 5)
    output = hill_climbing(problema)
    print(mapa)
    print('\nPath to the solution:')
    print(output.path())
    for item, state in output.path():
        print("nivel", problema.nivel)
        print("state", state)
        print("item", item)
        print(mapa[:state] + "$" + mapa[state+1:])
        print(f"Valor = {problema.value(state)}")

"""    while True:
        try:
            print_map = True
            mapa = crearMapa(20, 30, 20, 1, True)
            problema = Rover(mapa)
            if print_map:
                print("------------------------------------------- Mapa Inicial -------------------------------------------")
                print(mapa)
            getResults(mapa, problema,  breadth_first, 'breadth_first', print_map)
            getResults(mapa, problema, depth_first, 'depth_first', print_map)
            getResults(mapa, problema, greedy, 'greedy', print_map)
            getResults(mapa, problema, uniform_cost, 'uniform_cost', print_map)
            getResults(mapa, problema, astar, 'astar', print_map)
            break
        except Exception as e:
            pass
"""