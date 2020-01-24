# main
from MapBuilder import MapBuilder
from qlearner import QLearner
from universe import Universe
from Criterions import get_cost_based_on_fuel, get_cost_based_on_time, get_cost_based_on_mixture 

if __name__ == "__main__":

    universe = Universe(MapBuilder())
    qlearner_1 = QLearner(universe.get_initial_state(), get_cost_based_on_fuel, universe.move_request, universe.get_terminal_state(), 1, 0.9, universe.next_state)
    qlearner_2 = QLearner(universe.get_initial_state(), get_cost_based_on_time, universe.move_request, universe.get_terminal_state(), 1, 0.9,  universe.next_state)
    qlearner_3 = QLearner(universe.get_initial_state(), get_cost_based_on_mixture, universe.move_request, universe.get_terminal_state(), 1, 0.9, universe.next_state)


    num_of_epochs = 100

    for epoch_num in range(num_of_epochs):
        while qlearner_1._state != universe.get_terminal_state():
            qlearner_1.move()
        if epoch_num % 10 == 0:
            print("Epoch num: {}".format(epoch_num))
        qlearner_1.reset(universe.get_initial_state())

    print(qlearner_1._Q)
