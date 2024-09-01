import random

class Dice:
    """
    A class representing a dice with a specified number of sides.
    
    Attributes:
    - sides (int): The number of sides the dice has.
    
    Methods:
    - throw: Simulates throwing the dice and returns a random integer between 1 and the number of sides.
    """
    
    def __init__(self, sides):
        """
        Initializes a new Dice object with the given number of sides.
        
        Parameters:
        - sides (int): The number of sides for the dice.
        
        Raises:
        - Exception: If the number of sides is greater than 100.
        """
        if sides > 100:
            raise Exception("Dice should not have more than 100 sides")
        else:
            self.sides = sides

    def __repr__(self):
        """
        Returns a string representation of the Dice object.
        
        Returns:
        - str: A string representation of the Dice object including the number of sides.
        """
        return f"Dice({self.sides} sides)"
    
    def throw(self):
        """
        Simulates throwing the dice and returns a random integer between 1 and the number of sides.
        
        Returns:
        - int: A random integer between 1 and the number of sides.
        """
        return random.randint(1, self.sides)
