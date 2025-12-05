import pygame
import time

# Read the input
f = open("input.txt", "r")
arr = []
for l in f:
    arr.append([x for x in l.strip()])
f.close()

# Initialize pygame
pygame.init()

# Constants
CELL_SIZE = 5
PADDING = 10
FPS = 30  # Frames per second for animation

# Grid dimensions
GRID_HEIGHT = len(arr)
GRID_WIDTH = len(arr[0])

# Window dimensions
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE + 2 * PADDING
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE + 2 * PADDING + 50  # Extra space for text

# Colors
DARK_GREY = (50, 50, 50)
LIGHT_GREY = (150, 150, 150)
DARK_RED = (139, 0, 0)
WHITE = (255, 255, 255)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Visualization - Removing Sparse @ Characters")
clock = pygame.time.Clock()

# Directions for checking neighbors
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def can_remove(grid, i, j):
    count = 0
    for d in directions:
        ni, nj = i + d[0], j + d[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == '@':
                count += 1
    return count < 4

def draw_grid(grid, to_remove_set, total_removed, round_num):
    screen.fill(DARK_GREY)

    # Draw cells
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            x = PADDING + j * CELL_SIZE
            y = PADDING + i * CELL_SIZE

            if grid[i][j] == '@':
                if (i, j) in to_remove_set:
                    color = DARK_RED
                else:
                    color = LIGHT_GREY
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    # Draw text info
    font = pygame.font.Font(None, 36)
    text = font.render(f"Round: {round_num} | Total Removed: {total_removed}", True, WHITE)
    screen.blit(text, (PADDING, WINDOW_HEIGHT - 45))

    pygame.display.flip()

def main():
    running = True
    total_removed = 0
    removed_this_round = True
    round_num = 0

    # Initial draw
    draw_grid(arr, set(), total_removed, round_num)
    clock.tick(FPS)

    # Main algorithm loop with visualization
    while removed_this_round and running:
        # Handle pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        removed_this_round = False
        round_num += 1

        # Find cells to remove
        to_remove = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == '@' and can_remove(arr, i, j):
                    to_remove.append((i, j))

        if to_remove:
            # Show cells about to be removed in red
            draw_grid(arr, set(to_remove), total_removed, round_num)
            clock.tick(FPS)

            # Wait a bit to show the red cells
            time.sleep(0.15)

            # Remove the cells
            for i, j in to_remove:
                arr[i][j] = '.'
                total_removed += 1
                removed_this_round = True

            # Show updated grid
            draw_grid(arr, set(), total_removed, round_num)
            clock.tick(FPS)

    # Show final result
    print(f"Total removed: {total_removed}")

    # Keep window open until closed
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
