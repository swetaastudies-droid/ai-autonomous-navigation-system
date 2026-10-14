import csv
import os
import pygame

from src.config import (
    CELL_SIZE,
    FPS,
    GOAL_POSITION,
    GRID_HEIGHT,
    GRID_WIDTH,
    START_POSITION,
    WINDOW_TITLE,
)
from src.navigation import NavigationController
from src.simulator import SimulationWorld


BACKGROUND = (24, 28, 36)
GRID_COLOR = (55, 62, 74)
EMPTY_COLOR = (235, 239, 244)
OBSTACLE_COLOR = (65, 72, 85)
ROBOT_COLOR = (35, 145, 255)
GOAL_COLOR = (50, 190, 110)
PATH_COLOR = (255, 195, 65)

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 70


def cell_rect(position):
    x, y = position
    return pygame.Rect(
        x * CELL_SIZE,
        y * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE,
    )


def save_metrics(steps, reached_goal, path_length):
    os.makedirs("results", exist_ok=True)
    file_exists = os.path.exists("results/navigation_metrics.csv")

    with open(
        "results/navigation_metrics.csv",
        "a",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["steps", "reached_goal", "path_length"])

        writer.writerow([steps, reached_goal, path_length])

    print("Metrics saved to results/navigation_metrics.csv")


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    world = SimulationWorld()
    controller = NavigationController(
        GRID_WIDTH,
        GRID_HEIGHT,
        GOAL_POSITION,
    )

    paused = False
    running = True
    steps = 0
    reached_goal = False
    last_path = []
    message = "SPACE: pause | R: reset | O: add obstacle | S: save | ESC: quit"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_SPACE:
                    paused = not paused

                elif event.key == pygame.K_r:
                    world.reset()
                    steps = 0
                    reached_goal = False
                    last_path = []
                    message = "Simulation reset"

                elif event.key == pygame.K_o:
                    path = controller.plan(
                        world.robot_position,
                        world.obstacles,
                    )
                    if len(path) > 1 and world.add_obstacle(path[1]):
                        message = "Obstacle added; replanning"
                    else:
                        message = "Could not add obstacle there"

                elif event.key == pygame.K_s:
                    save_metrics(steps, reached_goal, len(last_path))

        if not paused and not reached_goal:
            last_path = controller.plan(
                world.robot_position,
                world.obstacles,
            )

            if len(last_path) > 1:
                next_position = controller.next_move(
                    world.robot_position,
                    world.obstacles,
                )

                if world.move_robot(next_position):
                    steps += 1

            if world.robot_position == GOAL_POSITION:
                reached_goal = True
                message = "Goal reached!"

            elif not last_path:
                message = "No path available — press R to reset"

        screen.fill(BACKGROUND)

        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                position = (x, y)
                rect = cell_rect(position)

                color = EMPTY_COLOR
                if position in world.obstacles:
                    color = OBSTACLE_COLOR
                elif position in last_path:
                    color = PATH_COLOR

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRID_COLOR, rect, 1)

        pygame.draw.rect(screen, GOAL_COLOR, cell_rect(GOAL_POSITION))
        pygame.draw.rect(screen, ROBOT_COLOR, cell_rect(world.robot_position))

        pygame.draw.rect(
            screen,
            BACKGROUND,
            pygame.Rect(0, GRID_HEIGHT * CELL_SIZE, WINDOW_WIDTH, 70),
        )

        status = (
            f"Steps: {steps} | "
            f"Goal: {'Reached' if reached_goal else 'Not reached'}"
        )
        screen.blit(
            font.render(status, True, (245, 245, 245)),
            (10, GRID_HEIGHT * CELL_SIZE + 8),
        )

        screen.blit(
            font.render(message, True, (245, 245, 245)),
            (10, GRID_HEIGHT * CELL_SIZE + 38),
        )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()