class QLearner:
    def __init__(self, move_request):
        self.move_request = move_request
        self.Q = {}
