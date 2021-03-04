from Mapa.crearMapa import crearMapa
from simpleai.search import breadth_first, depth_first, greedy, uniform_cost, astar
from Draw.Drawings import getResults
from SituacionProblema.SituacionProblema import Rover

if __name__ == '__main__':
    while True:
        try:
            mapa = crearMapa(20, 30, 25, 2, True)
            problema = Rover(mapa)
            print("------------------------------------------- Mapa Inicial -------------------------------------------")
            print(mapa)
            getResults(mapa, problema,  breadth_first, 'breadth_first')
            getResults(mapa, problema, depth_first, 'depth_first')
            getResults(mapa, problema, greedy, 'greedy')
            getResults(mapa, problema, uniform_cost, 'uniform_cost')
            getResults(mapa, problema, astar, 'astar')
            break
        except Exception as e:
            pass