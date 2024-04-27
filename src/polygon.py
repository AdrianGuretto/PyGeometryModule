# В этом файле хрянтся классы и функции, связанные с самими полигонами

from typing import List, Tuple
import math

class Polygon:
    def __init__(self, points: List[Tuple[float, float]]):
        self.points = points

    def translate(self, vector: Tuple[float, float]) -> 'Polygon':
        """
        Параллельный перенос полигона на вектор.

        Parameters:
        - vector: Tuple[float, float] - вектор переноса (dx, dy).

        Returns:
        - Polygon: Новый экземпляр класса Polygon, представляющий перенесенный полигон.
        """
        translated_points = [(x + vector[0], y + vector[1]) for x, y in self.points]
        return Polygon(translated_points)

    def rotate(self, angle: float) -> 'Polygon':
        """
        Поворот полигона на заданный угол.

        Parameters:
        - angle: float - угол поворота в радианах.

        Returns:
        - Polygon: Новый экземпляр класса Polygon, представляющий повернутый полигон.
        """
        rotated_points = []
        ox, oy = 0, 0  # Определяем точку вращения (например, центр полигона)
        for x, y in self.points:
            qx = ox + math.cos(angle) * (x - ox) - math.sin(angle) * (y - oy)
            qy = oy + math.sin(angle) * (x - ox) + math.cos(angle) * (y - oy)
            rotated_points.append((qx, qy))
        return Polygon(rotated_points)

    def symmetry(self, axis: Tuple[float, float]) -> 'Polygon':
        """
        Отражение полигона относительно заданной оси симметрии.

        Parameters:
        - axis: Tuple[float, float] - координаты точки, через которую проходит ось симметрии.

        Returns:
        - Polygon: Новый экземпляр класса Polygon, представляющий отраженный полигон.
        """
        symmetrical_points = [(2 * axis[0] - x, 2 * axis[1] - y) for x, y in self.points]
        return Polygon(symmetrical_points)

    def homothety(self, factor: float) -> 'Polygon':
        """
        Гомотетия полигона относительно начала координат.

        Parameters:
        - factor: float - коэффициент гомотетии.

        Returns:
        - Polygon: Новый экземпляр класса Polygon, представляющий гомотетически измененный полигон.
        """
        homothetic_points = [(factor * x, factor * y) for x, y in self.points]
        return Polygon(homothetic_points)