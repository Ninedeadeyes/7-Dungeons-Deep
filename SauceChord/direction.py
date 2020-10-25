from enum import Enum
import random

class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3

    @staticmethod
    def random():
        return random.choice([Direction.up, Direction.down, Direction.left, Direction.right])
