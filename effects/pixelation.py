import numpy as np
from utils.image_processing import ensure_rgb


def create_pixelation(image: np.ndarray, block_size: int = 20) -> np.ndarray:
    """Create pixelation effect using array reshaping and averaging"""
    image = ensure_rgb(image)
    h, w = image.shape[:2]

    # Calculate new dimensions that are divisible by block_size
    new_h = h - (h % block_size)
    new_w = w - (w % block_size)

    # Crop image to be divisible by block_size
    image = image[:new_h, :new_w]

    # Reshape and average blocks
    temp = image.reshape(
        new_h // block_size, block_size, new_w // block_size, block_size, 3
    )
    blocked = temp.mean(axis=(1, 3))

    # Scale back up using np.repeat
    result = np.repeat(np.repeat(blocked, block_size, axis=0), block_size, axis=1)

    return result.astype(np.uint8)
