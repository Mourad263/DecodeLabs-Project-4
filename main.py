"""
DecodeLabs Internship - Project 4
Image Text Recognition using OCR

This script loads an image, preprocesses it using OpenCV,
extracts text using pytesseract, and saves the output.

Author: Ahmed Mourad
"""

import os
import cv2
import pytesseract


# If Tesseract is not added to PATH on Windows, uncomment this line
# and edit the path according to your installation location:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


INPUT_IMAGE_PATH = os.path.join("sample_images", "sample_text.png")
OUTPUT_IMAGE_PATH = os.path.join("outputs", "processed_image.png")
OUTPUT_TEXT_PATH = os.path.join("outputs", "extracted_text.txt")


def preprocess_image(image_path):
    """
    Preprocess the input image to improve OCR accuracy.

    Steps:
    1. Read the image.
    2. Convert it to grayscale.
    3. Apply Gaussian blur to reduce noise.
    4. Apply adaptive thresholding to create a clear black-and-white image.
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    processed = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return processed


def extract_text(processed_image):
    """
    Extract text from the preprocessed image using pytesseract OCR.
    """
    extracted_text = pytesseract.image_to_string(processed_image)
    return extracted_text.strip()


def save_results(processed_image, extracted_text):
    """
    Save the processed image and extracted text into the outputs folder.
    """
    os.makedirs("outputs", exist_ok=True)

    cv2.imwrite(OUTPUT_IMAGE_PATH, processed_image)

    with open(OUTPUT_TEXT_PATH, "w", encoding="utf-8") as file:
        file.write(extracted_text)


def main():
    print("=" * 60)
    print("Project 4: Image Text Recognition using OCR")
    print("=" * 60)

    processed_image = preprocess_image(INPUT_IMAGE_PATH)
    extracted_text = extract_text(processed_image)
    save_results(processed_image, extracted_text)

    print("\nExtracted Text:")
    print("-" * 60)
    print(extracted_text)
    print("-" * 60)

    print(f"\nProcessed image saved to: {OUTPUT_IMAGE_PATH}")
    print(f"Extracted text saved to: {OUTPUT_TEXT_PATH}")


if __name__ == "__main__":
    main()
