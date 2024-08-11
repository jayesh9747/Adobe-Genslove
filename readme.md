
# Image Curve Analysis and Processing

This project involves performing several image processing operations on curves extracted from images. The operations include regularizing the curve, finding symmetry, and occluding the curve. The implementation utilizes various algorithms and techniques to achieve these goals.

## Operations

### 1. Regularizing the Curve

**Regularization** is achieved through two main techniques:
- **RDP Algorithm**: Reduces the number of points in a curve while preserving its shape.
- **B-Spline Smoothing**: Utilizes the `scipy.interpolate` library for smoothing the curve.

### 2. Finding Symmetry

**Symmetry Detection** is performed using two methods:
- **Vertical Symmetry**: Measured using the Maine Structural Similarity Score.
- **Horizontal Symmetry**: Evaluated through the Fourier Transform.

### 3. Occluding the Curve

**Occlusion Handling** is performed through:
- **Extract Boundaries**: Extracts the boundaries of the curve from the image.
- **Curve Completor**: Completes any incomplete curves based on the extracted boundaries. The `curve_completor` function internally calls the `extract_boundaries` function.

## Usage

### Requirements

Ensure you have the following packages installed:
- `scipy`
- `numpy`
- `matplotlib`
- `opencv-python` (for image processing)
- `skimage`
- `rdp`

You can install them using pip:

```sh
pip install scipy numpy matplotlib opencv-python
```

### Functions

#### 1. Regularize Curve

```python
from your_module import regularize_curve

# Example usage
curve = ...  # Your curve data
regularized_curve = regularize_curve(curve)
```

#### 2. Find Symmetry

```python
from your_module import find_symmetry

# Example usage
image_path = 'path/to/your/image.jpg'
vertical_symmetry = find_symmetry(image_path, direction='vertical')
horizontal_symmetry = find_symmetry(image_path, direction='horizontal')
```

#### 3. Occlude Curve

```python
from curve_completor import CompletingCurve
# Example usage
image_path = 'path/to/your/image.jpg'
completed_curve_plot = curve_completor(image_path)
```

## Example Workflow

1. **Regularize the Curve**:
   - Extract the curve from the image or data.
   - Apply the RDP algorithm and B-spline smoothing to regularize the curve.

2. **Find Symmetry**:
   - Use the Maine Structural Similarity Score to assess vertical symmetry.
   - Apply the Fourier Transform to evaluate horizontal symmetry.

3. **Handle Occlusions**:
   - Use the `curve_completor` function to fill in any incomplete parts of the curve based on boundary extraction.

## Notes

- Ensure that the input image is preprocessed if necessary to isolate the curve clearly.
- The output from each function should be carefully examined to validate the results.


## Acknowledgements

This project uses the RDP algorithm, B-spline smoothing from `scipy.interpolate`, and symmetry analysis techniques from various libraries. Special thanks to the authors and contributors of these libraries and methods.

---

Feel free to modify the content according to the specific details of your project or additional requirements.