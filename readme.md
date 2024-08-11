
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
  
## Outputs

#### 1. Regularize Curve
##### Images 
![image](https://github.com/user-attachments/assets/455e3076-0271-4c93-82a0-c1066959c8f2)
![image](https://github.com/user-attachments/assets/5b548668-aef5-44cb-a0d2-092d994eec20)
![image](https://github.com/user-attachments/assets/3e922cfc-e697-4eea-ac55-567ac03135b6)
![image](https://github.com/user-attachments/assets/8376e151-937d-40b2-985e-c27847e6fdf8)

##### video clips 


https://github.com/user-attachments/assets/ddf22ade-4f97-4637-82bf-8719a72f5b1c
https://github.com/user-attachments/assets/2890f99a-ea64-4e82-9ad1-410b67b5a797




#### 2. Find Symmetry
![image](https://github.com/user-attachments/assets/4d8adb91-95a1-474c-a741-901b2f80a347)
![image](https://github.com/user-attachments/assets/8afde725-8258-4e1f-abfe-a9d5f92241f2)

##### video clips 
https://github.com/user-attachments/assets/f9f7daeb-3b08-456b-94d6-36d1c9e58a97

#### 3. Occlude Curve
![image](https://github.com/user-attachments/assets/5d362045-018b-480b-9dd9-50e7d42e2962)
![image](https://github.com/user-attachments/assets/4b4d49b8-4dd9-4d5a-bafd-bb7302b1cfef)

##### video clips

https://github.com/user-attachments/assets/09d8aaf1-2561-41ff-91a8-c1e872fde43c

## Notes

- Ensure that the input image is preprocessed if necessary to isolate the curve clearly.
- The output from each function should be carefully examined to validate the results.


## Acknowledgements

This project uses the RDP algorithm, B-spline smoothing from `scipy.interpolate`, and symmetry analysis techniques from various libraries. Special thanks to the authors and contributors of these libraries and methods.
