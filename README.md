# Snake Game

A browser-ready Snake game built for Python and Pygbag deployment.

## Screenshot

(Add a screenshot of the game here)

## Features

- Classic snake movement on a grid
- Easy mode with wrap-around edges
- Hard mode with wall collision
- Score tracking
- Pause and restart support
- Browser-playable via `pygbag`

## Controls

- Arrow keys: move snake
- Space: pause/resume during play
- R: restart after game over
- E: select Easy mode from the menu
- H: select Hard mode from the menu

## Installation

1. Install Python 3.10+.
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Local execution

```bash
python main.py
```

## Web deployment (Pygbag)

From the repository root:

```bash
python -m pygbag .
```

This generates a `build/web/` folder containing the browser build. Host that
folder's contents (e.g. via GitHub Pages) to play in a browser.

## Technologies used

- Python
- Pygame
- Pygbag

## Repository structure

- `main.py` — browser compatible Snake game entry point
- `requirements.txt` — required Python packages
- `.gitignore` — common exclusions
- `README.md` — project overview and instructions
- `Task.md` — deployment and cleanup task description

## Future improvements

- Add sound effects
- Add mobile touch controls
- Add high score persistence
- Add graphics and animations

## Live Demo

(Add GitHub Pages link here)

## GitHub Repository

(Add repository URL here)

## License

This project is licensed under the [MIT License](LICENSE).
