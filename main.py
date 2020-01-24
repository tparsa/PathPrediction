# main
from Mapbuilder-2 import Mapbuilder
from qlearner import QLearner
from universe import Universe
from Criterions import get_cost_based_on_fuel, get_cost_based_on_time, get_cost_based_on_mixture 

if __name__ == "__main__":

    universe = Universe(Mapbuilder())
    qlearner_1 = QLearner(universe.get_initial_state(), get_cost_based_on_fuel, universe.move_request(), universe.get_terminal_state(), universe.next_state())
    qlearner_2 = QLearner(universe.get_initial_state(), get_cost_based_on_time, universe.move_request(), universe.get_terminal_state(), universe.next_state())
    qlearner_3 = QLearner(universe.get_initial_state(), get_cost_based_on_mixture, universe.move_request(), universe.get_terminal_state(), universe.next_state())

    