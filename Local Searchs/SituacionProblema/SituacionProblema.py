from simpleai.search import SearchProblem, astar
import random
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
    def __init__(self, mapa, used_space, goal):
        self.map = mapa
        self.inicial = self.map.find('Q')
        self.n = self.map.find('\n')
        self.used_space = used_space
        self.goal = goal
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
        super(Rover, self).__init__(initial_state=self.generate_random_state())
        
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
            if self.map[next_state] == self.goal:
                return True
            else:
                return False
        else:
            return True

    # Simula el movimiento que recibe
    def result(self, state, action):
        return state + self.available_steps[action]


    def value(self, state):
        if self.goal == 5:
            return int(self.map[state])
        else: 
            return -int(self.map[state])
    
    def generate_random_state(self):
        pos = np.random.randint(len(self.map))
        while pos in self.used_space:
            pos = np.random.randint(len(self.map))
        return pos
    

