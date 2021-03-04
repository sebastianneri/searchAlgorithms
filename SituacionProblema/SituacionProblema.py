from simpleai.search import SearchProblem, astar
import re
import numpy as np

costos = {
    "adelante": 1.0,
    "adelante derecha": 1.4,
    "adelante izquierda": 1.4,
    "atras": 1.0,
    "atras derecha": 1.4,
    "atras izquierda": 1.4
}

class Rover(SearchProblem):
    # El constructor inicializa el problema del rover
    def __init__(self, mapa):
        self.map = mapa
        self.inicial = self.map.find('Q')
        self.n = self.map.find('\n')
        self.rover_coors = self.getCoors(self.inicial)
        self.closest = self.findLakes()
        self.goal = '_'
        self.available_steps = {
            "adelante": self.n+1,
            "adelante derecha": self.n+2,
            "adelante izquierda": self.n,
            "atras": -self.n-1,
            "atras derecha": -self.n,
            "atras izquierda": -self.n-2
        }
        jail = True
        for i in list(self.available_steps.values()):
            try:
                if jail:
                    self.nivel = int(mapa[self.inicial + i])
                    self.map = self.map[:self.inicial] + str(self.nivel) + self.map[self.inicial + 1:]
                    jail = False
            except Exception:
                if mapa[self.inicial + i] == self.goal:
                    self.nivel = 0
                else:
                    continue
        if jail:
            return None
        super(Rover, self).__init__(initial_state=self.inicial)

        
    # Recibe un estado inicial, regresa los movimientos posibles
    def actions(self, state): 
        acciones = []
        for accion in list(costos.keys()):
            next_state = self.result(state, accion)
            if self._is_valid(state, next_state):
                acciones.append(accion)
        return acciones

    # Confirma si la acción que se quiere realizar es posible hacerse.
    def _is_valid(self, state, next_state):
        if self.map[next_state] in ["*", "#", "Q", "_"] or (int(self.map[next_state]) - int(self.map[state])) not in [1, -1]:
            if self.map[next_state] == "_":
                return True
            else:
                return False
        else:
            return True

    # Simula el movimiento que recibe
    def result(self, state, action):
        return state + self.available_steps[action]

    # Confirma si ya se alcanzó la meta
    def is_goal(self, state):
        return self.map[state] == self.goal

    def cost(self, state, action, next_state):
        if self.map[state] >= self.map[next_state] or self.map[next_state] == "_":
            return costos[action]
        else:
            return int(self.map[next_state]) + costos[action] - 1

    def findLakes(self):
        lakes = re.finditer("_", self.map)
        points = [lake.start() for lake in lakes]
        coors = [[self.getCoors(point), point] for point in points]
        distances = [[self.getDistanceFromRover(point[0]), point[1]] for point in coors]
        return np.array(self.getCoors(min(distances)[1]))

    def getCoors(self, index):
        x = round(index / self.n)
        y = index - x
        return (x, y)

    def getDistanceFromRover(self, point):
        return ((self.rover_coors[0] - point[0])**2 + (self.rover_coors[1] - point[1])**2)**0.5

    def getDistanceFromLake(self, point):
        return ((self.closest[0] - point[0])**2 + (self.closest[1] - point[1])**2)**0.5


    # ------ Manhattan Distance ------
    def heuristic(self, state):
        state = self.getCoors(state)
        return np.abs(self.closest[0] - np.array(state)[0]) + np.abs(self.closest[1] - np.array(state)[1])

"""   
# ------ Euclidean Distance ------
    def heuristic(self, state):
        state = self.getCoors(state)
        return self.getDistanceFromLake(state)


"""