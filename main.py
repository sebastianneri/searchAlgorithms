from Mapa.crearMapa import crearMapa
from simpleai.search import breadth_first, depth_first, greedy, uniform_cost, astar
from Draw.Drawings import getResults
from SituacionProblema.SituacionProblema import Rover

if __name__ == '__main__':
    while True:
        try:
            print_map = False
            mapa = crearMapa(100, 100, 200, 10, True)
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