from array import array

class DiceCollection:
    """
    A class representing a collection of dice with a maximum of 5 dice items.
    
    Attributes:
    - dice_items (list): A list containing Dice objects.
    - throws (array): An array storing the results of the dice throws.
    
    Methods:
    - append_dice: Adds a Dice object to the collection.
    - throw_dice: Simulates throwing a dice from the collection and updates the throws array.
    - last_100_throws: Returns the last 100 throw results stored in the throws array.
    """
    
    def __init__(self, dice_items=None):
        """
        Initializes a new DiceCollection object with an optional list of Dice items.
        
        Parameters:
        - dice_items (list, optional): A list of Dice objects to initialize the collection.
        
        Raises:
        - Exception: If the number of dice items provided is more than 5.
        """
        self.throws = array('i')
        if dice_items is None:
            self.dice_items = []
        else:
            if len(dice_items) <= 5:
                self.dice_items = dice_items
            else:
                raise Exception("DiceCollection should not have more than 5 dices")
    
    def append_dice(self, dice):
        """
        Adds a Dice object to the collection if the collection has less than 5 dice items.
        
        Parameters:
        - dice (Dice): The Dice object to add to the collection.
        
        Raises:
        - Exception: If the collection already has 5 dice items.
        """
        if len(self.dice_items) + 1 <= 5:
            self.dice_items.append(dice)
        else:
            raise Exception("DiceCollection should not have more than 5 dices")
    
    def throw_dice(self, index):
        """
        Simulates throwing a dice from the collection at a specified index and updates the throws array.
        
        Parameters:
        - index (int): The index of the Dice object in the collection to throw.
        
        Returns:
        - int: The result of the dice throw.
        
        Raises:
        - Exception: If the collection is empty or the index is out of range.
        """
        if len(self.dice_items) > 0:
            throw_result = self.dice_items[index].throw()
            self.__update_last_throw(throw_result)
            return throw_result
        else:
            raise Exception("DiceCollection should not have less than 0 dices")
    
    def last_100_throws(self):
        """
        Returns the last 100 throw results stored in the throws array.
        
        Returns:
        - array: An array containing the last 100 throw results.
        """
        return self.throws[-100:]
    
    def __getitem__(self, index):
        """
        Returns the Dice object at the specified index in the collection.
        
        Parameters:
        - index (int): The index of the Dice object to retrieve.
        
        Returns:
        - Dice: The Dice object at the specified index.
        """
        return self.dice_items[index] 
       
    def __len__(self):
        """
        Returns the number of dice items in the collection.
        
        Returns:
        - int: The number of dice items in the collection.
        """
        return len(self.dice_items)
    
    def __update_last_throw(self, throw_result):
        """
        Updates the throws array with the latest dice throw result.
        
        Parameters:
        - throw_result (int): The result of the latest dice throw to append to the throws array.
        """
        self.throws.append(throw_result)
