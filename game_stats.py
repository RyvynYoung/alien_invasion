class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in inactive state
        self.game_active = False
        # High Score should not be reset
        with open('side_projects/alien_invasion/all_time_high_score.txt') as file_obj:
            alltime_score = file_obj.read()
        self.high_score = int(alltime_score)

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 0

    