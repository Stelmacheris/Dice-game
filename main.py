from src.DiceCollection import DiceCollection
from src.GameRules import GameRules

if __name__ == "__main__":
    dc = DiceCollection()
    game_rules = GameRules(dc)
    game_rules.make_dice()
    print("LETS PLAY THE GAME!")
    isPlaying = True
    while isPlaying:
        isPlaying = game_rules.play_game(isPlaying)
    