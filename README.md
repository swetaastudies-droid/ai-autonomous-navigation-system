# AI-Based Autonomous Navigation System

A Python-based 2D robotics simulation demonstrating autonomous path planning, obstacle-aware navigation, and interactive visualization using the A* search algorithm.

## Features

- A* path planning with a Manhattan-distance heuristic
- Grid-based environment with obstacles and a destination
- Simulated obstacle perception
- Interactive Pygame simulation
- CSV-based navigation metrics
- Automated path-planning tests using pytest

## Technology Stack

- Python 3.13
- Pygame
- NumPy
- Matplotlib
- pytest

## Project Structure

```text
AI_Based_Autonomous_Navigation_System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
├── tests/
└── results/
    └── navigation_metrics.csv
```

## Installation

Create and activate a virtual environment, then install the dependencies.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the Simulation

```powershell
python app.py
```

## Run Tests

```powershell
python -m pytest -v
```

## Results

The path-planning test suite has passed four tests in the current development environment. Navigation runs can also be recorded in `results/navigation_metrics.csv`.

## Limitations

This is a software simulation. Obstacle perception uses the simulated environment's obstacle map; the project does not currently implement physical robot control, camera-based object detection, or SLAM.

## Screenshots

Screenshots of the running simulation and successful navigation will be added here.

## Future Improvements

- Compare A* with other path-planning algorithms
- Expand automated test coverage
- Add navigation performance charts
- Explore dynamic obstacles and robotics frameworks

## Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/YOUR-USERNAME)