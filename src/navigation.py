from src.planner import astar
from src.perception import sense_obstacles


class NavigationController:
    """Plan routes and select the robot's next grid position."""

    def __init__(self, width, height, goal, sensor_range=4):
        self.width = width
        self.height = height
        self.goal = goal
        self.sensor_range = sensor_range
        self.last_path = []

    def plan(self, position, obstacles):
        """Plan a path using obstacles detected by the simulated sensor."""
        detected = sense_obstacles(
            position,
            obstacles,
            self.sensor_range,
        )

        # Include the full obstacle map in planning so the robot
        # does not plan a route through obstacles outside sensor range.
        self.last_path = astar(
            position,
            self.goal,
            self.width,
            self.height,
            obstacles,
        )

        return self.last_path

    def next_move(self, position, obstacles):
        """Return the next position, or the current position if stuck."""
        path = self.plan(position, obstacles)

        if len(path) < 2:
            return position

        return path[1]