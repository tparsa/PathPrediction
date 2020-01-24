import operator
import random
from copy import deepcopy

class QLearner:
    def __init__(self, move_request, criterion, initial_state, terminal, alpha, gamma, next_state):
        self._move_request = move_request
        self.criterion = criterion
        self._previous_state = None
        self._state = initial_state
        self._Q = {self._state: {}}
        self.alpha = alpha
        self.gamma = gamma
        self.next_state = next_state
        self._terminal = terminal

    def _get_max_action(self, state):
        try:
            return max(self._Q[state].items(), operator.itemgetter(1))[0]
        except KeyError:
            self._Q[state] = {}
            return random.choice(self.next_state(self._state))

    def _update(self, action, reward):
        if self._state not in self._Q:
            self._Q[self._state] = {}
        self._Q[self._previous_state][action] = (1.0 - self.alpha) * self._Q[self._previous_state][action] + self.alpha * (reward + self._gamma * self._Q[self._state].get(self._get_max_action(self._state), 0))

    def _move(self):
        self._previous_state = self._state
        action = self._get_max_action(self._state)
        observation = self.move_request(action)
        self._state = observation.get('state', self._state)
        energy = observation.get('energy', 0)
        time = observation.get('time', 0)
        self._update(action, self.criterion(energy, time))

    