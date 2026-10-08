"""
GameEngine: owns all balloons, spawns new ones, and handles clicks.

The engine keeps gameplay state together: balloons, score, lives,
round timer, spawning, popping, misses, and restarting.
"""

import random

from game.balloon import Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT

SPAWN_INTERVAL_FRAMES = 45
POINTS_PER_POP = 10
BONUS_POINTS = 25
PENALTY_POINTS = -10
STARTING_LIVES = 3
ROUND_DURATION = 30.0


class GameEngine:
    def __init__(self):
        self.reset_round()

    def reset_round(self):
        """Start a completely fresh round."""
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0
        self.lives = STARTING_LIVES
        self.time_remaining = ROUND_DURATION
        self.game_over = False

    def _spawn_balloon(self):
        radius = random.randint(16, 44)
        x = random.randint(radius + 10, WIDTH - radius - 10)
        speed = random.uniform(1.5, 3.0)

        # Normal: +10, Bonus: +25, Penalty: -10.
        roll = random.random()
        if roll < 0.15:
            balloon_type = "bonus"
            color = (60, 210, 90)
            points = BONUS_POINTS
        elif roll < 0.30:
            balloon_type = "penalty"
            color = (80, 100, 230)
            points = PENALTY_POINTS
        else:
            balloon_type = "normal"
            color = (220, 90, 120)
            points = POINTS_PER_POP

        self.balloons.append(
            Balloon(
                x=x,
                y=-radius,
                radius=radius,
                speed=speed,
                color=color,
                balloon_type=balloon_type,
                points=points,
            )
        )

    def handle_click(self, pos):
        """Pop a balloon and apply its effect, if the round is active."""
        if self.game_over:
            return

        popped = check_pop(self.balloons, pos)
        if popped is not None:
            self.balloons.remove(popped)
            self.score += popped.points

    def _end_round(self):
        self.game_over = True
        # Nothing remains active on the board after the round ends.
        self.balloons.clear()

    def update(self, dt=1 / 60):
        """Advance the active round by dt seconds."""
        if self.game_over:
            return

        self.time_remaining = max(0.0, self.time_remaining - dt)
        if self.time_remaining <= 0:
            self._end_round()
            return

        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        remaining_balloons = []
        for balloon in self.balloons:
            balloon.update()
            if balloon.is_past_bottom(HEIGHT):
                self.lives -= 1
            else:
                remaining_balloons.append(balloon)

        self.balloons = remaining_balloons

        # A missed balloon is removed here, so it can decrement lives
        # only once. Popped balloons never enter this path.
        if self.lives <= 0:
            self.lives = 0
            self._end_round()

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(surface, self.balloons)
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
        renderer.draw_text(surface, font, f"Lives: {self.lives}", (10, 40))
        renderer.draw_text(surface, font, f"Time: {self.time_remaining:04.1f}", (10, 70))

        if self.game_over:
            renderer.draw_game_over(surface, font, self.score)
