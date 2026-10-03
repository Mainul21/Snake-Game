# Snake Game

A browser-ready Snake game built for Python and Pygbag deployment.

**[Play it live](https://mainul21.github.io/Snake-Game/)** — click the page once if prompted, then press E, H or Space.

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
2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Local execution

```bash
source .venv/bin/activate
python main.py
```

## Web deployment (Pygbag)

From the repository root:

```bash
source .venv/bin/activate
python -m pygbag --build --disable-sound-format-error .
```

This generates a `build/web/` folder containing the browser build. Host that
folder's contents (e.g. via GitHub Pages) to play in a browser.

Pushing to `main` deploys automatically: the GitHub Actions workflow builds with
Pygbag and publishes to the `gh-pages` branch (Settings → Pages → `gh-pages`).

Browser notes: the main loop must be `async` and call `await asyncio.sleep(0)`
each frame, and `pygame.time.set_timer` is not available on WASM, so timing uses
`pygame.time.get_ticks()`.

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

https://mainul21.github.io/Snake-Game/

## GitHub Repository

https://github.com/Mainul21/Snake-Game

## License

This project is licensed under the [MIT License](LICENSE).
