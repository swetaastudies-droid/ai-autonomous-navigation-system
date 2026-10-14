from src.config import SENSOR_RANGE


def sense_obstacles(position, obstacles, sensor_range=SENSOR_RANGE):
    """Return obstacles within Manhattan distance of the robot.

    This is a simulated sensor using the known obstacle map,
    not a real camera or physical sensor.
    """
    x, y = position
    visible_obstacles = set()

    for obstacle in obstacles:
        ox, oy = obstacle
        distance = abs(ox - x) + abs(oy - y)

        if distance <= sensor_range:
            visible_obstacles.add(obstacle)

    return visible_obstacles