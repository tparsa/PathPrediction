# main
from MapBuilder import MapBuilder
from qlearner import QLearner
from universe import Universe
from Criterions import get_cost_based_on_fuel, get_cost_based_on_time, get_cost_based_on_mixture 

if __name__ == "__main__":

    universe = Universe(MapBuilder())
    qlearners = [QLearner(universe.get_initial_state(), get_cost_based_on_fuel, universe.move_request, universe.get_terminal_state(), 1, 0.9, universe.next_state)
                , QLearner(universe.get_initial_state(), get_cost_based_on_time, universe.move_request, universe.get_terminal_state(), 1, 0.9,  universe.next_state)
                , QLearner(universe.get_initial_state(), get_cost_based_on_mixture, universe.move_request, universe.get_terminal_state(), 1, 0.9, universe.next_state)]


    num_of_epochs = 1000

    for epoch_num in range(num_of_epochs):
        for qlearner in qlearners:
            while qlearner._state != universe.get_terminal_state():
                qlearner.move()
            qlearner.reset(universe.get_initial_state())

    print("Energy:", qlearners[0]._Q, end='\n\n')
    print("Time:", qlearners[1]._Q, end='\n\n')
    print("E + T^2:", qlearners[2]._Q, end='\n\n')
