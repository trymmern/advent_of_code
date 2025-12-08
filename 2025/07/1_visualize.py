import pygame
import sys
import random

# Parse input
f = open("input.txt", "r")

def parse_input(file):
    lines = []
    for line in file:
        lines.append([x for x in line.strip()])
    return lines

def update_grid(row, index):
    new_grid = [row.copy() for row in grid]
    splits = 0
    for c in range(len(row)):
        cell = grid[index][c]
        if cell == "S":
            new_grid[index + 1][c] = "|"
        if cell == "^":
            if grid[index - 1][c] == "|":
                splits += 1
                new_grid[index][c - 1] = "|"
                new_grid[index][c + 1] = "|"
        if cell == ".":
            if grid[index - 1][c] == "|":
                new_grid[index][c] = "|"
    return new_grid, splits

# Initialize pygame
pygame.init()

# Colors
GREEN = (34, 139, 34)      # Christmas tree green for "|"
YELLOW = (255, 215, 0)     # Star yellow for "S"
DARK_GREY = (40, 40, 45)   # Soft dark grey background
WHITE = (240, 240, 240)    # For text

# Decoration colors for "^" - red, white, and light green
DECORATION_COLORS = [
    (220, 20, 60),    # Red
    (255, 255, 255),  # White
    (144, 238, 144),  # Light green
]

# Grid setup
grid = parse_input(f)
f.close()

# Calculate cell size based on grid dimensions
GRID_HEIGHT = len(grid)
GRID_WIDTH = len(grid[0]) if grid else 0
CELL_SIZE = 5  # Smaller cells to fit the large grid
SCREEN_WIDTH = GRID_WIDTH * CELL_SIZE + 40
SCREEN_HEIGHT = GRID_HEIGHT * CELL_SIZE + 100

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Christmas Tree Visualization")

# Font for info
font = pygame.font.Font(None, 24)

# Animation variables
index = 0
splits = 0
clock = pygame.time.Clock()
FPS = 20  # Frames per second for animation speed
paused = False
finished = False

# Create color map for decorations (^) - each position gets a random color
random.seed(42)  # Use seed for consistent colors across frames
decoration_colors_map = {}

def draw_grid(surface, grid_data, offset_y=50):
    """Draw the grid on the surface"""
    for row_idx, row in enumerate(grid_data):
        for col_idx, cell in enumerate(row):
            x = col_idx * CELL_SIZE + 20
            y = row_idx * CELL_SIZE + offset_y

            if cell == "|":
                color = GREEN
            elif cell == "S":
                color = YELLOW
            elif cell == "^":
                # Assign a random color to this position if not already assigned
                pos_key = (row_idx, col_idx)
                if pos_key not in decoration_colors_map:
                    decoration_colors_map[pos_key] = random.choice(DECORATION_COLORS)
                color = decoration_colors_map[pos_key]
            else:  # "."
                continue  # Skip drawing dots to keep background

            pygame.draw.rect(surface, color, (x, y, CELL_SIZE, CELL_SIZE))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                # Reset
                f = open("input.txt", "r")
                grid = parse_input(f)
                f.close()
                index = 0
                splits = 0
                finished = False
                paused = False
                decoration_colors_map.clear()  # Clear color map on reset

    # Update logic
    if not paused and not finished and index < len(grid):
        if index < len(grid) - 1:
            new_grid, new_splits = update_grid(grid[index], index)
            grid = new_grid
            splits += new_splits
        index += 1
    elif index >= len(grid):
        finished = True

    # Drawing
    screen.fill(DARK_GREY)

    # Draw grid
    draw_grid(screen, grid)

    # Draw info text
    status_text = "FINISHED" if finished else ("PAUSED" if paused else f"Row: {index}/{len(grid)}")
    info_text = font.render(f"Total splits: {splits} | {status_text}", True, WHITE)
    screen.blit(info_text, (20, 10))

    controls_text = font.render("SPACE: Pause/Resume | R: Reset | ESC: Quit", True, WHITE)
    screen.blit(controls_text, (20, SCREEN_HEIGHT - 30))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
