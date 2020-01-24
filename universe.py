class Universe:
    def __init__(self, map_builder):
        self._map_builder = map_builder

    def next_state(self, state):
        return self._map_builder.next_state(state)
    
    def move_request(self, state, action):
        if action not in self._map_builder.next_state(state):
            raise Exception("Wrong action pal")

        next_state = action
        energy, time = self._map_builder.get_Reward(state, action)
        return {'state': next_state, 'energy': energy, 'time': time}

    def get_initial_state(self):
        return self._map_builder.initial_state()
    
    def get_terminal_state(self):
        return self._map_builder.terminal_state()
