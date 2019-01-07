import numpy as np

def MoveVector(APositions, BPositions, masses, G=1.0):
    dim = APositions.shape[1]
    diff = BPositions - APositions
    magnitude = np.power(diff, 2).sum()
    