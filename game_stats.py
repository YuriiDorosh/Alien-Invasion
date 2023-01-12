class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in an inactive state
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
