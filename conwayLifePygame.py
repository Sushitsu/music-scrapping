import pygame
import random
import time

# La taille de la grille
grid_size = 30

# La probabilité qu'une cellule soit initialement vivante
init_proba = 0.2

# Le nombre d'itérations pour exécuter la simulation
num_iterations = 100

# La taille de chaque cellule en pixels
cell_size = 20

# La couleur de la cellule vivante
alive_color = (255, 255, 255)
dead_color = (0, 0, 0)


def create_grid():
    """Crée une grille vide de la taille spécifiée."""
    return [[0 for _ in range(grid_size)] for _ in range(grid_size)]


def initialize_grid(grid):
    """Initialiser au hasard la grille avec des cellules vivantes."""
    for i in range(grid_size):
        for j in range(grid_size):
            if random.random() < init_proba:
                grid[i][j] = 1


def count_neighbors(grid, x, y):
    """Comptez le nombre de voisins vivants autour d'une cellule."""
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_x = x + i
            neighbor_y = y + j
            if i == 0 and j == 0:
                continue
            elif neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= grid_size or neighbor_y >= grid_size:
                continue
            elif grid[neighbor_x][neighbor_y] == 1:
                count += 1
    return count


def update_grid(grid):
    """Mettez à jour la grille pour une itération de la simulation."""
    new_grid = create_grid()
    for i in range(grid_size):
        for j in range(grid_size):
            num_neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1:
                if num_neighbors < 2 or num_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if num_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid


def draw_grid(screen, grid):
    """Dessinez l'état actuel de la grille sur l'écran."""
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:
                color = alive_color
            else:
                color = dead_color
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)


def run_simulation():
    """Exécutez la simulation pour le nombre d'itérations spécifié."""
    pygame.init()
    screen = pygame.display.set_mode((grid_size * cell_size, cell_size * cell_size))
    grid = create_grid()
    initialize_grid(grid)
    for i in range(num_iterations):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        draw_grid(screen, grid)
        pygame.display.update()
        grid = update_grid(grid)
        time.sleep(0.1)
    pygame.quit()


if __name__ == '__main__':
    run_simulation()
