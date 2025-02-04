import numpy as np
from utils.image_processing import ensure_rgb


def create_rgb_shift(image: np.ndarray, shift_amount: int = 20) -> np.ndarray:
    """Create chromatic aberration effect by shifting RGB channels"""
    image = ensure_rgb(image)
    result = np.zeros_like(image)

    # Shift red channel left
    result[:, :, 0] = np.roll(image[:, :, 0], -shift_amount, axis=1)
    # Keep green channel
    result[:, :, 1] = image[:, :, 1]
    # Shift blue channel right
    result[:, :, 2] = np.roll(image[:, :, 2], shift_amount, axis=1)

    return result
