from src.Dice import Dice

class GameRules:
    """
    A class representing the rules and gameplay for a dice game using a DiceCollection object.
    
    Attributes:
    - dc (DiceCollection): The DiceCollection object containing the dice to be used in the game.
    
    Methods:
    - play_game: Executes the game loop, allowing the player to throw dice and continue playing.
    - __get_dice_number: Prompts the user to select a dice from the DiceCollection for throwing.
    - __get_throw_number: Prompts the user to specify the number of times to throw the selected dice.
    - last_100_throws_info: Asks the user if they want to view the last 100 throw results from the DiceCollection.
    - __selection: Helper method to handle user selection prompts.
    - make_dice: Allows the user to create and add Dice objects to the DiceCollection.
    """
    
    def __init__(self, dc):
        """
        Initializes a new GameRules object with a given DiceCollection.
        
        Parameters:
        - dc (DiceCollection): The DiceCollection object containing the dice for the game.
        """
        self.dc = dc

    def play_game(self, isPlaying):
        """
        Executes the game loop, allowing the player to throw dice and continue playing.
        
        Parameters:
        - isPlaying (bool): A flag indicating whether the player wants to continue playing the game.
        
        Returns:
        - bool: A flag indicating whether the player wants to continue playing the game.
        """
        index = self.__get_dice_number() - 1
        throw_number = self.get_throw_number()
        print(f"Dice was thrown {throw_number} times and the results are:")
        [print(self.dc.throw_dice(index)) for _ in range(throw_number)]
        self.last_100_throws_info()
        isPlaying = self.__selection("Do you want to continue [Y/N]?")
        return isPlaying

    def __get_dice_number(self):
        """
        Prompts the user to select a dice from the DiceCollection for throwing.
        
        Returns:
        - int: The index of the selected dice in the DiceCollection.
        """
        while True:
            print(f"PLEASE SELECT WHICH DICE YOU WOULD LIKE TO THROW (1-{len(self.dc)}):", end=" ")
            try:
                dice_number = int(input())
                if dice_number < 1 or dice_number > len(self.dc):
                    raise ValueError("Invalid dice number")
                break
            except ValueError:
                print("Please enter a valid dice number and try again.")
        return dice_number
    
    def get_throw_number(self):
        """
        Prompts the user to specify the number of times to throw the selected dice.
        
        Returns:
        - int: The number of times to throw the selected dice.
        """
        while True:
            print("HOW MANY TIMES YOU WANT TO THROW THE DICE:", end=" ")
            try:
                throw_count = int(input())
                if throw_count < 1:
                    raise ValueError("Invalid dice throw number")
                break
            except ValueError:
                print("Please enter a valid throw number and try again.")
        return throw_count

    def last_100_throws_info(self):
        """
        Asks the user if they want to view the last 100 throw results from the DiceCollection.
        """
        isSelected = self.__selection("Do you want to see the last 100 throws [Y/N]?")
        if isSelected:
            print("Last 100 throws:")
            throws_history = self.dc.last_100_throws()
            [print(throw, end=" ") for throw in throws_history]
            print()

    def __selection(self, string):
        """
        Helper method to handle user selection prompts.
        
        Parameters:
        - string (str): The prompt string to display to the user.
        
        Returns:
        - bool: A flag indicating the user's selection (True for 'Y', False for 'N').
        """
        isSelected = False
        while True:
            try:
                print(string, end=" ")
                selection = input()
                if selection.upper() == "Y":
                    isSelected = True
                elif selection.upper() == "N":
                    isSelected = False
                else:
                    raise ValueError("Invalid argument")
                break
            except ValueError:
                print("Please enter a valid argument and try again.")            
        return isSelected
    
    def make_dice(self):
        """
        Allows the user to create and add Dice objects to the DiceCollection.
        """
        print("Select how many dice you want to play with:", end=" ")
        dice_count = int(input())
        print("Select how many sides every dice should have:")
        for i in range(dice_count):
            print(f"Dice {i+1}: ", end=" ")
            dice_side = int(input())
            d = Dice(dice_side)
            self.dc.append_dice(d)
