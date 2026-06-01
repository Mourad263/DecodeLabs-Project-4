# DecodeLabs Internship - Project 4

## Project Title

**Image Text Recognition using OCR**

## Project Overview

This project was completed as part of the DecodeLabs AI Internship.

The objective of this project is to implement a basic image/text recognition task using available Python libraries. The project focuses on Optical Character Recognition (OCR), where a machine reads text from an image and converts it into editable digital text.

In this project, an input image is loaded, preprocessed using OpenCV, and then passed to the Tesseract OCR engine through the `pytesseract` Python library. The final output is the extracted text from the image, saved clearly in a text file.

## Project Objective

The main objective is to build a simple OCR pipeline that can:

- Read an image input.
- Improve the image quality using preprocessing.
- Extract readable text using OCR.
- Save the processed image.
- Save the extracted text in a clear output file.

## Project Files

| File Name | Format | Description |
|---|---|---|
| main.py | Python File | Main source code for running the OCR project |
| notebook.ipynb | Jupyter Notebook | Step-by-step implementation with explanation and outputs |
| requirements.txt | Text File | Required Python libraries |
| README.md | Markdown File | Project documentation |
| sample_text.png | PNG Image | Sample input image used for OCR |
| processed_image.png | PNG Image | Output image after preprocessing |
| extracted_text.txt | Text File | Text extracted from the image |

## Technologies Used

- Python
- OpenCV
- pytesseract
- Tesseract OCR Engine
- Pillow
- Matplotlib
- Jupyter Notebook

## Algorithm / Technique Used

This project uses **Optical Character Recognition (OCR)**.

OCR is a computer vision technique used to recognize and extract text from images. Instead of manually typing text from an image, OCR allows the machine to detect characters and convert them into digital text.

The OCR process in this project follows these steps:

1. Load the input image.
2. Convert the image to grayscale.
3. Apply Gaussian blur to reduce noise.
4. Apply adaptive thresholding to improve text visibility.
5. Use pytesseract to extract text.
6. Save the processed image and extracted text.

## Methodology

### 1. Image Loading

The image is loaded using OpenCV from the `sample_images` folder.

### 2. Grayscale Conversion

The image is converted from RGB/BGR color format into grayscale. This reduces the image from three color channels into one intensity channel, making it easier for OCR to process.

### 3. Noise Reduction

Gaussian blur is applied to reduce small noise and smooth the image.

### 4. Adaptive Thresholding

Adaptive thresholding converts the grayscale image into a black-and-white image. This helps separate the text from the background and improves OCR accuracy.

### 5. Text Extraction

The preprocessed image is passed to pytesseract, which extracts the readable text.

### 6. Output Saving

The project saves:

- The processed image in `outputs/processed_image.png`
- The extracted text in `outputs/extracted_text.txt`

## How to Run the Project

### Step 1: Install Python Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Install Tesseract OCR

You must install Tesseract OCR on your computer.

For Windows, download and install it from the official Tesseract installer.  
After installation, if Python cannot find Tesseract, open `main.py` and uncomment this line:

```python
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### Step 3: Run the Python File

```bash
python main.py
```

## Expected Output

The program prints the extracted text in the terminal and saves the result into the outputs folder.

Example output:

```text
Extracted Text:
DecodeLabs Internship - Project 4
Image Text Recognition using OCR
Student Name: Zeyad Mohamed
Goal: Extract readable text from an image.
```

## Project Result

The OCR system successfully reads text from an image after applying preprocessing techniques. The final output demonstrates that a machine can process visual input and convert it into machine-readable text.

## Possible Enhancements

This project can be improved in the future by:

- Adding support for multiple images.
- Adding a graphical user interface.
- Supporting PDF-to-text extraction.
- Improving OCR accuracy using deskewing.
- Supporting Arabic OCR.
- Adding object detection as a second recognition path.
- Exporting results into CSV or Excel files.

## Conclusion

This project demonstrates a basic but important computer vision task: extracting text from images. By combining OpenCV preprocessing with pytesseract OCR, the system can convert visual text into editable digital text. This project is a practical introduction to image recognition and machine perception.
