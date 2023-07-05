import random
import time
import os

height = 65
width = 250

def random_matrix():
    matrix = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]
    return matrix

def render(matrix):
    for _ in range(width):
        print('_', end="")
    for y in range(height):
        print("\n|", end="")
        for x in range(width):
            if matrix[y][x] == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print('|', end="")
    print("\n")

def next_board_state(matrix):
    matrix2 = [[0] * width for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            n = count_live_neighbors(matrix, y, x)
            if n <= 1:
                matrix2[y][x] = 0
            elif n == 3:
                matrix2[y][x] = 1
            elif n > 3:
                matrix2[y][x] = 0
            elif n == 2 and matrix[y][x] == 1:
                matrix2[y][x] = 1
    return matrix2

def count_live_neighbors(matrix, y, x):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    count = 0
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and matrix[ny][nx] == 1:
            count += 1
    return count

matrix = random_matrix()

while True:
    os.system("cls")
    render(matrix)
    matrix = next_board_state(matrix)
    time.sleep(1)
    #n = input()
