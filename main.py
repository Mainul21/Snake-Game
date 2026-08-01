import asyncio
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_r, K_e, K_h

GRID_SIZE = 10
GRID_WIDTH = 50
GRID_HEIGHT = 50
WINDOW_WIDTH = GRID_WIDTH * GRID_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * GRID_SIZE
INITIAL_INTERVAL = 150
MIN_INTERVAL = 40
SPEED_STEP = 8

COLOR_BACKGROUND = (0, 0, 0)
COLOR_SNAKE = (0, 200, 0)
COLOR_FOOD = (200, 0, 0)
COLOR_TEXT = (240, 240, 240)
COLOR_PAUSE = (255, 255, 0)

DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)

MODE_EASY = 0
MODE_HARD = 1

MOVE_EVENT = pygame.USEREVENT + 1


def clamp_speed(value):
    return max(MIN_INTERVAL, value)


def draw_text(surface, text, position, font, color=COLOR_TEXT):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)


def draw_block(surface, position, color):
    rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(surface, color, rect)


def generate_food(snake):
    while True:
        position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if position not in snake:
            return position


def move_head(head, direction, mode):
    x, y = head
    dx, dy = direction
    if mode == MODE_EASY:
        return ((x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT)
    return (x + dx, y + dy)


def check_collision(snake, mode):
    head = snake[0]
    if mode == MODE_HARD:
        if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
            return True
    if head in snake[1:]:
        return True
    return False


def reset_game(mode):
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = DIR_DOWN
    food = generate_food(snake)
    score = 0
    interval = INITIAL_INTERVAL
    return snake, direction, food, score, interval


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    font = pygame.font.Font(None, 28)
    title_font = pygame.font.Font(None, 40)

    mode = MODE_EASY
    state = "menu"
    paused = False
    snake, direction, food, score, interval = reset_game(mode)
    pygame.time.set_timer(MOVE_EVENT, interval)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if state == "menu":
                    if event.key == K_e:
                        mode = MODE_EASY
                        snake, direction, food, score, interval = reset_game(mode)
                        state = "playing"
                        paused = False
                        pygame.time.set_timer(MOVE_EVENT, interval)
                    elif event.key == K_h:
                        mode = MODE_HARD
                        snake, direction, food, score, interval = reset_game(mode)
                        state = "playing"
                        paused = False
                        pygame.time.set_timer(MOVE_EVENT, interval)
                    elif event.key == K_SPACE:
                        mode = MODE_EASY
                        snake, direction, food, score, interval = reset_game(mode)
                        state = "playing"
                        paused = False
                        pygame.time.set_timer(MOVE_EVENT, interval)
                elif state == "playing":
                    if event.key == K_SPACE:
                        paused = not paused
                    elif event.key == K_UP and direction != DIR_DOWN:
                        direction = DIR_UP
                    elif event.key == K_DOWN and direction != DIR_UP:
                        direction = DIR_DOWN
                    elif event.key == K_LEFT and direction != DIR_RIGHT:
                        direction = DIR_LEFT
                    elif event.key == K_RIGHT and direction != DIR_LEFT:
                        direction = DIR_RIGHT
                elif state == "game_over":
                    if event.key == K_r:
                        snake, direction, food, score, interval = reset_game(mode)
                        state = "playing"
                        paused = False
                        pygame.time.set_timer(MOVE_EVENT, interval)

            elif event.type == MOVE_EVENT and state == "playing" and not paused:
                new_head = move_head(snake[0], direction, mode)
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    interval = clamp_speed(interval - SPEED_STEP)
                    pygame.time.set_timer(MOVE_EVENT, interval)
                    food = generate_food(snake)
                else:
                    snake.pop()

                if check_collision(snake, mode):
                    state = "game_over"
                    pygame.time.set_timer(MOVE_EVENT, 0)

        screen.fill(COLOR_BACKGROUND)

        if state == "menu":
            draw_text(screen, "Snake Game", (22, 20), title_font)
            draw_text(screen, "Press E for Easy mode (wrap around)", (22, 90), font)
            draw_text(screen, "Press H for Hard mode (wall collision)", (22, 130), font)
            draw_text(screen, "Use Arrow keys to move", (22, 170), font)
            draw_text(screen, "Press Space to start in Easy mode", (22, 210), font)
            draw_text(screen, "Press Q or close window to quit", (22, 250), font)
        elif state == "playing":
            for block in snake:
                draw_block(screen, block, COLOR_SNAKE)
            draw_block(screen, food, COLOR_FOOD)
            draw_text(screen, f"Score: {score}", (10, 10), font)
            mode_text = "EASY" if mode == MODE_EASY else "HARD"
            draw_text(screen, f"Mode: {mode_text}", (10, 36), font)
            if paused:
                draw_text(screen, "PAUSED", (WINDOW_WIDTH - 120, 10), font, COLOR_PAUSE)
        else:
            draw_text(screen, "Game Over", (WINDOW_WIDTH // 2 - 90, WINDOW_HEIGHT // 2 - 30), title_font)
            draw_text(screen, f"Score: {score}", (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 20), font)
            draw_text(screen, "Press R to restart", (WINDOW_WIDTH // 2 - 95, WINDOW_HEIGHT // 2 + 60), font)
            draw_text(screen, "Press Q or close window to quit", (WINDOW_WIDTH // 2 - 145, WINDOW_HEIGHT // 2 + 100), font)

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
