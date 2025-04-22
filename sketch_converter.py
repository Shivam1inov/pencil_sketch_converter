import cv2

def convert_to_sketch(input_path: str, output_path: str = "sketch.png"):
    # Read the image
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {input_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert the grayscale image
    inv = 255 - gray

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(inv, (21, 21), 0)

    # Create the pencil sketch
    sketch = cv2.divide(gray, 255 - blur, scale=256.0)

    # Save the result
    cv2.imwrite(output_path, sketch)
    print(f"Sketch saved to {output_path}")

if __name__ == "__main__":
    convert_to_sketch(input("Enter your image file : "))
