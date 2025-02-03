# Image Effects App

A Streamlit application that applies various effects to uploaded images using NumPy array manipulations.

## Effects Available
- Color Pattern: Creates a 4x4 grid with colored overlays
- Simple Grid: Generates a 2x8 repeating pattern
- Complex Pattern: Produces a 4x6 grid with different image flips

## Installation

1. Create a Conda environment:
```bash
conda create -n image_effects python=3.9
conda activate image_effects
```

2. Clone the repository:
```bash
git clone git@github.com:oscarpete/dragndrop.git
cd image-effects-app
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
```
image_app/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── __init__.py
│   └── image_processing.py # Image processing utilities
├── effects/
│   ├── __init__.py
│   ├── color_pattern.py    # Color overlay effect
│   ├── simple_grid.py      # Simple grid pattern
│   └── complex_pattern.py  # Complex grid pattern
└── requirements.txt
```

## Running the App

1. Activate the Conda environment:
```bash
conda activate image_effects
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open browser at http://localhost:8501

## Usage
1. Upload an image using the drag & drop interface
2. Click any effect button to apply the transformation
3. The transformed image will appear below the original

## Note
Large images are automatically resized to prevent memory issues.
