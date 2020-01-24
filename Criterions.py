

def get_cost_based_on_fuel(fuel):
    return -fuel

def get_cost_based_on_time(time):
    return -time

def get_cost_based_on_mixture(fuel, time):
    return fuel + time**2
    