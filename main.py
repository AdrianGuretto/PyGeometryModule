from src import generator
from src import operations
from src import visualization

# Генерация фигур
shapes_generator = generator.generate_shapes()
figures = [next(shapes_generator) for _ in range(1)]

# Визуализация исходных фигур
print("Исходные фигуры:")
visualization.visualize(figures)

# Применение операций

translated_figures = operations.tr_translate(figures, (2, 2))
rotated_figures = operations.tr_rotate(figures, 45)
symmetric_figures = operations.tr_symmetry(figures, (0, 0))
homothetic_figures = operations.tr_homothety(figures, 2)

# Визуализация преобразованных фигур
print("Преобразованные фигуры:")
visualization.visualize(translated_figures)
visualization.visualize(rotated_figures)
visualization.visualize(symmetric_figures)
visualization.visualize(homothetic_figures)