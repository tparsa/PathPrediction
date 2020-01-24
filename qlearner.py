import operator
import random
from copy import deepcopy

class QLearner:
    def __init__(self, initial_state, criterion, move_request, terminal, alpha, gamma, next_state, decay=0.001):
        self._move_request = move_request
        self.criterion = criterion
        self._previous_state = None
        self._state = initial_state
        self._Q = {self._state: {}}
        self.alpha = alpha
        self.gamma = gamma
        self.next_state = next_state
        self._terminal = terminal
        self.decay = decay
        self.epsilon = 0.5

    def _get_max_action(self, state):
        try:
            return max(self._Q[state].items(), key=operator.itemgetter(1))[0]
        except Exception:
            self._Q[state] = {}
            next_states = self.next_state(self._state)
            if len(next_states) != 0:
                return random.choice(next_states)
            else:
                return self._terminal

    def _update(self, action, reward):
        if self._state not in self._Q:
            self._Q[self._state] = {}
        self._Q[self._previous_state][action] = (1.0 - self.alpha) * self._Q[self._previous_state].get(action, 0) + self.alpha * (reward + self.gamma * self._Q[self._state].get(self._get_max_action(self._state), 0))

    def move(self):
        self._previous_state = self._state
        if random.uniform(0, 1) > self.epsilon:
            action = self._get_max_action(self._state)
        else:
            next_states = self.next_state(self._state)
            if len(next_states) != 0:
                action = random.choice(next_states)
            else:
                action = self._terminal
        observation = self._move_request(self._state, action)
        self._state = observation.get('state', self._state)
        energy = observation.get('energy', 0)
        time = observation.get('time', 0)
        self._update(action, self.criterion(energy, time))
        self.alpha = max(0, self.alpha - self.decay)

    def reset(self, initial_state):
        self._state = initial_state
        self._previous_state = None        
