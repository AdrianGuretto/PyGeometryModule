# Этот файл отвечает за генерацию координат фигур

from typing import List, Tuple, Generator
import itertools
import math

def gen_rectangle() -> List[Tuple[float, float]]:
    """
    Генерация прямоугольника.

    Returns:
    - List[Tuple[float, float]]: Список координат вершин прямоугольника.
    """
    x1, y1 = 0, 0
    width, height = 1, 1
    x2, y2 = x1 + width, y1
    x3, y3 = x1 + width, y1 + height
    x4, y4 = x1, y1 + height
    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

def gen_triangle() -> List[Tuple[float, float]]:
    """
    Генерация треугольника.

    Returns:
    - List[Tuple[float, float]]: Список координат вершин треугольника.
    """
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 0.5, math.sqrt(3) / 2
    return [(x1, y1), (x2, y2), (x3, y3)]

def gen_hexagon() -> List[Tuple[float, float]]:
    """
    Генерация правильного шестиугольника.

    Returns:
    - List[Tuple[float, float]]: Список координат вершин шестиугольника.
    """
    vertices = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        x = math.cos(angle_rad)
        y = math.sin(angle_rad)
        vertices.append((x, y))
    return vertices

def generate_shapes() -> Generator[List[Tuple[float, float]], None, None]:
    """
    Генерация различных фигур.

    Yields:
    - List[Tuple[float, float]]: Список координат вершин фигуры.
    """
    generators = [gen_rectangle, gen_triangle, gen_hexagon]
    for generator in itertools.cycle(generators):
        yield generator()