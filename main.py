import matplotlib.pyplot as plt
import matplotlib.patches as patches
from src.generator import gen_rect, gen_triangle
from src import operations as op

# Создать фигуру и оси для отображения прямоугольников
fig, ax = plt.subplots()

rects = []

# Создать эталонный прямоугольник
first_square = patches.Rectangle(xy=(0, 0), width=4, height=3, color='green', alpha=0.4, angle=45)

rects.append(first_square)
# Сгенерировать последующие прямоугольники
for rect in gen_rect(first_square, angle=45):
    rects.append(rect)

for rect in op.tr_translate(rects, 5, 2):
    ax.add_patch(rect)
    

# Сгенерировать последующие треугольники
first_triangle = patches.RegularPolygon(xy=(4, -3), numVertices=3, radius=1, orientation=315,
                                        color='blue', alpha=0.4)
triangles = []
for triangle in gen_triangle(first_triangle, angle=120):
    ax.add_patch(triangle)

# Настроить оси
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Показать результат
plt.show()
