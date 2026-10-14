import random

from src.config import GRID_WIDTH, GRID_HEIGHT, START_POSITION, GOAL_POSITION


class SimulationWorld:
    """Grid world containing the robot, goal, and obstacles."""

    def __init__(self, obstacle_count=55, seed=42):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.start = START_POSITION
        self.goal = GOAL_POSITION
        self.robot_position = self.start
        self.obstacles = set()

        self._generate_obstacles(obstacle_count, seed)

    def _generate_obstacles(self, obstacle_count, seed):
        """Generate reproducible random obstacles."""
        rng = random.Random(seed)

        excluded = {self.start, self.goal}
        available = [
            (x, y)
            for x in range(self.width)
            for y in range(self.height)
            if (x, y) not in excluded
        ]

        obstacle_count = min(obstacle_count, len(available))
        self.obstacles = set(rng.sample(available, obstacle_count))

    def reset(self):
        """Return the robot to its starting position."""
        self.robot_position = self.start

    def move_robot(self, next_position):
        """Move one cell if the destination is valid and unblocked."""
        x, y = next_position

        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        if next_position in self.obstacles:
            return False

        self.robot_position = next_position
        return True

    def add_obstacle(self, position):
        """Add an obstacle unless it occupies the robot or goal."""
        if position in {self.robot_position, self.goal}:
            return False

        x, y = position
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False

        self.obstacles.add(position)
        return True