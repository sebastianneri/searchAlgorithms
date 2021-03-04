from Mapa.crearMapa import crearMapa
from SituacionProblema.SituacionProblema import Rover
from simpleai.search import breadth_first, depth_first, greedy, uniform_cost, astar

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

if __name__ == '__main__':
    while True:
        try:
            mapa = crearMapa(100, 100, 100, 50, True)
            problema = Rover(mapa)
            ' ' ' recibe actions, result y is_goal (depth first search)' ' '
            #result = depth_first(problema, graph_search=True)
            ' ' ' recibe actions, result y is_goal (breadth first search)' ' '
            #result = breadth_first(problema, graph_search=True)
            ' ' ' recibe actions, result, is_goal, cost y heuristic (A*)' ' '
            result = astar(problema, graph_search=True)
            ' ' ' recibe actions, result, is_goal, cost y heuristic (greedy)' ' '
            #result = greedy(problema, graph_search=True)
            ' ' ' recibe actions, result, is_goal y cost (uniform cost)' ' '
            #result = uniform_cost(problema, graph_search=True)
            path = [x[1] for x in result.path()]
            print(drawPath(mapa, path))
            print(f"Total Pasos: {len(result.path())}")
            break
        except Exception as e:
            pass