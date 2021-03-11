from Mapa.crearMapa import crearMapa
from SituacionProblema.SituacionProblema import Rover
from simpleai.search import hill_climbing_random_restarts, hill_climbing, simulated_annealing
from simpleai.search.local import _exp_schedule
from scipy.stats import boltzmann

temp = 100
def temperature(time):
    delta = temp - time
    print("Temperatura: ",time,delta)
    lambda_, n = 1.4, time
    
    return boltzmann.pmf(delta, lambda_, n)

if __name__ == '__main__':
    while True:
        try:
            mapa,used_space = crearMapa(20, 30, 20, 1, True)
            problema = Rover(mapa,used_space, 0)
            
            #output = hill_climbing(problema)
            # output = hill_climbing_random_restarts(problema,500)
            output = simulated_annealing(problema, temperature)
            # output = simulated_annealing(problema,_exp_schedule)
            print('\nPath to the solution:')
            for item,state in output.path():
                print(mapa[:state]+'?'+mapa[state+1:])
                print(f"Valor = {problema.value(state)}")
                
            problema = Rover(mapa,used_space, 5)
            
            #output = hill_climbing(problema)
            #output = hill_climbing_random_restarts(problema,500)
            output = simulated_annealing(problema, temperature)
            # output = simulated_annealing(problema,_exp_schedule)
            print('\nPath to the solution:')
            for item,state in output.path():
                print(mapa[:state]+'?'+mapa[state+1:])
                print(f"Valor = {problema.value(state)}")
            break
        except:
            pass