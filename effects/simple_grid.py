import numpy as np
from utils.image_processing import ensure_rgb, flip_image


def create_simple_grid(image: np.ndarray) -> np.ndarray:
    """Create a simple 2x8 grid pattern"""
    image = ensure_rgb(image)
    h, w = image.shape[:2]

    matrix = np.array([[0] * 8] * 2)
    rows, cols = matrix.shape
    result = np.zeros((h * rows, w * cols, 3), dtype=image.dtype)

    for i in range(rows):
        for j in range(cols):
            flipped = flip_image(image, matrix[i, j])
            result[i * h : (i + 1) * h, j * w : (j + 1) * w] = flipped

    return result
