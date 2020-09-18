import pygame
import random
import sys

print()
print("Enter the number of rooms horizontally (columns)")
a = int(input())
print("Enter the number of rooms vertically (rows)")
b = int(input())
width = a * 50  # ширина игрового окна
height = b * 50  # высота игрового окна
fps = 10  # частота кадров в секунду



color = (128, 128, 128)  # для цвета фона
# -----------------------------------------------------
room = 50  # определил плитку размер
cols = int(width / room)  # число колонн
rows = int(height / room)  # число рядов
# -----------------------------------------------------

pygame.init()  # команда, которая запускает pygame.
screen = pygame.display.set_mode((width, height))  # окно программы
pygame.display.set_caption("Task_6 Labirint")
clock = pygame.time.Clock()  # игра работает с заданной частотой кадров.


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls_t = True
        self.walls_b = True
        self.walls_l = True
        self.walls_r = True
        self.visited = False

    def __repr__(self, *args, **kwargs):
        return f"точка:{self.x, self.y, self.walls_t, self.walls_b, self.walls_l, self.walls_r, self.visited}"

    def cur_room(self):
        x = self.x * 50
        y = self.y * 50
        pygame.draw.rect(screen, pygame.Color("Red"), (x + 2, y + 2, room - 3, room - 3))

    def draw(self):
        x = self.x * room
        y = self.y * room

        if self.visited is True:
            pygame.draw.rect(screen, pygame.Color("LIGHTBLUE"), (x, y, room, room))

        if self.walls_t is True:
            pygame.draw.line(screen, pygame.Color('WHITE'), (x, y), (x + room, y), 3)
            # print("top",(x, y), (x + room, y))

        if self.walls_r is True:
            pygame.draw.line(screen, pygame.Color('WHITE'), (x + room, y), (x + room, y + room), 3)

        if self.walls_b == 1:
            pygame.draw.line(screen, pygame.Color('WHITE'), (x + room, y + room), (x, y + room), 3)

        if self.walls_l == 1:
            pygame.draw.line(screen, pygame.Color('WHITE'), (x, y + room), (x, y), 3)

    def go(self):
        go_ = []
        top = coord(w=self.x, ww=self.y - 1)
        right = coord(w=self.x + 1, ww=self.y)
        bottom = coord(w=self.x, ww=self.y + 1)
        left = coord(w=self.x - 1, ww=self.y)
        if top and top.visited is False:
            go_.append(top)
        if right and right.visited is False:
            go_.append(right)
        if bottom and bottom.visited is False:
            go_.append(bottom)
        if left and left.visited is False:
            go_.append(left)
        if go_:
            return random.choice(go_)
        else:
            return False


"""Находим элемент в одномерном массиве по индексу по координатам"""


def coord(w, ww):
    index = w + ww * cols
    if w < 0 or w > cols - 1 or ww < 0 or ww > rows - 1:
        return False
    return grid_cells[index]


"""Удаляем стенки"""


def del_walls(current_cell, next_room):
    dx = current_cell.x - next_room.x
    if dx == 1:
        current_cell.walls_l = False
        next_room.walls_r = False
    elif dx == -1:
        current_cell.walls_r = False
        next_room.walls_l = False
    dy = current_cell.y - next_room.y
    if dy == 1:
        current_cell.walls_t = False
        next_room.walls_b = False
    elif dy == -1:
        current_cell.walls_b = False
        next_room.walls_t = False


""" Создаем экземпляры с координатами точек"""
grid_cells = []
for row in range(rows):
    for col in range(cols):
        a = Room(col, row)
        grid_cells.append(a)

print(grid_cells)

current_cell = grid_cells[0]
stack = []

while 1:  # программа закрывается при клике на крестик окна.
    screen.fill(color)  # залил цветом экран

    for i in pygame.event.get():
        if i.type == pygame.QUIT:  # События клавиатуры могут быть двух типов (иметь одно из двух значений type)
            # – клавиша была нажата, клавиша была отпущена
            pygame.quit()
            sys.exit()

    """РИСУЕМ СЕТКУ"""
    for j in grid_cells:
        j.draw()

    current_cell.visited = True

    current_cell.cur_room()  # Придали цвет текущей ячейке

    next_room = current_cell.go()  # ищем след. случайно ячейку, рядом с текущей
    if next_room:

        next_room.visited = True
        stack.append(current_cell)
        del_walls(current_cell, next_room)
        current_cell = next_room
    elif stack:
        current_cell = stack.pop()

    # pygame.display.update()
    # clock.tick(fps)  # Держим цикл на правильной скорости

    # Обязательно для шаблона в Pygame
    pygame.display.flip()
    clock.tick(fps)
