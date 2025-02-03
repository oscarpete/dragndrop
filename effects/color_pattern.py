import numpy as np
from utils.image_processing import ensure_rgb


def resize_array(image: np.ndarray, new_size) -> np.ndarray:
    """Resize numpy array using nearest neighbor interpolation"""
    h, w = new_size
    h_factor, w_factor = h / image.shape[0], w / image.shape[1]
    y_coords = np.arange(h).reshape(-1, 1) / h_factor
    x_coords = np.arange(w) / w_factor
    y_indices = np.clip(y_coords.astype(int), 0, image.shape[0] - 1)
    x_indices = np.clip(x_coords.astype(int), 0, image.shape[1] - 1)
    return image[y_indices, x_indices]


def create_colorful_big_one(image: np.ndarray, alpha: float = 0.5) -> np.ndarray:
    """Create a 4x4 pattern with colored overlays"""
    image = ensure_rgb(image)
    h, w = image.shape[:2]

    cell_h = h // 4
    cell_w = w // 4

    grid_h = cell_h * 4
    grid_w = cell_w * 4
    result = np.zeros((grid_h, grid_w, 3), dtype=np.uint8)

    colors = {
        "blue": np.array([0, 0, 255], dtype=np.uint8),
        "red": np.array([255, 0, 0], dtype=np.uint8),
        "green": np.array([0, 255, 0], dtype=np.uint8),
    }

    def place_image_with_overlay(y, x, overlay_color):
        y_start, y_end = y * cell_h, (y + 1) * cell_h
        x_start, x_end = x * cell_w, (x + 1) * cell_w

        cell_img = resize_array(image, (cell_h, cell_w))

        result[y_start:y_end, x_start:x_end] = cell_img

        cell = result[y_start:y_end, x_start:x_end].astype(float)
        overlay = overlay_color.astype(float)
        result[y_start:y_end, x_start:x_end] = (
            cell * (1 - alpha) + overlay * alpha
        ).astype(np.uint8)

    # Apply pattern
    for j in range(4):
        place_image_with_overlay(0, j, colors["blue"])
        place_image_with_overlay(3, j, colors["green"])

    place_image_with_overlay(1, 0, colors["red"])
    place_image_with_overlay(2, 0, colors["red"])
    place_image_with_overlay(1, 3, colors["red"])
    place_image_with_overlay(2, 3, colors["red"])

    # Center image
    center_y_start, center_y_end = cell_h, 3 * cell_h
    center_x_start, center_x_end = cell_w, 3 * cell_w

    center_img = resize_array(image, (2 * cell_h, 2 * cell_w))
    result[center_y_start:center_y_end, center_x_start:center_x_end] = center_img

    return result
