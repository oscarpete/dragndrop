import numpy as np
from utils.image_processing import ensure_rgb, flip_image


def create_complex_pattern(image: np.ndarray) -> np.ndarray:
    """Create a complex 4x6 grid pattern with different flips"""
    image = ensure_rgb(image)
    h, w = image.shape[:2]

    matrix = np.array([[j % 4 for i in range(6)] for j in range(4)])
    rows, cols = matrix.shape
    result = np.zeros((h * rows, w * cols, 3), dtype=image.dtype)

    for i in range(rows):
        for j in range(cols):
            flipped = flip_image(image, matrix[i, j])
            result[i * h : (i + 1) * h, j * w : (j + 1) * w] = flipped

    return result
