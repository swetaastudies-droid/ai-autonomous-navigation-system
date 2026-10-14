from src.planner import astar


def test_finds_path():
    path = astar((0, 0), (4, 4), 5, 5)

    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)
    assert len(path) == 9


def test_avoids_obstacles():
    obstacles = {(1, 0), (1, 1)}

    path = astar((0, 0), (2, 0), 3, 3, obstacles)

    assert path
    assert path[0] == (0, 0)
    assert path[-1] == (2, 0)
    assert not any(cell in obstacles for cell in path)


def test_no_path_exists():
    obstacles = {
        (1, 0),
        (1, 1),
        (1, 2),
    }

    path = astar((0, 1), (2, 1), 3, 3, obstacles)

    assert path == []


def test_start_equals_goal():
    path = astar((1, 1), (1, 1), 3, 3)

    assert path == [(1, 1)]