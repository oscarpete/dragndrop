import numpy as np
from PIL import Image


def preprocess_image(image, max_dimension=1000):
    width, height = image.size
    if max(width, height) > max_dimension:
        scale = max_dimension / max(width, height)
        new_size = (int(width * scale), int(height * scale))
        return image.resize(new_size, Image.Resampling.LANCZOS)
    return image


def ensure_rgb(image: np.ndarray) -> np.ndarray:
    """Convert image to RGB format"""
    if len(image.shape) == 2:
        return np.stack([image] * 3, axis=-1)
    elif image.shape[2] == 4:  # RGBA
        return image[..., :3]  # Keep only RGB channels
    return image


def flip_image(image: np.ndarray, flip_type: int) -> np.ndarray:
    """Flip image based on flip type"""
    result = image.copy()
    if flip_type & 1:  # Left-right flip
        result = np.fliplr(result)
    if flip_type & 2:  # Up-down flip
        result = np.flipud(result)
    return result
