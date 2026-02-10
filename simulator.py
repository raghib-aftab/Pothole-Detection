import random

def get_acc_z():
    if random.random() < 0.2:
        return random.uniform(3.5, 5.0)
    return random.uniform(-1.0, 1.0)
